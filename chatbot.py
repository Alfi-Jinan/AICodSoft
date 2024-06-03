def chatbot_response(user_input):
    user_input = user_input.lower()  

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm here to help you!"
    elif "your name" in user_input:
        return "I'm a simple chatbot created to assist you."
    elif "help" in user_input:
        return "Sure, I can help! What do you need assistance with?"
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

def chat():
    print("Chatbot: Hello! I am a chatbot. Type 'bye' or 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    chat()
