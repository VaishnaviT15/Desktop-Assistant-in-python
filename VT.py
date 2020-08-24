import pyttsx3
import datetime
import speech_recognition  as sr


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
        query =  r.recognize_google(audio, Language='en_in')
        print("User said:{query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please....")
        return "None"
    return query
if __name__ == "__main__":
    wishMe()
    takeCommand()
