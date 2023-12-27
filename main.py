import time
import RPi.GPIO as GPIO
import time

#센서 및 액츄에이터 작동용 파일들
import waterlevel

global level

def main():
    global level
    
    level=0
    
    try:
        while True:
            print('======================')
            level=waterlevel.measure()
            print("level : ",level)
            
            time.sleep(2)
    except KeyboardInterrupt:
        # 프로그램 종료 시 GPIO 클린업
        GPIO.cleanup()
        
# 메인 함수 호출
if __name__ == '__main__':
    main()