import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import time
import requests
from bs4 import BeautifulSoup

def speak(text):
    engine = pyttsx3.init()

    # Set voice properties to sound deeper (Iron Man style)
    voices = engine.getProperty('voices')
    for voice in voices:
        if "male" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break

    engine.setProperty('rate', 150)  # Speed of speech (adjust to sound robotic)
    
    # engine.setProperty('volume', 1.0)  # Max volume (default is 1.0)
    
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio, language='en-in')
            print(f"User said: {command}\n")
        except Exception as e:
            print(e)
            print("Say that again please...")
            return "None"
    return command.lower()

def get_youtube_video(query):
    search_url = f"https://www.youtube.com/results?search_query={query}"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for video in soup.find_all('a', href=True):
        if '/watch?v=' in video['href']:
            return f"https://www.youtube.com{video['href']}"
    return None

def execute_command(command):
    if 'open' in command:
        site = command.replace('open ', '')
        speak(f"Opening {site}")
        if '.' not in site:
            site = f"{site}.com"
        webbrowser.open(f"https://www.{site}")
    elif 'search youtube for' in command:
        query = command.replace('search youtube for ', '')
        speak(f"Searching YouTube for {query}")
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
    elif 'search google for' in command:
        query = command.replace('search google for ', '')
        speak(f"Searching Google for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")
    elif 'play music' in command:
        speak("Playing music")
        music_dir = 'path_to_your_music_directory'
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[0]))
    elif 'show picture of' in command:
        query = command.replace('show picture of ', '')
        speak(f"Showing pictures of {query}")
        webbrowser.open(f"https://www.google.com/search?tbm=isch&q={query}")
    elif 'time' in command:
        from datetime import datetime
        strTime = datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {strTime}")
    elif 'tell me about' in command:
        query = command.replace('tell me about ', '')
        speak(f"Searching for information about {query}")
        webbrowser.open(f"https://en.wikipedia.org/wiki/{query}")
    elif 'play this music on youtube' in command:
        query = command.replace('play this music on youtube', '').strip()
        if query:
            speak(f"Playing {query} on YouTube")
            video_url = get_youtube_video(query)
            if video_url:
                webbrowser.open(video_url)
            else:
                speak("Sorry, I couldn't find the video on YouTube.")
        else:
            speak("What music do you want to play on YouTube?")
            query = take_command()
            if query != "None":
                speak(f"Playing {query} on YouTube")
                video_url = get_youtube_video(query)
                if video_url:
                    webbrowser.open(video_url)
                else:
                    speak("Sorry I couldn't find the video on YouTube.")
    else:
        speak("Sorry, please repeat that again...")

if __name__ == "__main__":
    speak("Hi Sanchita, how many times you can fall in love?")
    while True:
        command = take_command()
        if command == "none":
            continue
        execute_command(command)
