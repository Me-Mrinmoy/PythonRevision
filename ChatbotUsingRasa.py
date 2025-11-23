import nltk
from nltk.chat.util import Chat, reflections
import spacy
import sympy as sp
from datetime import datetime

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Define patterns and responses
pairs = [
    (r'Hi|Hello|Hey', ['Hello! How can I assist you today?']),
    (r'What is your name?', ['I am a chatbot created with NLTK and spaCy.']),
    (r'Goodbye|Bye', ['Goodbye! Have a great day!']),
    (r'How are you?', ['I am just a computer program, but I am doing well! How can I assist you?']),
    (r'What can you do?', ['I can answer simple questions, provide information, solve mathematical operations, and tell you the current time. Just ask me anything!']),
    (r'Tell me about (.*)', ['I can provide information on various topics. Can you be more specific about what you want to know?']),
    (r'Can you help me with (.*)', ['Sure! What specifically do you need help with regarding "{}"?']),
    (r'What is (.*)', ['I can provide information about {}. Can you give me more details?']),
    (r'Where is (.*)', ['I can provide information about {}. Could you specify what exactly you are looking for?']),
    (r'How do I (.*)', ['To {} you should follow these steps: ...']),
    (r'I need help with (.*)', ['I can assist with {}. Please provide more details.']),
    (r'What are your capabilities?', ['I can provide information, assist with general queries, solve mathematical problems, and tell you the current time. Let me know what you need!']),
    (r'I am looking for (.*)', ['I can help with {}. Could you provide more details?']),
    (r'What time is it?', ['Let me check the current time for you.']),
    (r'Who created you?', ['I was created using NLTK and spaCy.']),
    # Additional patterns
    (r'Where can I find (.*)', ['I can help with {}. Could you provide more details about what you are looking for?']),
    (r'What is the capital of (.*)', ['The capital of {} is not something I know off the top of my head, but you can check online for the most accurate information.']),
    (r'What is the weather like in (.*)', ['I cannot provide real-time weather information, but you can check a weather website or app for current conditions in {}.']),
    (r'How old is (.*)', ['I do not have the age of {}, but you can look it up online for accurate information.']),
    (r'Can you tell me a joke?', ['Why don’t scientists trust atoms? Because they make up everything!']),
    (r'What is (.*) in programming?', ['{} in programming typically refers to a concept or feature in coding. Could you provide more details about what you want to know?']),
    (r'What does (.*) mean?', ['The meaning of {} depends on the context. Could you please provide more details or specify the context?']),
    (r'Can you help me with my (.*)', ['I can help with {}. Please provide more details on what you need assistance with.']),
    (r'What is your favorite (.*)?', ['As a chatbot, I don’t have personal preferences, but I can provide information about {}.']),
    (r'What is the latest news?', ['I do not have real-time news updates, but you can check news websites for the latest information.']),
    (r'What are some interesting facts about (.*)', ['Here are some interesting facts about {}: ...']),
    # Mathematical operations
    (r'Calculate (.*)', ['Let me calculate that for you: {}']),
]

# Create a chatbot
chatbot = Chat(pairs, reflections)

def get_spacy_entities(text):
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]

def evaluate_expression(expression):
    try:
        result = sp.sympify(expression)
        return result
    except Exception as e:
        return f"Error in calculation: {str(e)}"

def get_current_time():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

def main():
    print("Hello! I'm your chatbot. Type 'Bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye', 'goodbye']:
            print("Chatbot: Goodbye! Have a great day!")
            break

        # Check if user input matches a time query
        if "what time is it" in user_input.lower():
            response = get_current_time()
        elif "calculate" in user_input.lower():
            expression = user_input.lower().replace("calculate", "").strip()
            response = evaluate_expression(expression)
        else:
            response = chatbot.respond(user_input)
        
        entities = get_spacy_entities(user_input)
        if not response:
            response = "I'm not sure how to respond to that."

        print(f"Chatbot: {response}")
        print(f"Entities detected: {entities}")

if __name__ == "__main__":
    main()
