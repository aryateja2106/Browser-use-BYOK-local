import os
import sys
import argparse
import asyncio

from langchain_google_genai import ChatGoogleGenerativeAI
from mlx_use import Agent
from pydantic import SecretStr
from mlx_use.controller.service import Controller


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def set_llm(llm_provider:str = "google"):
    if llm_provider == "google":
        api_key = os.getenv('GEMINI_API_KEY')
        return ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(api_key))
    else:
        raise ValueError(f"Unsupported LLM provider: {llm_provider}")

llm = set_llm('google')
controller = Controller()

async def main():
    parser = argparse.ArgumentParser(description="Run macOS-use agent with a specified task.")
    parser.add_argument("--task", type=str, required=True, help="The task for the agent to perform.")
    args = parser.parse_args()

    agent = Agent(
        task=args.task,
        llm=llm,
        controller=controller,
        use_vision=False,
        max_actions_per_step=10,
    )
    await agent.run(max_steps=25)

if __name__ == "__main__":
    asyncio.run(main())
