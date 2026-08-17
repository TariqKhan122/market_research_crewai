🤖 AI Product Market Research Crew

A portfolio-ready multi-agent market research and product strategy system built with CrewAI, Groq/Qwen, and Tavily. The crew researches an AI product idea from multiple business perspectives and produces a consolidated business/investment report.


📌 Project Overview

This project demonstrates how a multi-agent AI workflow can turn a product idea into structured market intelligence and a business recommendation.

The current example analyzes this product concept:

An AI-powered tool that summarizes YouTube videos from a creator's channel and prepares the summaries for distribution across platforms such as LinkedIn, Instagram, Facebook, X, and WhatsApp.

The important distinction is that this project is not itself a social-media posting bot. Its current purpose is to research and evaluate that product idea, including its market opportunity, competitors, customers, product strategy, and business viability.

🎯 Problem

Validating an AI product idea normally requires research across several areas:

Market size and growth

Industry and technology trends

Competitor products and pricing

Customer segments and pain points

Product differentiation

Technical feasibility

Pricing and revenue models

Risks and go-to-market strategy

Doing this manually is time-consuming and requires switching between different research workflows.

💡 Solution

The system divides the research workflow into five specialized AI agents.

Each agent has a focused responsibility and receives context from the earlier stages. The workflow runs sequentially so that later agents can build on previous research instead of treating every task independently.

Agent Workflow

                    ┌─────────────────────┐
                    │    Product Idea     │
                    │   User Input        │
                    └──────────┬──────────┘
                               │
                               ▼
                  ┌────────────────────────┐
                  │ 1. Market Research     │
                  │ Market size, trends,   │
                  │ regulation, technology │
                  └──────────┬─────────────┘
                             │
                             ▼
                  ┌────────────────────────┐
                  │ 2. Competitive         │
                  │ Intelligence           │
                  │ Competitors, pricing,  │
                  │ positioning & gaps     │
                  └──────────┬─────────────┘
                             │
                             ▼
                  ┌────────────────────────┐
                  │ 3. Customer Insights   │
                  │ Segments, personas,    │
                  │ pain points & channels │
                  └──────────┬─────────────┘
                             │
                             ▼
                  ┌────────────────────────┐
                  │ 4. Product Strategy    │
                  │ MVP, differentiation,  │
                  │ feasibility & roadmap  │
                  └──────────┬─────────────┘
                             │
                             ▼
                  ┌────────────────────────┐
                  │ 5. Business Analyst    │
                  │ Pricing, GTM, risks,   │
                  │ financial model &      │
                  │ final recommendation  │
                  └──────────┬─────────────┘
                             │
                             ▼
                  ┌────────────────────────┐
                  │ reports/report.md      │
                  │ Consolidated Report    │
                  └────────────────────────┘

🧠 Multi-Agent Roles

Agent

Responsibility

Main Output

Market Research Specialist

Market size, growth, trends, regulations and technology readiness

Market opportunity analysis

Competitive Intelligence Analyst

Direct/indirect competitors, features, pricing and competitive gaps

Competitive landscape

Customer Insights Researcher

Customer segments, personas, pain points, journey and acquisition channels

Customer intelligence

Product Strategy Advisor

Product positioning, MVP priorities, differentiation and roadmap

Product strategy

Business Analyst & Report Synthesizer

Pricing, revenue model, GTM, resources, risks and final recommendation

Executive business report

🔄 Task Dependency / Context Flow

The workflow is intentionally sequential:

Market Research
      │
      ├──────────────► Competitive Intelligence
      │                         │
      └──────────────► Customer Insights
                                │
              ┌─────────────────┘
              ▼
       Product Strategy
              │
              ▼
       Business Analysis
              │
              ▼
       Final Report

The implementation passes previous task outputs as context to downstream tasks. The final business-analysis task receives the accumulated research and writes the result to:

reports/report.md

🛠️ Tech Stack

Python — application logic

CrewAI — multi-agent orchestration

Groq — LLM inference

Qwen — model used through CrewAI's LLM interface

LiteLLM — model integration layer used by CrewAI

Tavily — live web search

ScrapeWebsiteTool — website content extraction

SeleniumScrapingTool — browser-based scraping capability

python-dotenv — environment variable management

YAML — agent and task configuration

🔧 Tools Used by Agents

All five agents currently share the same research toolkit:

TavilySearchTool
        │
        ├── Live web search
        │
ScrapeWebsiteTool
        │
        ├── Website content extraction
        │
SeleniumScrapingTool
        │
        └── Browser-based scraping

The CrewAI implementation creates these tools once and supplies the toolkit to each specialized agent.

📂 Project Structure

market-research-crew/
│
├── src/
│   └── market_research_crew/
│       ├── config/
│       │   ├── agents.yaml
│       │   └── tasks.yaml
│       │
│       ├── crew.py
│       └── main.py
│
├── reports/
│   └── report.md
│
├── .env.example
├── pyproject.toml
├── README.md
└── ...

Your exact generated project structure may vary depending on the CrewAI project template/version.

⚙️ How It Works

1. Product idea is provided

