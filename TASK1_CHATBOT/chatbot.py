def chatbot():
  print("Welcome to SimpleChatBot!")
  print("Type 'bye' to exit.")

  while True:
    user_input = input("You: ").lower()

    if "hello" in user_input or "hi" in user_input:
        print("Bot: Hello! How can I help you?")

    elif "how are you" in user_input:
        print("Bot: I'm doing great! Thanks for asking.")

    elif "your name" in user_input:
        print("Bot: My name is Bot.")

    elif "what can you do" in user_input:
        print("Bot: I can answer some basic questions and chat with you.")    

    elif "how old are you" in user_input:
        print("Bot: I'm just a chatbot, so I don't really have an age!")    

    elif "what is python" in user_input:
        print("Bot: Python is a popular programming language.")

    elif "help" in user_input:
        print("Bot: I can answer simple questions about Python.")

    elif "weather" in user_input:
        print("Bot: I cannot check live weather yet.")

    elif "thank you" in user_input:
        print("Bot: You're welcome!")

    elif "your favourite color" in user_input:
        print("Bot: My favourite color is blue.")  

    elif "bye" in user_input or "goodbye" in user_input:
        print("Bot: Goodbye! Have a great day!")
        break      

    else:
        print("Bot: Sorry, I don't understand that.")
chatbot()