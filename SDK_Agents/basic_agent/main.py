import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent, Runner, OpenAIChatCompletionsModel
#import google.generativeai as genai

load_dotenv()

def main():
    gemini_api_key = os.getenv('GEMINI_API_KEY')
    
    client = AsyncOpenAI(
        api_key = gemini_api_key,
         base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    )
    
    agent = Agent(
        name = 'Assistant',
        instructions = "You are expert agent",
        model = OpenAIChatCompletionsModel(
            model = 'gemini-2.0-flash',
            openai_client = client,
            )
    )
    
    query = input("Enter your query: ")
    
    result = Runner.run_sync(
        agent, 
        query
    )
    
    print(result.final_output)

if __name__ == "__main__":
    main()
