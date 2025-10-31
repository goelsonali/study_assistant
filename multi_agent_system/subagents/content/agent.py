"""Content Agent is a specialist in simplifying complex topics researched from Google."""

from google.adk.agents import Agent
from multi_agent_system.tools.search import google_search_grounding

MODEL_GEMINI_2_0_FLASH = "gemini-2.0-flash"

# 1. ROLE PROMPTING: Defining the agent's identity via the description/system instruction
CONTENT_AGENT_PROMPT = (
    "Content Researcher. You are a highly-regarded specialist in simplifying complex topics. "
    "Your task is to find and summarize a key resource from the web. Respond in an academic but friendly tone."
)

content_agent = Agent(
    model=MODEL_GEMINI_2_0_FLASH,
    name="content_agent",
    description="Given some text, search Google for the most relevant, trustworthy, and helpful online resources summarize in beginner-friendly tone",
    instruction=CONTENT_AGENT_PROMPT,
    tools=[google_search_grounding]
)