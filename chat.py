from datetime import datetime

def respond(user_message):
    text = user_message.strip().lower()
    intents = [
        (lambda t: any(greet in t for greet in ["hello", "hi", "hey"]), "Hi there! 👋"),
        (lambda t: "how are you" in t, "I'm doing great! What about you? 😊"),
        (lambda t: "your name" in t or "who are you" in t, "I'm PyBot 🤖, your friendly terminal assistant."),
        (lambda t: "time" in t, f"The current time is {datetime.now().strftime('%H:%M:%S')} ⏰"),
        (lambda t: "date" in t, f"Today's date is {datetime.now().strftime('%Y-%m-%d')} 📅"),
        (lambda t: "thank" in t, "You're welcome! 🙌"),
        (lambda t: "joke" in t, "Why do programmers prefer dark mode? Because light attracts bugs! 🐛"),
        (lambda t: t in ["help", "?"], "Try: hello, how are you, time, date, joke, bye"),
    ]

    for matcher, reply in intents:
        if matcher(text):
            return reply
    return "Sorry, I didn't understand that. Type 'help' for options." 

def chatbot():
    print("Hello! I'm PyBot 🤖. Type 'bye' to exit.")
    while True:
        user = input("You: ")
        if user.strip().lower() == "bye":
            print("PyBot: Goodbye! 👋")
            break
        print("PyBot:", respond(user))

chatbot()
