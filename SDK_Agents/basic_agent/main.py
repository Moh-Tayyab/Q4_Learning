import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent, Runner, OpenAIChatCompletionsModel
import asyncio
import chainlit as cl

load_dotenv()

# Create agent at global scope
gemini_api_key = os.getenv('GEMINI_API_KEY')

client = AsyncOpenAI(
    api_key = gemini_api_key,
     base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

agent = Agent(
    name="ExpertAgent",
    instructions="You are a highly skilled and knowledgeable expert agent, capable of providing accurate and effective solutions.",
    model = OpenAIChatCompletionsModel(model = 'gemini-2.0-flash', openai_client = client,)
)

@cl.on_message   
async def handle_message(message: cl.Message):
    result = await Runner.run(
        agent,
        input=message.content
    ) 
    await cl.Message(content=result.final_output).send()   


