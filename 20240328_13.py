import random
import math
from tkinter.simpledialog import *
import tkinter as tk

def getString():
    retStr = askstring('문자열 입력', '거북이 쓸 문자열을 입력')
    return retStr

def getRGB():
    r = random.random()
    g = random.random()
    b = random.random()
    return r, g, b

def getXYAS(sw, sh, count, i):
    x, y, angle, size = 0, 0, 0, 20  # 문자열 크기 설정
    radius = 200  # 나선형의 반지름
    center_x, center_y = sw // 2, sh // 2  # 화면의 중심 좌표

    angle = (360 * 2 / count) * i  # 문자열을 나선형으로 그리기 위한 각도 계산
    radian = math.pi * angle / 180  # 각도를 라디안으로 변환

    distance_from_center = i * 5  # 나선형으로 안쪽으로 그리기 위한 거리 조절
    x = center_x + distance_from_center * math.cos(radian)  # x 좌표 계산
    y = center_y + distance_from_center * math.sin(radian)  # y 좌표 계산

    return [x, y, angle, size]


# Tkinter 윈도우 생성
root = tk.Tk()
root.title("Spiral Text")

# 화면 설정
width, height = 500, 500
canvas = tk.Canvas(root, width=width, height=height, bg='white')
canvas.pack()

# 문자열 입력 받기
inStr = getString()
count = len(inStr)

# 문자열 그리기
for i in range(count):
    x, y, angle, size = getXYAS(width, height, count, i)
    r, g, b = getRGB()
    canvas.create_text(x, y, text=inStr[i], font=("Arial", size),
                       fill=f"#{int(r * 255):02X}{int(g * 255):02X}{int(b * 255):02X}")

root.mainloop()