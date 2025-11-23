from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

def train_chatbot(chatbot):
    trainer = ChatterBotCorpusTrainer(chatbot)
    # Train the chatbot with English corpus data
    trainer.train('chatterbot.corpus.english')

def get_response(chatbot, user_input):
    response = chatbot.get_response(user_input)
    return response

def main():
    # Create a new chatbot instance
    chatbot = ChatBot('SimpleBot')
    
    # Train the chatbot
    train_chatbot(chatbot)
    
    print("Hello! I'm SimpleBot. How can I help you today?")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
        
        response = get_response(chatbot, user_input)
        print(f"SimpleBot: {response}")

if __name__ == "__main__":
    main()
