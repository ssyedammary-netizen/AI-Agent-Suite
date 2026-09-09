"""
Main entry point for AI Agent Suite
Demonstrates all agents in one place
"""

from agents.coding_assistant import CodingAssistant
from agents.chatbot import ChatBot
from agents.autonomous_agent import AutonomousAgent
from agents.specialized_agent import SpecializedAgent

def print_menu():
    """Display the main menu"""
    print("\n" + "=" * 60)
    print("🤖 AI AGENT SUITE - MAIN MENU")
    print("=" * 60)
    print("1. Coding Assistant")
    print("2. Chatbot")
    print("3. Autonomous Agent")
    print("4. Specialized Domain Agent")
    print("5. Exit")
    print("=" * 60)

def coding_assistant_demo():
    """Run coding assistant demo"""
    print("\n📝 CODING ASSISTANT DEMO")
    print("-" * 60)
    
    assistant = CodingAssistant(provider="openai")
    
    print("\nWhat would you like the assistant to do?")
    print("1. Generate Code")
    print("2. Debug Code")
    print("3. Optimize Code")
    print("4. Explain Code")
    print("5. Back to Main Menu")
    
    choice = input("\nEnter your choice (1-5): ").strip()
    
    if choice == "1":
        requirements = input("Describe what code you need: ")
        language = input("Programming language (default: python): ") or "python"
        print("\nGenerating code...")
        result = assistant.generate_code(requirements, language)
        print(f"\n{result}")
    
    elif choice == "2":
        code = input("Paste your code:\n")
        error = input("Paste the error message:\n")
        print("\nDebugging...")
        result = assistant.debug_code(code, error)
        print(f"\n{result}")
    
    elif choice == "3":
        code = input("Paste your code to optimize:\n")
        print("\nOptimizing...")
        result = assistant.optimize_code(code)
        print(f"\n{result}")
    
    elif choice == "4":
        code = input("Paste your code to explain:\n")
        print("\nExplaining...")
        result = assistant.explain_code(code)
        print(f"\n{result}")

def chatbot_demo():
    """Run chatbot demo"""
    print("\n💬 CHATBOT DEMO")
    print("-" * 60)
    
    personality = input("Choose personality (helpful/professional/creative/technical): ").lower()
    if personality not in ["helpful", "professional", "creative", "technical"]:
        personality = "helpful"
    
    chatbot = ChatBot(provider="openai", personality=personality)
    print(f"\n🤖 Chatbot initialized with '{personality}' personality")
    print("Type 'quit' to exit, 'summary' for conversation summary\n")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == "quit":
            break
        elif user_input.lower() == "summary":
            summary = chatbot.get_conversation_summary()
            print(f"Summary: {summary}\n")
        elif user_input:
            response = chatbot.chat(user_input)
            print(f"Bot: {response}\n")

def autonomous_agent_demo():
    """Run autonomous agent demo"""
    print("\n🤖 AUTONOMOUS AGENT DEMO")
    print("-" * 60)
    
    agent = AutonomousAgent(provider="openai")
    
    print("\nWhat would you like the agent to do?")
    print("1. Research a Topic")
    print("2. Process Data")
    print("3. Compare Items")
    print("4. Back to Main Menu")
    
    choice = input("\nEnter your choice (1-4): ").strip()
    
    if choice == "1":
        topic = input("What topic would you like researched? ")
        print("\nResearching...")
        result = agent.research_topic(topic)
        print(f"\n{result}")
    
    elif choice == "2":
        print("Enter data as comma-separated values (e.g., value1,value2,value3)")
        data_input = input("Enter data: ")
        instruction = input("What should I do with this data? ")
        data = data_input.split(",")
        print("\nProcessing...")
        result = agent.process_data(data, instruction)
        print(f"\n{result}")
    
    elif choice == "3":
        items = input("Enter items to compare (comma-separated): ").split(",")
        print("\nComparing...")
        result = agent.compare_items(items)
        print(f"\n{result}")

def specialized_agent_demo():
    """Run specialized agent demo"""
    print("\n🎯 SPECIALIZED DOMAIN AGENT DEMO")
    print("-" * 60)
    
    print("\nSelect a domain:")
    print("1. Customer Support")
    print("2. Content Generation")
    print("3. Marketing")
    print("4. Legal")
    print("5. Medical")
    print("6. Financial")
    print("7. Back to Main Menu")
    
    choice = input("\nEnter your choice (1-7): ").strip()
    
    domains = {
        "1": "customer_support",
        "2": "content_generation",
        "3": "marketing",
        "4": "legal",
        "5": "medical",
        "6": "financial"
    }
    
    if choice in domains:
        domain = domains[choice]
        agent = SpecializedAgent(domain=domain, provider="openai")
        
        query = input("Enter your query/request: ")
        print(f"\nProcessing with {domain} agent...")
        
        result = agent.query_domain(query)
        print(f"\n{result}")

def main():
    """Main application loop"""
    print("\n" + "🚀 " * 20)
    print("WELCOME TO AI AGENT SUITE")
    print("🚀 " * 20)
    
    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            coding_assistant_demo()
        elif choice == "2":
            chatbot_demo()
        elif choice == "3":
            autonomous_agent_demo()
        elif choice == "4":
            specialized_agent_demo()
        elif choice == "5":
            print("\n👋 Thank you for using AI Agent Suite!")
            print("Goodbye!\n")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