The application passes a product_idea variable into the CrewAI workflow.

Example:

inputs = {
    "product_idea": "An AI-powered tool that summarizes YouTube videos..."
}

2. Market research agent investigates the opportunity

The first agent researches:

TAM / SAM / SOM

Market growth

Industry trends

AI adoption

Regulatory considerations

Technology readiness

3. Competitive intelligence agent builds the competitive picture

It researches:

Direct and indirect competitors

Product capabilities

Pricing

Target customers

Positioning

Strengths and weaknesses

Competitive gaps

4. Customer insights agent analyzes demand

It investigates:

Customer segments

Personas

Pain points

Customer journeys

Value proposition

Acquisition channels

Willingness-to-pay indicators

5. Product strategy agent converts research into product decisions

It develops:

Product vision

Positioning

MVP priorities

Differentiation

Technical feasibility

Development roadmap

Success metrics

6. Business analyst synthesizes everything

The final agent combines the preceding research into:

Executive summary

Pricing strategy

Revenue model

Go-to-market strategy

Resource requirements

Risk analysis

Investment thesis

Go / No-Go / Conditional recommendation

🚀 Getting Started

Prerequisites

Python >=3.10

A Groq API key

A Tavily API key

uv package manager

Installation

Install uv:

pip install uv

Install project dependencies:

uv sync

Environment Variables

Create .env from the example:

Copy-Item .env.example .env

Add:

GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key

Never commit .env or expose API keys in GitHub.

Run

From the project root:

uv run crewai run

The crew executes the five stages sequentially and generates:

reports/report.md

📊 Example Use Cases

Although the current example focuses on a YouTube-content product concept, the workflow can be adapted to research many AI/SaaS ideas, such as:

AI customer-support platforms

AI sales automation tools

AI developer tools

B2B SaaS products

Marketing automation platforms

Vertical AI products

Productivity applications

The product idea can be changed without redesigning the entire agent architecture.

🎓 What This Project Demonstrates

This project is designed to demonstrate practical understanding of:

Multi-agent system design

Agent specialization

Sequential task orchestration

Context passing between agents

LLM integration

Tool-augmented agents

Live web research

Prompt/configuration-driven agent behavior

Business-oriented AI workflows

Automated report generation

⚠️ Current Limitations

This project is a research and decision-support system, not a production financial or investment advisory platform.

Current limitations include:

Research quality depends on the quality and availability of web sources.

Generated market-size and financial estimates should be independently validated.

The current workflow uses a sequential process, so later stages wait for earlier stages.

The current example researches a proposed YouTube/social-content product; it does not download YouTube videos or publish content to social platforms.

The final report is generated by an LLM and should be reviewed before being used for real business decisions.

🔐 Security

API credentials are loaded through environment variables.

Required secrets:

GROQ_API_KEY
TAVILY_API_KEY

Do not hard-code credentials into Python files or commit .env to version control.

🚧 Future Improvements

Potential production-level extensions:

Add persistent research history

Add source URL tracking and automated citation validation

Add structured Pydantic output schema for the final business report

Add a Streamlit/FastAPI interface

Add human approval before final recommendations

Add report export to PDF

Parallelize independent first-stage research tasks where task dependencies allow

Add automated evaluation of research quality

Add caching to reduce repeated web/LLM calls

Add database-backed project and report history

Add observability/tracing for agent runs

Connect the researched YouTube-content concept to an actual content generation and social publishing pipeline

📈 Portfolio Value

This project goes beyond a single LLM prompt by demonstrating an orchestrated Agentic AI workflow where specialized agents perform different stages of a real business problem and share context before producing a final deliverable.

It is especially relevant to roles involving:

Agentic AI · Generative AI · AI Automation · LLM Applications · Python · Multi-Agent Systems · AI Product Development

👨‍💻 Author

Muhammad Tariq

AI/ML & Generative AI Enthusiast

⭐ If you find this project useful, consider starring the repository and exploring the implementation.

🔬 Engineering Improvements

The project uses a structured BusinessResearchReport Pydantic model for the final deliverable. This makes the output predictable and easier to validate, consume in an API, store in a database, or render in a frontend.

Structured Output

The final stage is expected to produce fields for:

Executive summary

Market opportunity

Competitive landscape

Customer insights

Product strategy

Business model

Risks and mitigations

Final recommendation

Context-Aware Orchestration

The crew deliberately remains sequential because downstream tasks depend on previous research. For example, the product-strategy stage receives market, competitor, and customer research before generating its recommendations.

A future optimization is to parallelize independent research stages first, then merge their outputs before downstream strategy tasks.

LLM Token Budget

The previous 1,000-token global response cap was too restrictive for a final business report. The implementation now uses a larger response budget while still keeping the limit bounded to control usage.

Note: the exact supported output length depends on the selected Groq model and service tier.

Recommended Next Engineering Step: Evidence Grounding

For a production-grade research system, the next major improvement should be source-aware outputs:

Claim → Source URL → Evidence Snippet → Agent Conclusion

This would allow the final report to distinguish sourced facts from AI-generated interpretation and make research claims easier to audit.

