def chatbot():
    print("=== BASIC CHATBOT ===")
    print("Chatbot: Hello! I am a simple chatbot.")
    print("Type 'bye' to end the conversation.")

    while True:
        message = input("You: ").lower().strip()

        if message == "hello" or message == "hi":
            print("Chatbot: Hi! How can I help you?")
        elif message == "how are you":
            print("Chatbot: I'm fine, thanks! How are you?")
        elif message == "what is your name":
            print("Chatbot: I am CodeAlpha Bot.")
        elif message == "help":
            print("Chatbot: You can say hello, ask how I am, or say bye.")
        elif message == "bye":
            print("Chatbot: Goodbye! Have a nice day.")
            break
        else:
            print("Chatbot: Sorry, I don't understand that.")

chatbot()
