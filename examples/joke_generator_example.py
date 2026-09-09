"""Example usage of Joke Generator Agent"""
from agents.joke_generator import JokeGenerator

def main():
    # Initialize the joke generator
    generator = JokeGenerator(provider="openai")
    
    print("\n" + "=" * 60)
    print("🎭 JOKE GENERATOR EXAMPLES")
    print("=" * 60)
    
    # Example 1: Random Joke
    print("\n1. Random Joke from Official API:")
    print("-" * 60)
    joke = generator.get_random_joke()
    print(generator.print_joke(joke))
    
    # Example 2: Dad Joke
    print("\n2. Dad Joke:")
    print("-" * 60)
    dad_joke = generator.get_dad_joke()
    print(generator.print_joke(dad_joke))
    
    # Example 3: Programming Joke
    print("\n3. Programming Joke:")
    print("-" * 60)
    prog_joke = generator.get_programming_joke()
    print(generator.print_joke(prog_joke))
    
    # Example 4: Category-Based Joke
    print("\n4. Knock-Knock Joke:")
    print("-" * 60)
    knock_knock = generator.get_joke_by_category("knock-knock")
    print(generator.print_joke(knock_knock))
    
    # Example 5: Custom Joke Generation
    print("\n5. AI-Generated Custom Joke (about Python):")
    print("-" * 60)
    custom = generator.generate_custom_joke("Python programming", style="funny")
    print(f"🤖 AI Generated Joke:\n{custom}\n")
    
    # Example 6: Joke Enhancement
    print("\n6. Enhanced Joke (using AI):")
    print("-" * 60)
    joke_to_enhance = "Why did the programmer quit his job? He didn't get arrays."
    enhanced = generator.enhance_joke(joke_to_enhance)
    print(f"Original: {joke_to_enhance}")
    print(f"\nEnhanced:\n{enhanced}\n")
    
    # Example 7: Joke with Rating
    print("\n7. Random Joke with Humor Rating:")
    print("-" * 60)
    rated_joke = generator.tell_joke_with_rating()
    if "error" not in rated_joke["joke"]:
        print(generator.print_joke(rated_joke["joke"]))
        print(f"Rating & Analysis:\n{rated_joke['rating']}\n")
    
    # Example 8: Multiple Jokes at Once
    print("\n8. Multiple Programming Jokes:")
    print("-" * 60)
    multiple = generator.get_multiple_jokes(count=3, category="programming")
    for i, j in enumerate(multiple, 1):
        print(f"\nJoke {i}:")
        print(generator.print_joke(j))
    
    # Show History
    print("\n" + "=" * 60)
    print("📜 Joke History Summary:")
    print("=" * 60)
    history = generator.get_joke_history()
    print(f"Total jokes fetched: {len(history)}")
    for i, joke in enumerate(history, 1):
        joke_type = joke.get('type', 'unknown')
        category = joke.get('category', '')
        category_str = f" ({category})" if category else ""
        print(f"{i}. {joke_type}{category_str}")

if __name__ == "__main__":
    main()
