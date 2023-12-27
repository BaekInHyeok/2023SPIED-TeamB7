import os
import subprocess

def show_gif(case):
    
    # 이미지 경로 설정
    if case == 1: #물 높이가 충분한 상태
        image_path = "happy.gif"
    elif case == 2: # 물 보충을 권장하는 상황
        image_path = "/home/pi/2023SPIED-TEAMB7/sad.gif"
    elif case == 3: # 지금 바로 물 보충을 해야 하는 상황
        image_path = "/home/pi/2023SPIED-TEAMB7/angry.gif"
    elif case == 4 : #AI를 호출했을 때 반응
        image_path = "/home/pi/2023SPIED-TEAMB7/waiting.gif"
    elif case == 5 : #AI가 자신의 대답을 스피커를 통해 말할 때
        image_path = "/home/pi/2023SPIED-TEAMB7/answering.gif"
    else:
        print("올바르지 않은 경우입니다.")
        image_path = None

    # 이미지가 존재하는지 확인
    if image_path and os.path.exists(image_path):
    # feh로 이미지 열기
        subprocess.call(["feh", "-F", image_path])
    else:
        print(f"파일 {image_path}을(를) 찾을 수 없습니다.")