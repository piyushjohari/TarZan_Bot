import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

MASTER="pIYUSH"
print("Initializing Jarvis")


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishme():
    h=int(datetime.datetime.now().hour)
    if(h>=0 and h<12):
            speak("Good morning dear"+MASTER+"sir")
    elif(h>=12 and h<18):
        speak("Good afternoon dear"+MASTER+"sir")    
    elif(h>=18 and h<21):
        speak("Good evening dear"+MASTER+"sir")    
    else:
        speak("Good night dear"+MASTER+"sir")    
    speak("how may i help you sir")

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        audio=r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language='en-in')
        print("User said:"+query)
    except Exception as e:
        print("Hye i am hbhj")
        query=None
    return query


    
speak("Hii sir Intializing Jarvis")
wishme()
query=takecommand()

#logic

if('wikipedia' in query.lower()):
    speak("yes sir searchin wikipedia")
    query=query.replace("wikipedia","")
    result=wikipedia.summary(query,sentences=2)
    speak(result)
elif("open youtube" in query.lower()):
    webbrowser.open("Youtube.com")













