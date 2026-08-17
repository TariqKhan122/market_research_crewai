# MarketResearchCrew Crew

Welcome to the MarketResearchCrew Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the project dependencies:

```bash
uv sync
```
### Customizing

This project uses a model hosted by **Groq**
key in the [Groq Console](https://console.groq.com/keys), then copy the example variables:

```powershell
Copy-Item .env.example .env
```

Add your keys to `.env`:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

`GROQ_API_KEY` is used for the Groq model. `TAVILY_API_KEY` is required because the crew
uses `TavilySearchTool` for live web search. Create the Tavily key at
[app.tavily.com](https://app.tavily.com/). The `.env` file is ignored by Git.

The model is configured as `groq/qwen/qwen3.6-27b` in `crew.py`. This is passed through
CrewAI's LiteLLM integration, so no separate Groq SDK is needed. The project
installs CrewAI's `litellm` extra automatically.

The Groq on-demand tier has token-per-minute limits. This project caps each
model response at 1,000 tokens to keep requests within that limit. If Groq
returns a `429` error, wait for the reset time shown in the error and run the
crew again, or upgrade the Groq service tier for larger reports.

- Modify `src/market_research_crew/config/agents.yaml` to define your agents
- Modify `src/market_research_crew/config/tasks.yaml` to define your tasks
- Modify `src/market_research_crew/crew.py` to add your own logic, tools and specific args
- Modify `src/market_research_crew/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
uv run crewai run
```

This command initializes the market-research-crew Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The market-research-crew Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.
