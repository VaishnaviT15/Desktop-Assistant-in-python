import pyttsx3
import datetime
import speech_recognition  as sr
import wikipedia
import webbrowser
import os
#import smtplib

# dict of email address
# to use the voice in windows
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# to use the voice from your computer
engine.setProperty('voice',voices[1].id)

def speak(audio):
     engine.say(audio)
     engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Godd Morning!")

    elif hour>=12 and hour <18:
        speak("Good  Afternoon!")

    else:
        speak("Good Evening!")
    speak("I am VT Sir. Please tell me how may I help you")

def takeCommand():
    '''
    it Takes microphone input from the user
    and returns string output
    '''
    r  = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1
        audio = r.listen(source)

    try :
        print("Recognising...")
        query = r.recognize_google(audio)
        print(f"User said :{query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please....")
        return "None"
    return query

#def sendEmail(to,content):
    



if __name__ == "__main__":
    wishMe()
    if 1:
         query  = takeCommand().lower()
         # Logic for executing tasks based on query
         if  'wikipedia' in query:
             speak("Searching Wikipedia")
             query  = query.replace("wikipedia","") 
             results = wikipedia.summary(query,sentences=2)
             speak("According to Wikipedia")
             print(results)
             speak(results)
         elif 'open youtube' in query:
             webbrowser.open("youtube.com")   

         elif 'open google' in query:
             webbrowser.open(" google.com")   

         elif 'open gmail' in query:
             webbrowser.open("gmail.com")

         elif 'play music'  in query:
             music_dir  = 'F:\\Music\\mm' 
             songs = os.listdir(music_dir)
             #generate random no for song
             os.startfile(os.path.join(music_dir,songs[0])) 

         elif 'the time' in query:
             strTime  = datetime.datetime.now().strftime("%H:%M:%S")  
             print(strTime)
             speak(f" Sir the time is {strTime}") 
             
         elif 'start vscode'  in query:
             vscode_path  = "C:\\Users\\shri\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
             os.startfile(vscode_path)   
        

         elif 'start terminal' in query:
             cmd_path  = 'C:\\Windows\\System32\\cmd.exe'
             os.startfile(cmd_path)

         elif 'open paint' in query:
             doc  = "C:\\Windows\\System32\\mspaint.exe "
             os.startfile(doc)             










