###self study 10-5 : 10-22을 수정해서 이미지가 회색 영상으로 보이도록 하자
#힌트1 : 이미지 크기는 photo.width()와 photo.heighr()로 알아낸다.
#힌트2 : 각 픽셀의 색상 값은 photo.get(x위치, y위치)로 알아낸다. 반환 값은 (red, green, blue) 튜플이다.
#힌트3 : 색상을 회색 값으로 하려면 (red+green+blue)/3으로 처리한다.
#힌트4 : 이미지의 픽셀값을 변경하려면 다음 코드를 사용한다.

from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk


##함수 선언 부분##
def func_open():
  filename = askopenfilename(parent=window, filetypes=(("GIF 파일", "*.gif"),
                                                       ("모든 파일", "*.*")))
  image = Image.open(filename).convert("L")  # "L"은 회색조(그레이스케일)로 변환하는 모드입니다.
  photo = ImageTk.PhotoImage(image)
  pLabel.configure(image=photo)
  pLabel.image = photo


def func_exit():
  window.quit()
  window.destroy()


##메인 코드 부분##
window = Tk()
window.geometry("400x400")
window.title("명화 감상하기")

pLabel = Label(window)
pLabel.pack(expand=1, anchor=CENTER)

mainMenu = Menu(window)
window.config(menu=mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="파일 열기", command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label="프로그램 종료", command=func_exit)

window.mainloop()