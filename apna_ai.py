import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from time import sleep
from gtts import gTTS



listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty("language",'hi')



def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
  
    try:
        with sr.Microphone() as source:
            print('listening...')
            talk('ask me you fucking bitch')
            voice = listener.listen(source , language='hi-In')
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'india' in command:
                command = command.replace('india', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
   
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
        sleep(100) # Time in seconds
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'what is ' in command:
        person = command.replace('what is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'cutting' in command:
        talk("tera baap chhod ke gaya tha ya teri maa")

    else:
        talk('paan , thuk, ke bol ')


while True:
    run_alexa()
