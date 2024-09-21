import speech_recognition as sr
import pyttsx3
import webbrowser
import musicLibrary 

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
   
    

if __name__ == "__main__":
    speak("Initializing Jarvis")
    
    while True:
            r = sr.Recognizer()
            # recognize speech using Sphinx
            print("Recognizing")
            try:
                with sr.Microphone() as source:  # Use default microphone
                    print("Listening...")
                    # Adjusts for background noise
                    audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)
                word = r.recognize_google(audio)
                if(word.lower() == "jarvis"):
                    speak("Ya")
                    # Listening for command
                    with sr.Microphone() as source:  # Use default microphone
                        print("Jarvis Active")
                        audio = r.listen(source)
                        command = r.recognize_google(audio)

                        processCommand(command)

            except Exception as e:
                print("Error: {0}".format)
            