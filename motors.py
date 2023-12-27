import RPi.GPIO as GPIO
import pyttsx3
import time
import os
import subprocess

RELAY_PIN1 = 20
RELAY_PIN2 = 21

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    
def left_on():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    GPIO.setup(RELAY_PIN1,GPIO.OUT)
    GPIO.output(RELAY_PIN1,GPIO.LOW)
    
def left_off():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    GPIO.setup(RELAY_PIN1,GPIO.OUT)
    GPIO.output(RELAY_PIN1,GPIO.HIGH)
    
def right_on():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    GPIO.setup(RELAY_PIN2,GPIO.OUT)
    GPIO.output(RELAY_PIN2,GPIO.LOW)
    
def right_off():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    GPIO.setup(RELAY_PIN2,GPIO.OUT)
    GPIO.output(RELAY_PIN2,GPIO.HIGH)
    
def main():
    #subprocess.call(["feh","-F","/home/pi/watertest/sad.gif"])
    #speak("I'm so thirsty. Please help. Please don't leave me alone")
    # left_on()
    # time.sleep(0.03)
    # left_off()
    
    # time.sleep(1)
    
    #subprocess.call(["feh","-F","/home/pi/watertest/angry.gif"])
    # speak("Excuse me? Are you ignoring me? My root will dry out!. Change my water now!")
    # right_on()
    # time.sleep(0.03)
    # right_off()
    
    # time.sleep(1)
    
    #subprocess.call(["feh","-F","/home/pi/watertest/angry.gif"])
    speak("Thank you for changing my water. I'm so glad to your help ! I hope you have a nice day!")
    left_on()
    right_on()
    
    time.sleep(0.03)
    
    left_off()
    right_off()
    
    speak("")

if __name__ == "__main__":
    main()