from tkinter import *

def leftClickButton(event):
    result = float(textBoxWeight.get())/(float(textBoxHeight.get())/100)**2
    re_bel = Label(MainWindow, text= str(result))
    re_bel.configure()
    re_bel.grid(row=0, column=3)
    if result >= 30.0 :
        BMI = Label(MainWindow, text= "อ้วนมาก")
        BMI.configure()
        BMI.grid(row=1,column=3)
    elif 25.0 <= result <= 29.9 :
        BMI = Label(MainWindow, text="อ้วน")
        BMI.configure()
        BMI.grid(row=1, column=3)
    elif 23.0 <= result <= 24.9 :
        BMI = Label(MainWindow, text="น้ำหนักเกิน")
        BMI.configure()
        BMI.grid(row=1, column=3)
    elif 18.6 <= result <= 22.9 :
        BMI = Label(MainWindow, text="น้ำหนักปกติ เหมาะสม")
        BMI.configure()
        BMI.grid(row=1, column=3)
    elif result <= 18.5 :
        BMI = Label(MainWindow, text="ผอมเกินไป")
        BMI.configure()
        BMI.grid(row=1, column=3)

MainWindow = Tk()
labelHeight = Label(MainWindow, text="ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeigth = Label(MainWindow, text="น้ำหนัก (Kg.)")
labelWeigth.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text = "คำนวน")
calculateButton.grid(row=2)
calculateButton.bind('<Button-1>',leftClickButton)
labelResult = Label(MainWindow, text="BMI:")
labelResult.grid(row=0,column=2)

MainWindow.mainloop()

#labelResult.configure(text=float(textBoxWeight.get())/(float(textBoxHeight.get())/100)**2)