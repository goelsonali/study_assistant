import os
from google.adk.agents import LlmAgent

from dotenv import load_dotenv
from .subagents.chat.agent import chat_agent
from .subagents.motivation.agent import motivation_agent
from multi_agent_system.subagents.content.agent import content_agent
from multi_agent_system.subagents.quiz.agent import quiz_agent
#from google.adk.agents import agent_tool

# Load environment variables from .env file
load_dotenv()


root_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="StudyAssistant",
    instruction="An agent that coordinates the flow of information and delegates tasks to specialized " \
    "subagents in a study assistant system. When user wants to chat use the chat agent and when needs " \
    "some motivation to study or learn use the motivation agent.",
    sub_agents=[chat_agent, motivation_agent],
    #tools=[MCPToolset(
    #        connection_params=SseServerParams(port=8001, host="localhost")
    #        )
    #    ],
)




# Convert specialized agents into AgentTools
#chat_tool = agent_tool.AgentTool(agent=chat_agent)
#motivation_tool = agent_tool.AgentTool(agent=motivation_agent)
#content_tool = agent_tool.AgentTool(agent=content_agent)
#quiz_tool = agent_tool.AgentTool(agent=quiz_agent)
# Root agent now uses these agents as tools
#root_agent = LlmAgent(
#    model='gemini-2.0-flash',
#    name="StudyAssistant",
#    instruction=f"""Acts as a comprehensive Study Assistant...
#    Based on the user request, sequentially invoke the tools to gather all necessary information and present to the user...""",
#    tools=[chat_tool, motivation_tool, content_tool, quiz_tool] # The root agent can use these tools
#)