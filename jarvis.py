import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import pyaudio
import aiml

kernel = aiml.Kernel()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
terminate = ['bye', 'buy', 'shutdown', 'exit', 'quit', 'gotosleep', 'goodbye']



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis. Please tell me how may I help you?")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        #speak("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif any([i for i in terminate if i in query]):
            s="Bye, Have a nice day."
            print(s)
            speak(s)
            exit(0)
     
        else:
            if os.path.isfile("brain.dump"):
                print("i have learnt")
                kernel.bootstrap("brain.dump")
            else:
                kernel.bootstrap(learnFiles = "startup.aiml", commands = "load aiml b")
                kernel.saveBrain("brain.dump")
                print("i am learning")
            #kernel.learn("sample.aiml")
            response = kernel.respond(query)
            speak(response)
