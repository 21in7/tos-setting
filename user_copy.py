import shutil
import os
import time


def select_path():
    default_path = 'C:\\Program Files (x86)\\Steam\\steamapps\\common\\Tree of Savior (Kor)\\release'

    path_select = input("설치된 경로를 입력해 주세요. 기본 경로는 C드라이브입니다.\n(엔터를 누르면 기본 경로가 선택됩니다.)\n")

    if path_select:
        selected_path = path_select
    else:
        selected_path = default_path

    return selected_path

def select_file():
    qhd_file = './qhd.xml'
    fhd_file = './fhd.xml'
    
    file_select = input("사용 하시는 해상도를 입력해 주세요.\n1. qhd\n2. fhd\n")

    if file_select == '1':
        selected_file = qhd_file
    elif file_select == '2':
        selected_file = fhd_file
    else:
        print("올바른 선택이 아닙니다. 기본파일(fhd.xml)을 선택합니다.") 
        selected_file = fhd_file

    return selected_file

selected_path = select_path()
selected_file = select_file()
new_file_name = 'user.xml'
destination_path = os.path.join(selected_path, new_file_name)
shutil.copy(selected_file, destination_path)
time.sleep(5)