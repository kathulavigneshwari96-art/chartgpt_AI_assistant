# Talk to Machines: Build AI Assistant with ChatGPT
# Internshala Project - MOCK IMPLEMENTATION (No API billing required)

print("AI Assistant is running (type 'exit' to stop)")

# Predefined responses (simulate ChatGPT)
mock_responses = {
    "what is machine learning?": 
        "Machine learning is a branch of artificial intelligence that allows systems to learn from data and improve automatically without explicit programming.",

    "what is artificial intelligence?":
        "Artificial Intelligence refers to the simulation of human intelligence in machines that are programmed to think and learn.",

    "who invented chatgpt?":
        "ChatGPT was developed by OpenAI as a conversational artificial intelligence model.",

    "what are applications of ai?":
        "AI is used in healthcare, self-driving cars, virtual assistants, recommendation systems, and customer support."
}

while True:
    user_input = input("You: ").lower()

    if user_input in ["exit", "quit"]:
        print("Bot: Goodbye!")
        break

    # Fetch mock response
    response = mock_responses.get(
        user_input,
        "I'm an AI assistant. I can answer questions related to AI, machine learning, and technology."
    )

    print("Bot:", response)