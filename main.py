import threading
import time
# import speech_recognition as sr


import display
import ai
import waterlevel

def main():
    
    global case 
    
    while True:
        
        waterlevel_thread = threading.Thread(target=waterlevel.waterlevelmeasure, args=(case.lock,))
        waterlevel_thread.start()
            
        
        # with sr.Microphone() as source:
        #     ai_thread = threading.Thread(target=ai.listen_for_wake_word, args=(source,case.lock))
        #     ai_thread.start()
        
        
        waterlevel_thread.join()   
        # ai_thread.join()
        
        
        display.show_gif(case)
        
if __name__ == "__main__":
    main()