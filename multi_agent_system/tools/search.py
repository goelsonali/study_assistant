"""Wrapper to Google Search Grounding with custom prompt."""

from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools.google_search_tool import google_search

MODEL_GEMINI_2_0_FLASH = "gemini-2.0-flash"

_search_agent = Agent(
    model=MODEL_GEMINI_2_0_FLASH,
    name="google_search_grounding",
    description="An agent providing Google-search grounding capability",
    instruction=""",
    Answer the user's question directly using google_search grounding tool; Provide a brief but concise response. 
    Rather than a detail response, provide the actionable item for a user to the users's query.
    """,
    tools=[google_search],
)

google_search_grounding = AgentTool(agent=_search_agent)