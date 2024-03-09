import logging
import time
import openai

logging.getLogger("openai").setLevel(logging.ERROR)
logging.getLogger("http.client").setLevel(logging.ERROR)

# from langchain.chat_models import ChatOpenAI
# from langchain_community.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable import Runnable
from langchain.schema.runnable.config import RunnableConfig

import chainlit as cl


@cl.on_chat_start
async def on_chat_start():
    model = ChatOpenAI(streaming=True)
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a Python Coder. You create Python code snippets from natural language requests and explain them in easy-to-understand English, suitable even for a 5-year-old.",
            ),
            ("human", "{question}"),
        ]
    )
    runnable = prompt | model | StrOutputParser()
    cl.user_session.set("runnable", runnable)

    # Send a system message when the chat starts
    system_message = cl.Message(content="I am an AI Python Coder, I will help you create python code and explain it to you like a 5-year old")
    await system_message.send()

   

@cl.on_message
async def on_message(message: cl.Message):
    runnable = cl.user_session.get("runnable") 

    msg = cl.Message(content="")

    start_time = time.time()

    try:    
        async for chunk in runnable.astream(
            {"question": message.content},
            config=RunnableConfig(callbacks=[cl.LangchainCallbackHandler()]),
        ):
            await msg.stream_token(chunk)
    except openai.RateLimitError:
        print("Rate limit exceeded.")
        

    end_time = time.time()

    print(f"Response time: {end_time - start_time} seconds")


    await msg.send()
