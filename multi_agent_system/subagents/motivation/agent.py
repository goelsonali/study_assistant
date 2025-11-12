"""Content Agent is a specialist in simplifying complex topics researched from Google."""

import os
from google.adk.agents import LlmAgent
from . import prompt
from dotenv import load_dotenv
from multi_agent_system.subagents.chat.agent import chat_agent
from multi_agent_system.subagents.content.agent import content_agent
from multi_agent_system.subagents.quiz.agent import quiz_agent

load_dotenv()

GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')

MODEL_GEMINI_2_0_FLASH = "gemini-2.0-flash"

motivation_agent = LlmAgent(
    model=MODEL_GEMINI_2_0_FLASH,
    name="motivation_agent",
    description="The motivation agent is designed to uplift and encourage the learner throughout their study journey.",
    instruction=prompt.MOTIVATION_AGENT_PROMPT
)