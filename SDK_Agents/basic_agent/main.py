from agents import Agent, Runner
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

GOOGLE_KEY = os.getenv("GOOGLE_API_KEY")

client = AsyncOpenAI(
    api_key=GOOGLE_KEY,
    base_url=""
)

agent = Agent(
    name = "basic_agent",
    instructions = "You are a helpful assistant. Answer's question to the best of your ability"
)

query = "what is the capital of UK?"

result = Runner.run_sync(
    agent,
    query 
)

print(result.final_output)