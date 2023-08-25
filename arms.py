import RPi.GPIO as GPIO

#릴레이 모듈은 HIGH 신호에서 전기를 끊고, LOW 신호에서 전원을 인가한다.
#따라서, 릴레이 모듈을 사용하면, 라즈베리파이에 직결하는 방식과 반대다.

RELAY_PIN1 = 17 #GPIO 17번과 연결되어 있는 왼쪽 팔을 제어
RELAY_PIN2 = 27 #GPIO 27번과 연결되어 있는 오른쪽 팔을 제어

#왼쪽 팔 작동 시작
def left_on():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    GPIO.setup(RELAY_PIN1,GPIO.OUT)
    GPIO.output(RELAY_PIN1,GPIO.LOW)

#왼쪽 팔 작동 중단
def left_stop():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    GPIO.setup(RELAY_PIN1,GPIO.OUT)
    GPIO.output(RELAY_PIN1,GPIO.HIGH)

#오른쪽 팔 작동 시작
def right_on():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    GPIO.setup(RELAY_PIN2,GPIO.OUT)
    GPIO.output(RELAY_PIN2,GPIO.LOW)

#오른쪽 팔 작동 중단
def right_off():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    GPIO.setup(RELAY_PIN2,GPIO.OUT)
    GPIO.output(RELAY_PIN2,GPIO.HIGH)
