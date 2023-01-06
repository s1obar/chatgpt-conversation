from revChatGPT.ChatGPT import Chatbot
import json

from record import SpeechRecognizer
from speak import Speak


config = json.load(open("config.json"))
chatbot = Chatbot(config, conversation_id=None)
chatbot.reset_chat()
chatbot.refresh_session()

listen = SpeechRecognizer()

speak = Speak()

print("Say something!")
while True:
    message = listen.listen()
    print(f"Recognized: {message}")
    resp = chatbot.ask(message, conversation_id=None, parent_id=None)
    response = resp['message']
    print(f"Response: {response}")
    speak.speak(response)
