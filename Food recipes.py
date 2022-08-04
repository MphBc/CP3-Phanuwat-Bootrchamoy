import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk

# เมนูผัดกะเพรา
A = '''
    เมนูผัดกะเพรา
    ส่วนประกอบ
       1.เนื้อสัตว์ 200 กรัม
       2.กระเทียม 2 ช้อนโต๊ะ
       3.ซีอิ๊วขาว 1 ช้อนโต๊ะ
       4.น้ำมันหอย 1 ช้อนโต๊ะ
       5.น้ำตาลทราย 1 ช้อนชา
       6.ซีอิ๊วดำเล็กน้อย 
'''

# เมนูทอดกระเทียม
B = '''
    เมนูทอดกระเทียม
    ส่วนประกอบ      
    1.เนื้อสัตว์ 300 กรัม
    2.กระเทียมสับ 1 ถ้วย
    3.รากผักชี 5 ราก
    4.กระเทียม (สำหรับสามเกลอ) 1 หัว
    5.พริกไทยเม็ด 1 ช้อนชา
    6.ซอสหอยนางรม 1 ช้อนโต๊ะ
    7.ซีอิ๊วขาว 1/2 ช้อนโต๊ะ
    8.ซอสปรุงรส 1/2 ช้อนโต๊ะ
    9.น้ำตาลทราย 1 ช้อนชา
    10.ผักชี ตามชอบ
'''

# เมนูผัดพริกแกง
C = '''
    เมนูผัดพริกแกง
    ส่วนประกอบ
    1.เนื้อสัตว์ 300 กรัม
    2.น้ำมันพืช สำหรับผัด
    3.น้ำพริกแกงเผ็ด 1 ช้อนโต๊ะ
    4.น้ำปลา 1 ช้อนโต๊ะ
    5.น้ำตาลปี๊บ หรือน้ำตาลทราย 1/2 ช้อนโต๊ะ
    6.ใบมะกรูดซอย 3 ใบ
    7.พริกชี้ฟ้าแดง (แต่งจาน)
   
'''

def MenuSelection():
    if FoodLists.get() == 'ผัดกะเพรา' :
        output.insert('end', A)
    elif FoodLists.get() == 'ทอดกระเทียม':
        output.insert('end', B)
    elif FoodLists.get() == 'ผัดพริกแกง':
        output.insert('end', C)

MainWindow = Tk()
# MainWindow
MainWindow.title("Food recipes")
MainWindow.geometry("400x250")

# Label Food list
Label_FoodList = Label(MainWindow, text = 'ราการอาหาร')
Label_FoodList.grid(row=0,column=0)

# Combobox
n = tk.StringVar()
FoodLists = ttk.Combobox(MainWindow, width = 27)

# Adding combobox drop down list
FoodLists['values'] =('ผัดกะเพรา',
                      'ทอดกระเทียม',
                      'ผัดพริกแกง')
FoodLists.grid(row=1,column=0)

# Button selection
ButtonSelection = Button(MainWindow, text='เลือก', command = MenuSelection)
ButtonSelection.grid(row=1,column=1)

# Box ingredient
output = Text(MainWindow, width=40, height=20)
output.grid(row=5, column=0)

MainWindow.mainloop()
