import pyttsx3
import time

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    
speak("I'm a little thirsty")
time.sleep(1)
speak("I'm too thirsty!")
time.sleep(1)
speak("I'm not thirsty now!")
time.sleep(1)