import logging
import time
import openai
import chainlit as cl

# from langchain.chat_models import ChatOpenAI
# from langchain_community.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable import Runnable
from langchain.schema.runnable.config import RunnableConfig

# Suppress unnecessary logs
logging.getLogger("openai").setLevel(logging.DEBUG)
logging.getLogger("http.client").setLevel(logging.ERROR)


@cl.on_chat_start
async def on_chat_start() -> None:
    """
    Initialize the chat session with necessary components.
    """
    # Initialize ChatOpenAI model with streaming enabled
    model: ChatOpenAI = ChatOpenAI(streaming=True)
    
    # Define a prompt for the conversation
    prompt: ChatPromptTemplate = ChatPromptTemplate.from_messages([
        ("system", "You are a Python Coder. You create Python code snippets from natural language requests and explain them in easy-to-understand English, suitable even for a 5-year-old."),
        ("human", "{question}"),
    ])
    
    # Construct a runnable pipeline
    runnable: Runnable = prompt | model | StrOutputParser()
    
    # Set the runnable pipeline in user session
    cl.user_session.set("runnable", runnable)
    
    # Send a system message when the chat starts
    system_message: cl.Message = cl.Message(content="I am an AI Python Coder, I will help you create python code and explain it to you like a 5-year old")
    await system_message.send()


@cl.on_message
async def on_message(message: cl.Message) -> None:
    """
    Respond to user messages.
    """
    # Retrieve the runnable pipeline from user session
    runnable: Runnable = cl.user_session.get("runnable")
    
    # Initialize an empty message
    msg: cl.Message = cl.Message(content="")
    
    # Measure response time
    start_time: float = time.time()
    
    try:
        # Process the user message asynchronously
        async for chunk in runnable.astream(
            {"question": message.content},
            config=RunnableConfig(callbacks=[cl.LangchainCallbackHandler()]),
        ):
            await msg.stream_token(chunk)
    except openai.RateLimitError:
        print("Rate limit exceeded.")
    
    # Calculate response time
    end_time: float = time.time()
    print(f"Response time: {end_time - start_time} seconds")
    
    # Send the message response
    await msg.send()
