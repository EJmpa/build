# Python Code Generation and Explanation AI

## Overview

This project implements an AI-powered Python code generation and explanation tool using OpenAI's GPT-3.5 language model. The system is designed to generate Python code snippets from natural language requests and provide clear explanations in easy-to-understand English, suitable even for a 5-year-old.

## Features

- **Code Generation:** Utilizes OpenAI API to generate Python code snippets based on natural language input.
- **Code Explanation:** Provides explanations of the generated code in a manner suitable for users of all ages, including 5-year-olds.
- **Real-time Interaction:** Implements a real-time chat interface for users to input questions and receive instant responses.

## Getting Started

### Prerequisites

- [OpenAI API Key](https://beta.openai.com/signup/): Obtain your OpenAI API key to enable interaction with the GPT-3.5 language model.

### Installation

1. Clone the repository:
   \`\`\`bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   \`\`\`

Install dependencies:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

## Usage

Run the application:

\`\`\`bash
chainlit run run.py -w
\`\`\`

Start interacting with the AI Python Coder:

Send natural language requests as messages to the system.

## Project Structure

- `run.py`: Main script implementing the AI Python Coder using the ChainLit framework.
- `langchain_openai`: Package for interacting with the OpenAI API.
- `langchain.prompts`: Module defining templates for system and user messages.
- `langchain.schema`: Module containing modules for defining the schema, runnable configurations, and callback handling.

## Metrics and Evaluation

The project is evaluated using a simple metrics: `Response time (Latency)`



## Acknowledgments

- OpenAI for providing the GPT-3.5 language model.
- ChainLit framework for simplifying the implementation of conversational AI.
- langchain for interacting/communicating with the OpenAI API.


Remember to customize the placeholders (`your-username`, `your-repo`, `your-api-key`, `your-email@example.com`).
\`\`\`
```