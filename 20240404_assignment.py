#3번 답 : (1)var.get(), (2)IntVar(), (3)var
from tkinter import *
window = Tk()

def rdo_change():
    if var.get() == 1 :
        labal1.configure(text="벤츠")
    else :
        label1.configure(text="포르쉐")

var = IntVar()
rdo1 = Radiobutton(window, text="벤츠", variable=var , value=1, command=rdo_change)
rdo2 = Radiobutton(window, text="포르쉐", variable=var , value=1, command=rdo_change)
label1 = Label(window, text="선택한 차량", fg="red")

rdo1.pack()
rdo2.pack()
label1.pack()

window.mainloop()


#4번 답 : (1)LEFT, (2)RIGHT, (3)TOP, (4)BOTTOM
from tkinter import *
window = Tk()

button1 = Button(window, text = "버튼1")
button2 = Button(window, text = "버튼2")
button3 = Button(window, text = "버튼3")

button1.pack(side = 빈칸)
button2.pack(side = 빈칸)
button3.pack(side = 빈칸)

window.mainloop()


#5번
from tkinter import *
from time import *

fnameList = ["jeju1.gif", "jeju2.gif", "jeju3.gif", "jeju4.gif", "jeju5.gif", "jeju6.gif",
             "jeju7.gif", "jeju8.gif", "jeju9.gif"]

num = 0

def clickNext():
    global num
    num = (num + 1) % len(fnameList)
    pLabel.configure(text=fnameList[num])

def clickPrev():
    global num
    num = (num - 1) % len(fnameList)
    pLabel.configure(text=fnameList[num])

window = Tk()

pLabel = Label(window, text=fnameList[num])
pLabel.pack()

btnPrev = Button(window, text="<이전>", command=clickPrev)
btnPrev.pack(side=LEFT)

btnNext = Button(window, text="<다음>", command=clickNext)
btnNext.pack(side=RIGHT)

window.mainloop()
