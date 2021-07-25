import smtplib
from urllib.request import urlopen

import speech_recognition as sr
import pyaudio
import pyttsx3

import datetime
import wikipedia
import webbrowser
import os
import subprocess
import time
import pyjokes
import PyDictionary
import ctypes
from newspaper import Article

import json
import wolframalpha
import requests
import math

import random

import math_function
import ToDo

assistant = "Sophia"
user = "Human"
end = ["bye","goodbye","adios","exit","stop","close","quit","end", "shut down", "you may leave","shutdown"]
random_list = ["will you be my gf", "will you be my bf", "i love you"]
music = ["play music", "play song", "song", "music", "lift my mood"]

mailDir = {
    # Enter your email directory here to send the email
}

chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe %s"
#setting speech engine
#Sapi5 is microsoft tect to speech engine used for voice recognition

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')

#speak function converts text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()
def display(text):
    print(f"{assistant}:{text}\n")
    speak(text)
def isContain(txt, lst):
    for word in lst:
        if word in txt:
            return True
    return False



def wish():
    time = int(datetime.datetime.now().hour)
    if time>=0 and time<12:
        display("Hello, Good Morning!")
    elif time>= 12 and time <18:
        display("Hello, Good Afternoon!")
    else:
        display("Hello, Good Evening!")
    display("I am " + assistant + "." +" Your Voice Assistant!")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(f"{assistant}: Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print(f"{assistant}: Recognizing...")
            statement = r.recognize_google(audio,language='en-in')
            print(f"\n{user}:{statement}\n")
        except Exception as e:
            display("Pardon Me, Please say that again...")
            return "None"
        return statement

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    file = open("key.txt", "rt")
    password = file.read()
    file.close()
    server.login('your-email-id-here', 'your-password-here')
    server.sendmail('your-email-id-here', mailDir[to], content)
    server.close()

def work():
    print("Loading your AI personal assistant Sophia")
    wish()
    display("Tell me, What can I do for you?")
    while True:
        query = takeCommand().lower()
        if 'how are you' in query:
            display("I am fine, Thank you")
            display("How are you?")
        elif 'fine' in query or "good" in query:
            display("It's good to know that your fine")
        elif "morning" in query or "evening" in query or "afternoon" in query:
            display("A warm" + query)
            display(f"How are you {user}?")
        elif "what can you do" in query:
            display("I can assist you in your day to day activities.")

        elif "sophia" in query or "sofia" in query:
            wish()
            display(assistant + " in your service Mister")
        elif "change name" in query:
            display(f"What would you like to call me, {user} ")
            assistant = takeCommand()
            display("Thanks for naming me")
        elif "what's your name" in query or "What is your name" in query:
            speak("Yukta maned me")
            speak(assistant)
            print("Yukta named me", assistant)

        elif 'wikipedia' in query:
            display('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            display("According to Wikipedia")
            print(results)
            display(results)

        elif 'youtube' in query:
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            display("Here you go to Youtube\n")
            webbrowser.get(chrome_path).open("youtube.com")
        elif 'google' in query:
            speak("Here you go to Google\n")
            webbrowser.get(chrome_path).open("google.com")
        elif 'chrome' in query:
            display("Here you go to chrome\n")
            os.startfile(chrome_path)
        elif 'stack overflow' in query:
            display("Here you go to Stack Over flow. Keep Coding")
            webbrowser.get(chrome_path).open("stackoverflow.com")

        elif "joke" in query:
            display("Here you go...")
            joke = pyjokes.get_joke(language='en',category='all')
            display("\n" + joke)

        #math functions
        elif isContain(query,['factorial', 'log', 'value of', 'math', ' + ', ' - ', ' x ', 'multiply', 'divided by', 'binary',
                      'hexadecimal', 'octal', 'shift', 'sin ', 'cos ', 'tan ']):
            try:
                display('\nResult is: ' + math_function.perform(query))
            except Exception as e:
                return
            continue

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("To whom should I send the email?")
                to = takeCommand()
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email at the moment")

        elif "meaning" in query:
            dic = PyDictionary.PyDictionary()
            display("Say the word you wanna find meaning of")
            word = takeCommand()
            ans = dic.meaning(word)
            print(ans)
            for state in ans:
                print(ans[state])
                display("the meaning in " + state + " form is" + str(ans[state]))


        elif any(ext in query for ext in music):
            speak("Enjoy the music!")
            music_dir = r"C:\Users\ASUS\Music\Playlists"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, random.choice(songs)))
        elif any(ext in query for ext in random_list):
            display("I am not sure about that! May be you should give me some time")
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            display(f"The time is {strTime}")
        elif 'open code' in query:
            display("Opening your favorite I D E")
            codepath = r"C:\Users\ASUS\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(codepath)

        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()
        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
        elif "hibernate" in query or "sleep" in query:
            display("Hibernating")
            subprocess.call("shutdown / h")
        elif "log off" in query or "sign out" in query:
            display("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        if 'list' in query:
            if isContain(query, ['add', 'create', 'make']):
                display("What do you want to add?")
                #item = record(False, False)
                item = takeCommand().lower()
                ToDo.toDoList(item)
                display("Alright, I added to your list")
                continue
            if isContain(query, ['show', 'my list']):
                items = ToDo.showtoDoList()
                display("Here are Contents of your To-Do List\n")
                #print(items)
                if len(items) == 1:
                    display(items[0])
                    #return
                else:
                    display('\n'.join(items))
                #if len(items) == 0:
                    #display("No Items in your List")
                #else:
                    #for i in items:
                        #display(str(items[i]))
                continue
            if isContain(query, ['clear','delete','erase']):
                display("Clearing your List")
                ToDo.truncatetoDoList()
                continue


        elif 'news' in query:

            try:
                jsonObj = urlopen('https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\')
                data = json.load(jsonObj)
                i = 1
                display('Here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============''' + '\n')
                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    display(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                print(str(e))

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            display("User asked to Locate")
            display(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")

        elif "don't listen" in query or "stop listening" in query:
            display("for how much time you want to stop sofia from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)


        elif any(ext in query for ext in end):
            display("Happy to be in your service. Have a nice time! Sophia Signs off!")
            exit()

        #weather foercast
        """
        elif "weather" in query:
            api_key = "API_Key_that_i_don't_have"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            display("City Name: ")
            city = takeCommand().lower()
            url = base_url + "appid=" + api_key + "&q=" + city
            response =requests.get(url)
            x = response.join
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " + str(current_temperature) + "\n atmospheric pressure (in hPa unit) = " + str(current_pressure) + "\n humidity (in percentage) = " + str(current_humidity) + "\n description = " + str(weather_description))
            else:
                print(" City Not Found ")
        """

if __name__ == '__main__':
    work()