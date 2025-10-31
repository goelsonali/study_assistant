import os
from google.adk.agents import LlmAgent
from dotenv import load_dotenv
from .subagent.chat.agent import chat_agent

# Load environment variables from .env file
load_dotenv()

GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')

# More supported models can be referenced here: https://ai.google.dev/gemini-api/docs/models#model-variations
MODEL_GEMINI_2_0_FLASH = "gemini-2.0-flash"

root_agent = LlmAgent(
    model=MODEL_GEMINI_2_0_FLASH,
    name="root_agent",
    description="An agent that coordinates the flow of information and delegates tasks to specialized subagents in a study assistant system.",
    sub_agents=[chat_agent]
)