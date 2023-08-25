import threading
import time
import RPi.GPIO as GPIO
import speech_recognition as sr

#main.py와 연결되는 파일들
import display
import ai
import waterlevel

def main():
    
    global case #case를 전역변수로 사용하겠다고 선언
    
    while True:
        # 물 높이 측정 스레드 생성 및 시작
        waterlevel_thread = threading.Thread(target=waterlevel.waterlevelmeasure, args=(case.lock,))
        waterlevel_thread.start()
            
        # AI 호출 스레드 생성 및 시작
        with sr.Microphone() as source:
            ai_thread = threading.Thread(target=ai.listen_for_wake_word, args=(source,case.lock))
            ai_thread.start()
        
        # 두 스레드가 종료될 때까지 기다림
        waterlevel_thread.join()   
        ai_thread.join()
        
        # 여기에서 case 값에 따라 적절한 작업 수행
        display.show_gif(case)
        
if __name__ == "__main__":
    main()