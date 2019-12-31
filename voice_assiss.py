import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
from gtts import gTTS
import webbrowser
import os
import subprocess
from tkinter import *
from tkinter.ttk import *
root = Tk()
root.title("Voice Assistant")
root.geometry('1000x1000')
Button(root, text = 'Chatbot').pack(side='left')


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Hello ! I am Aasaan- your interactive help!. what do you want me to do?")

def get_audio():
    r = sr.Recognizer()
    r.energy_threshold = 4000
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print(e)
            print("Exception: " + str(e))

    return said
def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    r.energy_threshold = 4000
    with sr.Microphone() as source:
        print("Aasaan listening...")

        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Aasaan recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Once more please! ")

        return "None"
    return query

def note(query):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(query)

    subprocess.Popen([r"notepad.exe", file_name])


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia-")
            print(results)
            speak(results)

        elif 'youtube' in query:
            webbrowser.open("https://www.youtube.com/watch?v=")

        elif 'google' in query:
            webbrowser.open("google.com")

        elif 'ajtak' in query or 'news' in query:
            webbrowser.open("https://aajtak.intoday.in/livetv/")
        elif 'search for' in query:
            print("You asked : {}".format(query))
            url = 'https://www.google.co.in/search?q='
            search_url = url + query
            webbrowser.open(search_url)

        elif 'what is' in query or 'kya' in query or 'kyon' in query:

            print("You asked : {}".format(query))
            url = 'https://www.google.co.in/search?q='
            search_url = url + query
            webbrowser.open(search_url)

        elif 'who is' in query:

            print("You asked : {}".format(query))
            url = 'https://www.google.co.in/search?q='
            search_url = url + query
            webbrowser.open(search_url)

        elif 'what is' in query or 'why' in query or 'how ' in query:

            print("You said : {}".format(query))
            url = 'https://www.google.co.in/search?q='
            search_url = url + query
            webbrowser.open(search_url)

        elif 'play music' in query:
            music_dir = 'D:\machine learning\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'quit' in query or 'bye' in query:
            speak("Aasaan out! It was nice helping you. GoodBye")
            exit()

        elif 'note' in query:
             speak("What would you like me to write down? ")
             write_down = get_audio()
             note(write_down)
             speak("I've made a note of that.")

