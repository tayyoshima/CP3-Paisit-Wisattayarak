from tkinter import *

def leftClickButton(event):
    txt = int(textBoxW.get())/((int(textBoxH.get())/100)*(int(textBoxH.get())/100))
    print(txt)
    if txt < 18.5 :
        labelResult.configure(text="น้ำหนักต่ำกว่าเกณฑ์")
    elif txt < 22.9 :
        labelResult.configure(text="สมส่วน")
    elif txt < 24.9 :
        labelResult.configure(text="น้ำหนักเกิน")
    elif txt < 29.9 :
        labelResult.configure(text="โรคอ้วน")
    else :
        labelResult.configure(text="โรคอ้วนอันตราย")



window = Tk()
labelHeight = Label(window,text = "ส่วนสูง (.cm)")
labelHeight.grid(row=0,column=0)
textBoxH = Entry(window)
textBoxH.grid(row=0,column=1)
labelWeight = Label(window,text = "น้ำหนัก (.kg)")
labelWeight.grid(row=1,column=0)
textBoxW = Entry(window)
textBoxW.grid(row=1,column=1)
calcalateButton = Button(window,text = "คำนวณ")
calcalateButton.bind("<Button-1>",leftClickButton)
calcalateButton.grid(row=2,column=0)
labelResult = Label(window,text="ผลลัพธ์")
labelResult.grid(row=2,column=1)
window.mainloop()