import nltk          
import random
import pyttsx3      # this libray will all the chatbot to speak 
from nltk.chat.util import Chat, reflections

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# This are some  pre-Define pairs of patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hey there! How's it going?", "Hello! What's up?", "Hi! How can I help you today?"]
    ],
    [
        r"how are you ?",
        ["I'm doing great, thanks for asking! How about you?", "I'm good, how about yourself?"]
    ],
    [
        r"(.*) your name ?",
        ["I'm a friendly chatbot programmed Analystt developer. You can call me Anna.",]
    ],
    [
        r"what can you do ?",
        ["I can help you with various things! Just ask me anything.",]
    ],
    [
        r"who are you ?",
        ["I'm just your friendly neighborhood chatbot, here to chat with you!",]
    ],
    [
        r"(.*)",
        ["Hmm, that's interesting! Tell me more.", "I'm not sure I understand. Could you elaborate?", "I'm here to listen. Go ahead and share!",]
    ],
    [
        r"quit|exit|bye",
        ["Bye! Take care.", "Catch you later!"]
    ],
]

# Create a chatbot Function 
def simple_chatbot():
    print("Hey there! I'm Analystt. How can assist you ?")
    chatbot = Chat(pairs, reflections)
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print("Analystt:", response)
        # Speak the response
        engine.say(response)
        engine.runAndWait()
        # when  the user want to leave the appication 
        if user_input.lower() in ['quit', 'exit', 'bye']:
            break

if __name__ == "__main__":
    simple_chatbot()
