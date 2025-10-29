def chatbot():
    print("Hello! I’m PyBot 🤖. Type 'bye' to exit.")
    while True:
        user = input("You: ").lower()
        if "hello" in user:
            print("PyBot: Hi there!")
        elif "how are you" in user:
            print("PyBot: I’m doing great! What about you?")
        elif "bye" in user:
            print("PyBot: Goodbye! 👋")
            break
        else:
            print("PyBot: Sorry, I didn’t understand that.")

chatbot()
