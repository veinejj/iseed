from tkinter import *
import os
import random

## 전역 변수 선언 부분 ##
btnList = [None]*9
fnameList = ["honeycomb.gif", "icecream.gif", "jellybean.gif", "kitkat.gif",
             "lollipop.gif", "marshmallow.gif", "nougat.gif", "oreo.gif", "pie.gif"]
photoList = [None]*9
xPos, yPos = 0, 0

## 메인 코드 부분 ##
window = Tk()
window.geometry("210x210")

# 현재 작업 디렉토리를 기준으로 이미지 파일을 불러옴
current_directory = os.path.dirname(os.path.abspath(__file__))
# 이미지 파일 리스트를 섞음
random.shuffle(fnameList)

for i in range(0,9):
    photoList[i] = PhotoImage(file=os.path.join(current_directory, fnameList[i]))
    btnList[i] = Button(window, image=photoList[i])

for i in range(0,3):
    for k in range(0,3):
        btnList[i*3 + k].place(x=xPos, y=yPos)  # 올바른 버튼 인덱스를 사용하여 위치 지정
        xPos += 70
    xPos = 0
    yPos += 70

window.mainloop()