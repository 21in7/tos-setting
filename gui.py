import shutil
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def select_path():
    default_path = 'C:\\Program Files (x86)\\Steam\\steamapps\\common\\Tree of Savior (Kor)\\release'

    path_select = filedialog.askdirectory(title="설치된 경로를 선택해 주세요.", initialdir=default_path)

    if path_select:
        selected_path.set(path_select)
    else:
        selected_path.set(default_path)

def select_resolution(*args):
    resolution_mapping = {
        "1. qhd": './qhd.xml',
        "2. fhd": './fhd.xml',
        "3. wide_qhd": './wide_qhd.xml',
        "4. wide_fhd": './wide_fhd.xml'
    }

    selected_resolution_value = resolution_options.get()
    selected_file.set(resolution_mapping.get(selected_resolution_value, './fhd.xml'))

def copy_file():
    selected_path_value = selected_path.get()
    selected_file_value = selected_file.get()

    new_file_name = 'user.xml'
    destination_path = os.path.join(selected_path_value, new_file_name)

    try:
        shutil.copy(selected_file_value, destination_path)
        messagebox.showinfo("성공", "파일 복사가 완료되었습니다.")
    except Exception as e:
        messagebox.showerror("오류", f"파일 복사 실패: {e}")

# tkinter 윈도우 생성
root = tk.Tk()
root.title("파일 복사 GUI")

# 경로 선택
selected_path = tk.StringVar()
select_path()

path_label = tk.Label(root, text="설치된 경로:")
path_label.pack()

path_entry = tk.Entry(root, textvariable=selected_path, state='readonly')
path_entry.pack()

# 경로 다시 지정 버튼 추가
select_path_button = tk.Button(root, text="경로 다시 지정", command=select_path)
select_path_button.pack(pady=5)

# 해상도 선택
resolution_options = tk.StringVar()
resolution_options.set("1. qhd")  # 기본값은 1번 파일
resolution_label = tk.Label(root, text="해상도를 지정해주세요.:")
resolution_label.pack()

selected_file = tk.StringVar()
selected_file.set('./qhd.xml')  # 기본값은 qhd.xml로 설정

resolution_menu = tk.OptionMenu(root, resolution_options, "1. qhd", "2. fhd", "3. wide_qhd", "4. wide_fhd")
resolution_menu.pack()

# trace를 사용하여 옵션 변경 감지 후 콜백 함수 호출
resolution_options.trace_add("write", select_resolution)

# 버튼 생성 및 클릭 시 파일 복사 함수 호출
button = tk.Button(root, text="파일 복사 시작", command=copy_file)
button.pack(pady=10)

# tkinter 메인 루프 시작
root.mainloop()
