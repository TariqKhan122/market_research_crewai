import os

from crewai import Agent, Crew, LLM, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai_tools import ScrapeWebsiteTool, SeleniumScrapingTool, TavilySearchTool
from dotenv import load_dotenv

load_dotenv()


def get_groq_llm() -> LLM:
    """Create the Groq-hosted LLM used by every agent in this crew."""
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError(
            "GROQ_API_KEY is missing. Add it to your .env file. "
            "See .env.example for the required variables."
        )

    return LLM(
        # Qwen supports CrewAI's local tool-calling loop without invoking
        # Groq's server-side built-in tools.
        model="groq/qwen/qwen3.6-27b",
        api_key=api_key,
        temperature=0.2,
        # Groq's on-demand tier allows 8,000 tokens/minute for this model.
        # A bounded response prevents a single CrewAI request from exhausting it.
        max_tokens=1000,
    )

# create the tools for the agent
web_search_tool = TavilySearchTool(search_depth="basic", max_results=5)
web_scraping_tool = ScrapeWebsiteTool()
selenium_scraping_tool = SeleniumScrapingTool()

toolkit = [web_search_tool, web_scraping_tool, selenium_scraping_tool]

# define the crew class
@CrewBase
class MarketResearchCrew():
    """MarketResearchCrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # provide the path for configuration files
    agents_config = "config/agents.yaml" 
    tasks_config = "config/tasks.yaml"
    
    # ================ Agents ========================
    
    @agent
    def market_research_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config["market_research_specialist"],
            tools=toolkit,
            llm=get_groq_llm(),
        )

    @agent
    def competitive_intelligence_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["competitive_intelligence_analyst"],
            tools=toolkit,
            llm=get_groq_llm(),
        )
        
    @agent
    def customer_insights_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["customer_insights_researcher"],
            tools=toolkit,
            llm=get_groq_llm(),
        )
        
    @agent
    def product_strategy_advisor(self) -> Agent:
        return Agent(
            config=self.agents_config["product_strategy_advisor"],
            tools=toolkit,
            llm=get_groq_llm(),
        )
        
    @agent
    def business_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["business_analyst"],
            tools=toolkit,
            llm=get_groq_llm(),
        )
        
    # ================ Tasks ======================
    
    @task
    def market_research_task(self) -> Task:
        return Task(
            config=self.tasks_config["market_research_task"]
        )
        
    @task
    def competitive_intelligence_task(self) -> Task:
        return Task(
            config=self.tasks_config["competitive_intelligence_task"],
            context=[self.market_research_task()]
        )
        
    @task
    def customer_insights_task(self) -> Task:
        return Task(
            config=self.tasks_config["customer_insights_task"],
            context=[self.market_research_task(),
                     self.competitive_intelligence_task()]
        )
        
    @task
    def product_strategy_task(self) -> Task:
        return Task(
            config=self.tasks_config["product_strategy_task"],
            context=[self.market_research_task(),
                     self.competitive_intelligence_task(),
                     self.customer_insights_task()]
        )
        
    @task
    def business_analyst_task(self) -> Task:
        return Task(
            config=self.tasks_config["business_analyst_task"],
            context=[self.market_research_task(),
                     self.competitive_intelligence_task(),
                     self.customer_insights_task(),
                     self.product_strategy_task()],
            output_file="reports/report.md"
        )
        
    # ================= Crew ===========================
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential
        )
