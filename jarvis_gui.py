import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
from time import sleep
from tkinter import *
from datetime import datetime
from playsound import playsound

   
screen = Tk()
screen.geometry("500x500")
screen.title("Jarvis AI")
heading = Label(text = "productivity app", bg = "grey", fg = "black", width = "500", height = "3")
heading.pack()

filename = "img1.png"
canvas = Canvas(screen, width = 300, height = 300)      
canvas.pack()      
img = PhotoImage(file=filename)      
canvas.create_image(20,20, anchor=NW, image=img)


def counter(): 
        run_alexa()

def counter1(): 
        my_label.config(text = "LISTENING...")
   
my_button = Button(screen, text = "Ping me",  command = counter ) 

my_label = Label(screen, text = "sleeping") 
my_label.pack() 
my_button.pack() 

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', 1)

outq= Label(text = "heyy, I am jarvis, your assistant, how may i help you" ,)
outq.place(x=30, y= 430)

query = Label(text = "welcome" ,)
query.place(x = 20, y = 360)



def talk(text):
    outq.config(text= text)
    engine.say(text)
    engine.runAndWait()
    
talk('heyy, I am jarvis, your assistant, how may i help you')

def take_command():
   
    try:
        with sr.Microphone() as source:
            my_label.config(text = "PROCESSING...")    
            talk('Ask me anything')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
            query.config(text=command)
            my_label.config(text = "SLEEPING...")
            
           
    except:
        pass
    return command
    
def run_alexa():
    command = take_command()
    if 'good morning' in command:
            talk('good morning sir, it is, 6: 00 am, right now. A perfect day is waiting to start')
            talk('weather outside is, no one cares. Please dont forget to add reminders for the day')
            talk('And remember End semester exam is on head')
            talk('Have a nice day')

    if 'add reminder at' in command:
            command = command.replace('add reminder at', '')
            talk('okat whats the reminder')
            
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
        sleep(100)
    elif len(command) == 0 :
        talk('if you dont have any question, then why you pinged me little ash**le')
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'google' in command:
        search = command.replace('google', '')
        url = 'http://google.com/search?q=' + search
        webbrowser.open(url, new=2)            
    elif 'manoj' in command:
        person = command.replace('manoj', '')
        info = "ehehheeeeeheee, very very sweet and nice teacher"
        talk(info)
    elif 'you are dumb' in command:
        person = command.replace('you are dumb', '')
        info = "saurabh, remember you had created me, and if you are calling me dumb, then you are the biggest motherfucker in the world"
        talk(info)
    elif 'what is ' in command:
        person = command.replace('what is', '')
        info = wikipedia.summary(person, 1)
        talk(info)
    elif 'who is ' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'money' in command:
        playsound('audio1.mp3')
    elif 'vidhayak' in command:
        playsound('audiokhufia.mp3')
    elif'kya hua' in command:
        playsound('audioflush.mp3')
    elif 'space' in command:
        playsound('audiokhufia.mp3')
    elif 'cheating' in command:
        playsound('audiokhufia.mp3')
    elif 'gana' in command:
        playsound('audioshadi.mp3')
    elif 'iit' in command:
        playsound('audio2_iit.mp3')
    elif 'jee' in command:
        playsound('audio2_iit.mp3')
    elif 'college' in command:
        playsound('audiotaarekh.mp3')
    elif 'delete' in command:
        playsound('audiobhool.mp3')
    elif 'harmonium' in command:
        playsound('audiosed.mp3')
        talk('thats it from my side')
    else:
        talk('Saurabh, you are not audible, Speak lodly and clearly')
    my_label.config(text = "LISTENING...")
    counter1()


