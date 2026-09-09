"""Random Joke Generator Agent - Fetches jokes from external APIs"""
import requests
from llm_client import LLMClient
from typing import Dict, List, Any

class JokeGenerator:
    """Generates random jokes using external APIs and AI enhancement"""
    
    def __init__(self, provider: str = None):
        self.llm = LLMClient(provider)
        self.joke_history = []
        self.base_apis = {
            "official": "https://official-joke-api.appspot.com",
            "random": "https://v2.jokeapi.dev/joke",
            "dad_jokes": "https://icanhazdadjoke.com"
        }
    
    def get_random_joke(self) -> Dict[str, Any]:
        """Fetch a random joke from Official Joke API"""
        try:
            url = f"{self.base_apis['official']}/random_joke"
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            
            joke_data = response.json()
            joke = {
                "type": "official",
                "setup": joke_data.get("setup", ""),
                "punchline": joke_data.get("punchline", ""),
                "full_joke": f"{joke_data.get('setup', '')} {joke_data.get('punchline', '')}",
                "id": joke_data.get("id")
            }
            self.joke_history.append(joke)
            return joke
        
        except Exception as e:
            return {"error": str(e), "type": "official"}
    
    def get_joke_by_category(self, category: str = "general") -> Dict[str, Any]:
        """Fetch a joke by category using JokeAPI"""
        try:
            categories = ["general", "knock-knock", "programming", "miscellaneous", "spooky", "christmas"]
            
            if category.lower() not in categories:
                category = "general"
            
            url = f"{self.base_apis['random']}/{category}"
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            
            joke_data = response.json()
            
            if joke_data.get("type") == "twopart":
                joke = {
                    "type": "category",
                    "category": category,
                    "setup": joke_data.get("setup", ""),
                    "delivery": joke_data.get("delivery", ""),
                    "full_joke": f"{joke_data.get('setup', '')} {joke_data.get('delivery', '')}",
                    "id": joke_data.get("id")
                }
            else:
                joke = {
                    "type": "category",
                    "category": category,
                    "setup": joke_data.get("joke", ""),
                    "delivery": "",
                    "full_joke": joke_data.get("joke", ""),
                    "id": joke_data.get("id")
                }
            
            self.joke_history.append(joke)
            return joke
        
        except Exception as e:
            return {"error": str(e), "type": "category", "category": category}
    
    def get_dad_joke(self) -> Dict[str, Any]:
        """Fetch a random dad joke"""
        try:
            url = self.base_apis['dad_jokes']
            headers = {'Accept': 'application/json'}
            response = requests.get(url, headers=headers, timeout=5)
            response.raise_for_status()
            
            joke_data = response.json()
            joke = {
                "type": "dad_joke",
                "setup": "",
                "punchline": joke_data.get("joke", ""),
                "full_joke": joke_data.get("joke", "")
            }
            self.joke_history.append(joke)
            return joke
        
        except Exception as e:
            return {"error": str(e), "type": "dad_joke"}
    
    def get_programming_joke(self) -> Dict[str, Any]:
        """Fetch a programming-related joke"""
        try:
            url = f"{self.base_apis['random']}/programming"
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            
            joke_data = response.json()
            
            if joke_data.get("type") == "twopart":
                joke = {
                    "type": "programming",
                    "setup": joke_data.get("setup", ""),
                    "delivery": joke_data.get("delivery", ""),
                    "full_joke": f"{joke_data.get('setup', '')} {joke_data.get('delivery', '')}",
                    "id": joke_data.get("id")
                }
            else:
                joke = {
                    "type": "programming",
                    "setup": joke_data.get("joke", ""),
                    "delivery": "",
                    "full_joke": joke_data.get("joke", ""),
                    "id": joke_data.get("id")
                }
            
            self.joke_history.append(joke)
            return joke
        
        except Exception as e:
            return {"error": str(e), "type": "programming"}
    
    def enhance_joke(self, joke: str) -> str:
        """Use AI to enhance or expand a joke"""
        system_message = """You are a comedy writer. 
Take a joke and enhance it by:
1. Adding more details or context
2. Making the punchline funnier
3. Creating a variation of the joke
Keep it clean and clever."""
        
        prompt = f"Enhance this joke: {joke}"
        
        enhanced = self.llm.generate(prompt, system_message)
        return enhanced
    
    def generate_custom_joke(self, topic: str, style: str = "funny") -> str:
        """Generate a custom joke about a topic using AI"""
        system_message = f"""You are a professional comedy writer.
Generate a {style} joke about the given topic.
Make it clever, witty, and memorable.
Include a setup and punchline."""
        
        prompt = f"Write a {style} joke about: {topic}"
        
        joke = self.llm.generate(prompt, system_message)
        return joke
    
    def tell_joke_with_rating(self) -> Dict[str, Any]:
        """Get a joke and provide a humor rating"""
        joke = self.get_random_joke()
        
        if "error" in joke:
            return joke
        
        # Use AI to rate the humor
        system_message = """You are a comedy critic.
Rate a joke's humor on a scale of 1-10 and explain why.
Be fair and constructive."""
        
        prompt = f"""Rate this joke's humor:
Setup: {joke.get('setup', '')}
Punchline: {joke.get('punchline', '')}

Provide a rating (1-10) and explanation."""
        
        rating = self.llm.generate(prompt, system_message)
        
        return {
            "joke": joke,
            "rating": rating
        }
    
    def get_multiple_jokes(self, count: int = 5, category: str = None) -> List[Dict[str, Any]]:
        """Get multiple jokes"""
        jokes = []
        for _ in range(count):
            if category:
                joke = self.get_joke_by_category(category)
            else:
                # Randomly pick from different sources
                import random
                choice = random.choice([1, 2, 3])
                if choice == 1:
                    joke = self.get_random_joke()
                elif choice == 2:
                    joke = self.get_dad_joke()
                else:
                    joke = self.get_joke_by_category()
            
            jokes.append(joke)
        
        return jokes
    
    def get_joke_history(self) -> List[Dict[str, Any]]:
        """Get all fetched jokes"""
        return self.joke_history
    
    def clear_history(self):
        """Clear joke history"""
        self.joke_history = []
    
    def print_joke(self, joke: Dict[str, Any]) -> str:
        """Pretty print a joke"""
        if "error" in joke:
            return f"❌ Error: {joke['error']}"
        
        output = []
        output.append("=" * 60)
        output.append(f"📝 Type: {joke.get('type', 'unknown')}")
        
        if joke.get('setup'):
            output.append(f"\n😊 Setup: {joke['setup']}")
        
        if joke.get('delivery'):
            output.append(f"\n😂 Delivery: {joke['delivery']}")
        elif joke.get('punchline'):
            output.append(f"\n😂 Punchline: {joke['punchline']}")
        
        if joke.get('category'):
            output.append(f"\n📂 Category: {joke['category']}")
        
        output.append("\n" + "=" * 60)
        
        return "\n".join(output)
