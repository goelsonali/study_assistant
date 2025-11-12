## System Overview

### Mission Statement
Provide intelligent, personalized study assistance through a coordinated multi-agent system that leverages advanced LLMs to deliver specialized educational support across multiple domains.

### Core Architecture Principles

1. **Agent Specialization**: Each agent has a well-defined role and responsibility
2. **Hierarchical Coordination**: Root agent coordinates specialized subagents
3. **Task Delegation**: Intelligent routing of tasks to appropriate agents
4. **Tool Integration**: Agents leverage specialized tools for enhanced capabilities
5. **Scalability**: Easy to add new agents without modifying existing ones
6. **Maintainability**: Clear separation of concerns and responsibilities

### System Boundaries

```
┌─────────────────────────────────────────────────────────────┐
│                    Study Assistant System                    │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐ │
│  │         Multi-Agent Orchestration Layer                │ │
│  │  • Agent coordination                                  │ │
│  │  • Task routing                                       │ │
│  │  • Response aggregation                              │ │
│  └────────────────────────────────────────────────────────┘ │
│                           │                                  │
│  ┌────────────────────────┴────────────────────────────────┐ │
│  │         Specialized Agents Layer                       │ │
│  │  • Chat Agent (Coordinator)                           │ │
│  │  • Content Agent (Research)                           │ │
│  │  • Quiz Agent (Assessment)                            │ │
│  │  • Motivation Agent (Support)                         │ │
│  └────────────────────────────────────────────────────────┘ │
│                           │                                  │
│  ┌────────────────────────┴────────────────────────────────┐ │
│  │            Tools & External Services                   │ │
│  │  • Google Search API                                  │ │
│  │  • Google Gemini LLM                                  │ │
│  │  • Search Grounding Tool                             │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                              │
└─────────────────────────────────────────────────────────────┘

```

---

### Agents
**Responsibility**: Specialized task execution

#### Agent Taxonomy

```
Agents
├── LLM-only Agents
│   ├── Chat Agent (uses LLM only)
│   ├── Motivation Agent (uses LLM + role-based prompting)
│
└── Tool-using Agents
    ├── Content Agent (uses Google Search tool)
    └── Quiz Agent (uses structured output)
```
