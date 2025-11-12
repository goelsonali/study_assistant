import os
import asyncio
import json
from typing import Any
from rich import print
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import (
    MCPToolset,
    SseServerParams,
)

from dotenv import load_dotenv
from .subagents.chat.agent import chat_agent
from .subagents.motivation.agent import motivation_agent

# Load environment variables from .env file
load_dotenv()


root_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="assistant_agent",
    description="An agent that coordinates the flow of information and delegates tasks to specialized subagents in a study assistant system.",
    sub_agents=[chat_agent, motivation_agent],
    #tools=[MCPToolset(
    #        connection_params=SseServerParams(port=8001, host="localhost")
    #        )
    #    ],
)
