"""Content Agent is a specialist in simplifying complex topics researched from Google."""

from google.adk.agents import Agent
from . import prompt
from multi_agent_system.subagents.chat.agent import chat_agent

MODEL_GEMINI_2_0_FLASH = "gemini-2.0-flash"

motivation_agent = Agent(
    model=MODEL_GEMINI_2_0_FLASH,
    name="motivation_agent",
    description="The motivation agent is designed to uplift and encourage the learner throughout their study journey.",
    instruction=prompt.MOTIVATION_AGENT_PROMPT,
    sub_agents=[chat_agent]
)