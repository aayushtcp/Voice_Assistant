import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random
# from pygame import mixer
# from playsound import playsound


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()
# speak("Initializing jarvis...")

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning aayush sir")
    elif hour>=12 and hour<18:
        speak("Good afternoon aayush sir")
    elif hour>=18 and hour<20:
        speak("Good evening aayush sir")
    else:
        speak("sleep well sir")
    speak("This is your voice assistaint Preyaans")
    speak("What can I help you for?")

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com', 578)
    server.ehlo()
    server.starttls()
    server.login('your_gmail@gmail.com', 'your_password')
    server.sendmail('your_gmail@gmail.com',to,content)
    server.close()
    
def takecommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        query = None
    return query


# speak("initializing jarvis")
if __name__=="__main__":
    wishme()
    while True:
        query = takecommand()

        if 'wikipedia' in query.lower():
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences =1)
            print(results)
            speak(results) 
        elif 'open youtube' in query.lower():
            url="youtube.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)
            
        elif 'open google' in query.lower():
            url="google.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'say some bad words' in query.lower():
            speak("fuck")
            speak("mugi, maa chik ni, ran di koo ban, laa do, puu tii ")


        elif 'open stack overflow' in query.lower():
            speak("Opening stack overflow")
            url="stackoverflow.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'technology news' in query.lower():
            url="gsmarena.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'check my internet speed' in query.lower():
            url="fast.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)
            

        elif 'who developed you' in query.lower():
            speak("I was recently developed by sir Aayush Dhaa kaal")
            speak("He is one of the tallented person in technology and he is from Nepal")
            speak("Jai Nepal, Love Nepal")

        elif 'hello friend' in query.lower():
            speak("Yes I am here, and remember, justice for Nirmala Paanta")

       
        elif 'play music' in query.lower():
            speak("Playing music")
            music_dir='D:\\mero python\\python_sg\\'
            songs= os.listdir(music_dir)
            choose_song=random.choice(songs)
            os.startfile('D:\\mero python\\python_sg\\'+choose_song)

        elif 'power' in query.lower():
            speak("I am showing my power")
            music_dir='D:\\mero python\\python_sg\\beatbox\\'
            songs= os.listdir(music_dir)
            choose_song=random.choice(songs)
            os.startfile('D:\\mero python\\python_sg\\beatbox\\'+choose_song)

        elif 'the time' in query.lower():
            strtime = datetime.datetime.now().strftime("%H: %M")
            speak(f"Sir, The time is, {strtime}, at this movement ")

        elif 'open opera mini' in query.lower():
            speak("Opening opera mini")
            codePath='C:\\Users\\dell\\AppData\\Local\\Programs\\Opera\\launcher.exe'
            os.startfile(codePath)

        elif 'email to' in query.lower():
            try:
                speak("What should I say")
                content= takecommand()
                to = "kaslai_pathauni_ho@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry sir, I am not able to send this email at the movement!")
        elif 'stop' or 'exit' or 'out' in query.lower():
            speak("okay sir")
            exit()

        elif 'hellow friend' in query.lower():
            speak("Yes I am here, and remember, justice for Nirmala Panta")
        
        elif 'who is yaman' in query.lower():
            speak("Yaman is tallented  programmer representing Nepal, and he is also good at, python!")
        # elif 'search' in query.lower():
            # search=speak("What do you want to search for?")
            # url='https://google.com/search?q=' +search
            # webbrowser.get().open(url)
            # print('Here is what I found for' +search)
        else:
            speak("Cannot recognize your voice sir, please say again")
            
            
#            hello this line is from me
