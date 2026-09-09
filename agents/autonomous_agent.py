"""Autonomous Agent - Performs tasks like web scraping and data processing"""
import requests
from bs4 import BeautifulSoup
from llm_client import LLMClient
from typing import List, Dict, Any
import json

class AutonomousAgent:
    """Autonomous agent that can perform various tasks"""
    
    def __init__(self, provider: str = None):
        self.llm = LLMClient(provider)
        self.task_log = []
    
    def scrape_webpage(self, url: str) -> Dict[str, Any]:
        """Scrape content from a webpage"""
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract basic information
            title = soup.title.string if soup.title else "No title"
            text = soup.get_text()
            links = [a.get('href') for a in soup.find_all('a') if a.get('href')]
            
            task = {
                "task": "scrape_webpage",
                "url": url,
                "status": "success",
                "data": {
                    "title": title,
                    "text_length": len(text),
                    "links_found": len(links),
                    "preview": text[:500]
                }
            }
            self.task_log.append(task)
            
            return task["data"]
        
        except Exception as e:
            task = {
                "task": "scrape_webpage",
                "url": url,
                "status": "error",
                "error": str(e)
            }
            self.task_log.append(task)
            return {"error": str(e)}
    
    def process_data(self, data: List[Any], instruction: str) -> str:
        """Process data using AI interpretation of instructions"""
        system_message = "You are a data processing expert. Process the data according to the given instructions."
        
        prompt = f"""Data to process:
{json.dumps(data, indent=2)}

Instructions: {instruction}

Please process this data and provide results."""
        
        response = self.llm.generate(prompt, system_message)
        
        task = {
            "task": "process_data",
            "instruction": instruction,
            "status": "success",
            "result": response
        }
        self.task_log.append(task)
        
        return response
    
    def analyze_data(self, data: List[Dict[str, Any]]) -> str:
        """Analyze data and provide insights"""
        system_message = "You are a data analyst. Provide detailed analysis and insights."
        
        prompt = f"""Analyze this data and provide insights:
{json.dumps(data, indent=2)}"""
        
        response = self.llm.generate(prompt, system_message)
        
        task = {
            "task": "analyze_data",
            "status": "success",
            "result": response
        }
        self.task_log.append(task)
        
        return response
    
    def research_topic(self, topic: str) -> str:
        """Research a topic and provide comprehensive information"""
        system_message = """You are a research expert. Provide comprehensive, well-structured information.
Include:
1. Overview
2. Key points
3. Recent developments
4. Future outlook
5. Relevant resources"""
        
        prompt = f"Research and provide detailed information about: {topic}"
        
        response = self.llm.generate(prompt, system_message)
        
        task = {
            "task": "research_topic",
            "topic": topic,
            "status": "success",
            "result": response
        }
        self.task_log.append(task)
        
        return response
    
    def compare_items(self, items: List[str], criteria: List[str] = None) -> str:
        """Compare multiple items based on criteria"""
        system_message = "You are a comparison expert. Provide detailed, unbiased comparisons."
        
        criteria_text = f"Criteria: {', '.join(criteria)}" if criteria else ""
        
        prompt = f"""Compare these items:
{', '.join(items)}

{criteria_text}

Provide a detailed comparison table and analysis."""
        
        response = self.llm.generate(prompt, system_message)
        
        task = {
            "task": "compare_items",
            "items": items,
            "status": "success",
            "result": response
        }
        self.task_log.append(task)
        
        return response
    
    def get_task_log(self) -> List[Dict[str, Any]]:
        """Get log of all performed tasks"""
        return self.task_log
    
    def clear_task_log(self):
        """Clear task log"""
        self.task_log = []
