import pyttsx3
import time
import RPi.GPIO as GPIO
import subprocess


image1 = '/home/pi/watertest/normal.gif'
image2 = '/home/pi/watertest/angry.gif'
image3 = '/home/pi/watertest/sad.gif'
image4 = '/home/pi/watertest/happy.gif'


WATER_PIN_HIGH = 13
WATER_PIN_LOW = 19

TRIG = 23
ECHO = 24


def ultrasonic():
    GPIO.setmode(GPIO.BCM)
    time.sleep(0.0001)
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    GPIO.output(TRIG, False)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        start = time.time()

    while GPIO.input(ECHO) == 1:
        stop = time.time()

    check_time = stop-start
    distance = check_time * 34300 / 2
    print("Distance : %.1f cm" % distance)
    return distance


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def detect_LOW():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(WATER_PIN_LOW, GPIO.IN)
    return GPIO.input(WATER_PIN_LOW)


def detect_HIGH():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(WATER_PIN_HIGH, GPIO.IN)
    return GPIO.input(WATER_PIN_HIGH)


def main():
    global water1
    global water2
    global distance

    water1 = 0
    water2 = 0
    distance = 0

    while True:
        print('======= Start =======')
        water1 = detect_LOW()
        water2 = detect_HIGH()
        distance = ultrasonic()

        if water1 == 0 and water2 == 0 and distance < 20:
            print('WATER LEVEL IS DANGEROUS')
            process = subprocess.Popen(['xdg-open', image2])
            speak(
                "Excuse me? Are you ignoring me? My root will dry out!. Change my water now!")

        elif water1 == 1 and water2 == 0 and distance < 20:
            print('Alarm! Low WATER LEVEL')
            process = subprocess.Popen(['xdg-open', image3])
            speak("I'm so thirsty. Please help. Please don't leave me alone")

        elif water1 == 1 and water2 == 1 and distance < 20:
            print('WATER LEVEL IS OK!')
            process = subprocess.Popen(['xdg-open', image4])
            speak(
                "Thank you for changing my water. I'm so glad to your help ! I hope you have a nice day!")

        else:
            process = subprocess.Popen(['xdg-open', image1])

        print('===== Complete =====')
        print('')

        time.sleep(4)

        process.kill()


if __name__ == '__main__':
    main()
