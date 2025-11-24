import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import time
import requests

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio, language = 'en-in')
            print(f"User said:{command}\n")
        except Exception as e:
            print(e)
            print("Say that again please...")
            return "None"
        return command.lower()