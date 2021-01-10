import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

from pyjokes import get_joke


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 150)     # setting up new voice rate

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import requests
from bs4 import BeautifulSoup
import re
import webbrowser
import json



from pyjokes import get_joke

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 150)     # setting up new voice rate

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            name = listener.recognize_google(voice)
            command = command.lower()
            if 'venks' in command:
                command=command.replace('venks', '')
                talk(command)
    except:
        pass
    return command


def scrape_weather(city):
    url = 'https://www.google.com/search?q=accuweather+' + city
    page = requests.get(url)


    soup = BeautifulSoup(page.text, 'lxml')
    links = [a['href'] for a in soup.findAll('a')]
    link = str(links[16])
    link = link.split('=')
    link = str(link[1]).split('&')
    link = link[0]

    page = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(page.content, 'lxml')

    time = soup.find('p', attrs={'class': 'cur-con-weather-card__subtitle'})
    time = re.sub('\n', '', time.text)
    time = re.sub('\t', '', time)
    time =  time
    temperature = soup.find('div', attrs={'class': 'temp'})
    temperature = temperature.text

    realfeel = soup.find('div', attrs={'class': 'real-feel'})
    realfeel = re.sub('\n', '', realfeel.text)
    realfeel = re.sub('\t', '', realfeel)
    realfeel =  realfeel[-3:]
    climate = soup.find('span', attrs={'class': 'phrase'})
    climate = "Climate: " + climate.text

    info = 'For more information visit: ' + link

    print('The weather for today is: ')
    print(time)
    print(temperature)
    print(realfeel)
    print(climate)
    print(info)
    return city,temperature,realfeel

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'who' in command:
        info=command.replace('who is ','')
        info=wikipedia.summary(info,1)
        talk(info)
    elif 'what ' in command:
        info=command.replace('what is','')
        info=wikipedia.summary(info,2)
        talk('  '+ info)
    elif 'joke' in command:

        joke=get_joke()
        talk('Here is a joke' + joke)
    elif 'stop' in command:
        engine.stop()
    elif 'weather' in command:
        print('..')
        words = command.split(' ')
        print(words[-1])
        scrape_weather(words[-1])


    else:
        talk('Nope , say it again')

while True:
    run_alexa()
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            name = listener.recognize_google(voice)
            command = command.lower()
            if 'venks' in command:
                command=command.replace('venks', '')
                talk(command)
    except:
        pass
    return command
def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'who' in command:
        info=command.replace('who is ','')
        info=wikipedia.summary(info,1)
        talk(info)
    elif 'what ' in command:
        info=command.replace('what is','')
        info=wikipedia.summary(info,2)
        talk('  '+ info)
    elif 'joke' in command:
        #joke=command.replace('tell me a joke','')
        joke=get_joke()
        talk('Here is a joke' + joke)




run_alexa()
