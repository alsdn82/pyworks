# gui 프로그램 만들기 - tkinter 모듈 불러오기
# 루트 > 프레임 > 라벨, 버튼
from tkinter import *

def click():
    print("안녕~ 파이썬!")



root = Tk()  # 루트 생성
root.title("윈도우 창")
root.geometry("300x100+800+300")    # 창의 크기(너비 x 높이 + x좌표 + y좌표)

frame = Frame(root)  # root를 매개로 frame객체 생성
frame.pack()     # 화면에 라벨, 버튼 출력(가운데 정렬)

Label(frame, text="Hellow~ Python!", font=("Times", 16)).grid(row=0, column=0) #1행 1열
Button(frame, text="확인", command=click).grid(row=1, column=0)   # 버튼 명령 실행 command - click()의 괄호 생략


root.mainloop()