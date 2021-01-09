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
