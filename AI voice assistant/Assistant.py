from datetime import datetime
from email.mime import audio
from fileinput import close
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')  # using pyttsx3 to form  an obj of api "sapi5"
voices = engine.getProperty('voice')
# print(voices)
engine.setProperty('voice', voices[0])  # setting voice choice

# function to perform speaking


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def Wish():
    hour = int(datetime.now().hour)
    if hour > 0 and hour < 12:
        speak("Good Mourning!!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!!")
    else:
        speak("Good Evening")

    speak("I am your personal assistant and how may i help u")

# function to take input in string form


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:  # using active microphone as input source
        print("Listening...")
        r.pause_threshold = 1  # pause required to sense end of a statement
        audio = r.listen(source)

    try:
        print("Recogniting...")
        # using google engine for recognition
        query = r.recognize_google(audio, language="en-in")
        print(f"User said : {query}\n")

    except Exception as e:
        # print(e)
        print("pardon")
        return "none"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('anirudhyadavlm10@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    # speak("hello anirudh")
    Wish()
    while (True):
        query = takeCommand().lower()  # taking input in lower case

        # Logic for wiki search
        if 'wikipedia' in query:
            speak("Searching in wikipedia")
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentence=2)
            print(results)
            speak(results)

        # logic for opening various site
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

    # playing music stored in given directry
        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'  # directory location
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

    # current time function
        elif 'the time' in query:
            strTime = datetime.now().strftime("%H:%M:%S")
            speak(strTime)

    # basic email send logic
        elif 'email to anirudh' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "anirudhyadavlm10@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
               # print(e)
                speak(" I am not able to send this email")

        elif 'shut down' in query:
            speak("shutting down ")
            speak("bye !! and have a nice day")
            close()
