# Study Assistant - Multi-Agent Learning System

A sophisticated multi-agent AI system designed to provide personalized, intelligent study assistance using Google's Gemini 2.0 Flash model. The system employs multiple specialized agents that work together to deliver comprehensive learning support.

## 🎯 Overview

The Study Assistant is a multi-agent system that leverages the power of large language models to provide intelligent tutoring. It breaks down complex learning tasks across specialized agents, each designed to excel in their specific domain:

- **Chat Agent**: Natural conversation interface and task coordination
- **Content Agent**: Research and content simplification
- **Quiz Agent**: Dynamic quiz generation with quality assurance
- **Motivation Agent**: Emotional support and encouragement
- **Reflector Agent**: Quality verification of generated content

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                          ROOT AGENT                             │
│                  (Coordinator & Dispatcher)                     │
│                    Model: Gemini 2.0 Flash                      │
└───────────────────┬─────────────────────────────────────────────┘
                    │
        ┌───────────┴───────────┐
        │                       │
        ▼                       ▼
   ┌─────────────┐      ┌──────────────┐
   │ CHAT AGENT  │      │ MOTIVATION   │
   │ Coordinator │      │  AGENT       │
   └──────┬──────┘      └──────────────┘
          │
          │ Delegates tasks
          │
    ┌─────┴──────────────────────────────────┐
    │                                        │
    ▼                                        ▼
┌──────────────────┐            ┌────────────────────────┐
│ CONTENT AGENT    │            │ QUIZ AGENT             │
│ • Web Research   │            │ • Quiz Gen             │
│ • Summarization  │            │ • JSON Format          │
│ • Simplification │            │                        │
└────────┬─────────┘            └──────────┬─────────────┘
         │                                 |
         │ Provides Content                | Generate Quiz
         │                                 |
         |                                 | 
         │                                 |
         └─────────────────────────────────┘
                          │
    ┌─────────────────────▼────────────────────┐
    │         TOOLS LAYER                      │
    ├──────────────────────────────────────────┤
    │  • Google Search Grounding Tool          │
    └──────────────────────────────────────────┘
```

### Agent Interaction Flow

```
User Query
    │
    ▼
[ROOT AGENT]
    │
    ├─ Analyzes query intent
    │
    ▼
[CHAT AGENT]
    │
    ├─ Content Request? ──→ [CONTENT AGENT] ──→ Google Search ──→ Simplified Summary
    │
    ├─ Quiz Request? ──→ [QUIZ AGENT] ──→ Generate Quiz ──→ [REFLECTOR AGENT] ──→ Validate
    │
    ├─ Motivation Request? ──→ [MOTIVATION AGENT] ──→ Encouragement Response
    │
    └─ General Chat? ──→ Direct Response
```

## 📂 Project Structure

```
study_assistant/
├── README.md                                    # This file
├── multi_agent_system/
│   ├── __init__.py
│   ├── agent.py                            # Root agent configuration
│   ├── subagents/
│   │   ├── chat/
│   │   │   ├── __init__.py
│   │   │   ├── agent.py                        # Chat agent definition
│   │   │   └── prompt.py                       # Chat agent system prompt
│   │   ├── content/
│   │   │   ├── __init__.py
│   │   │   └── agent.py                        # Content research agent
│   │   ├── motivation/
│   │   │   ├── __init__.py
│   │   │   ├── agent.py                        # Motivation agent
│   │   │   └── prompt.py                       # Motivation prompt
│   │   └── quiz/
│   │       ├── __init__.py
│   │       ├── agent.py                        # Quiz generation agent
│   └── tools/
│       ├── __init__.py
│       └── search.py                           # Google Search integration
└── .env                                        # Environment configuration (not in repo)
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Google ADK (Agent Development Kit)
- Gemini 2.0 Flash API access
- Environment variables configured

### Installation

```bash
# Clone the repository
git clone https://github.com/goelsonali/study_assistant.git
cd study_assistant

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

### To run the agents
- go to root path study_assistant->
```
adk web
```
