"""Quiz Agent is a specialist in creating quizes for the content provided."""

from google.adk.agents import Agent
from multi_agent_system.subagents.content.agent import content_agent

MODEL_GEMINI_2_0_FLASH = "gemini-2.0-flash"

# 1. ROLE PROMPTING & FEW-SHOT Concept: Defined in the system instruction
QUIZ_AGENT_PROMPT = (
    "Quiz Master. Your task is to generate a 3-question quiz in a structured JSON format (q, a, topic) "
    "based STRICTLY on the content provided. The following JSON structure MUST be strictly followed: "
    "[{\"q\": \"...\", \"a\": \"...\", \"topic\": \"...\"}, ...]. This is a Few-Shot instruction."
)

quiz_agent = Agent(
    model=MODEL_GEMINI_2_0_FLASH,
    name="quiz_agent",
    description="Quiz Agent is a specialist in creating quizes for the content provided.",
    instruction=QUIZ_AGENT_PROMPT,
    subagents=[content_agent]
)