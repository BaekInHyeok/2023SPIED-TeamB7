import os
import openai
from dotenv import load_dotenv
import time
import speech_recognition as sr
import pyttsx3
import numpy as np

# from os.path import join, dirname
# import matplotlib.pyplot as plt
# ^ matplotlib is great for visualising data and for testing purposes but usually not needed for production

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
model = 'gpt-3.5-turbo'

# Set up the speech recognition and text-to-speech engines
r = sr.Recognizer()
engine = pyttsx3.init()
voice = engine.getProperty('voices')[1]
engine.setProperty('voice', voice.id)
name = "emmet"
greetings = [f"whats up {name}", 
             "yeah?", 
             "listening"]

# Listen for the wake word "hello"
def listen_for_wake_word(source, lock):
    global case # case를 전역변수로 사용함을 선언
    print("Listening for 'Hello'...")

    while True:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            if "hello" in text.lower():
                print("Wake word detected.")
                with lock:
                    case = 4  # "hello"가 인식되면 case 값을 4로 설정
                engine.say(np.random.choice(greetings))
                engine.runAndWait()
                listen_and_respond(source, lock)
                break
        except sr.UnknownValueError:
            pass

# Listen for input and respond with OpenAI API
def listen_and_respond(source, lock):
    global case # case를 전역변수로 사용함을 선언
    print("Listening...")

    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")
        if not text:
            return

        # Send input to OpenAI API
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": f"{text}"}]) 
        response_text = response.choices[0].message.content
        print(f"OpenAI response: {response_text}")
        
        with lock:
            case = 5  # AI가 응답하기 직전에 case 값을 5로 설정

        # Speak the response
        engine.say(response_text)
        engine.runAndWait()

                
    except sr.UnknownValueError:
        time.sleep(2)
        print("Silence found, shutting up, listening...")
        
            
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        engine.say(f"Could not request results; {e}")
        engine.runAndWait()
        
# #use the default microphone as the audio source
# with sr.Microphone() as source:
#     listen_for_wake_word(source)