"""Content Agent is a specialist in simplifying complex topics researched from Google."""

from google.adk.agents import Agent
from multi_agent_system.subagents.quiz.agent import quiz_agent

MODEL_GEMINI_2_0_FLASH = "gemini-2.0-flash"

# 1. ROLE PROMPTING: Defining the agent's identity via the description/system instruction
REFLECTOR_AGENT_PROMPT = (
    "Critical Reflector. Review the generated quiz against the source content and confirm that all questions "
    "and answers align with the provided material. Output 'Reflection Passed' or 'Reflection Failed'."
)

reflector_agent = Agent(
    model=MODEL_GEMINI_2_0_FLASH,
    name="reflector_agent",
    description="Given some text, search Google for the most relevant, trustworthy, and helpful online resources summarize in beginner-friendly tone",
    instruction=REFLECTOR_AGENT_PROMPT,
    subagents=[quiz_agent]
)