import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk


# Function Menu List
def EspressoClick():
    Entry_Order.delete(0,END)
    Entry_Order.insert(0,'Espresso')

def AmericanoClick():
    Entry_Order.delete(0,END)
    Entry_Order.insert(0,'Americano')

def CappuccinoClick():
    Entry_Order.delete(0,END)
    Entry_Order.insert(0,'Cappuccino')

def LatteClick():
    Entry_Order.delete(0,END)
    Entry_Order.insert(0,'Latte')

# function Sweetness Level
def Level0Click():
    Entry_Sweetness.delete(0,END)
    Entry_Sweetness.insert(0,'0%')

def Level50Click():
    Entry_Sweetness.delete(0,END)
    Entry_Sweetness.insert(0,'50%')

def Level100Click():
    Entry_Sweetness.delete(0,END)
    Entry_Sweetness.insert(0,'100%')

# Function Submit Order
def SubmitOrder():
    menu = Entry_Order.get()
    sweet = Entry_Sweetness.get()
    if menu == 'Espresso' and sweet == '0%':
        Text_box.insert(END, ES0)
    elif menu == 'Espresso' and sweet == '50%':
        Text_box.insert(END, ES50)
    elif menu == 'Espresso' and sweet == '100%':
        Text_box.insert(END, ES100)
    elif menu == 'Americano' and sweet == '0%':
        Text_box.insert(END, A0)
    elif menu == 'Americano' and sweet == '50%':
        Text_box.insert(END, A50)
    elif menu == 'Americano' and sweet == '100%':
        Text_box.insert(END, A100)
    elif menu == 'Cappuccino' and sweet == '0%':
        Text_box.insert(END, Cap0)
    elif menu == 'Cappuccino' and sweet == '50%':
        Text_box.insert(END, Cap50)
    elif menu == 'Cappuccino' and sweet == '100%':
        Text_box.insert(END, Cap100)
    elif menu == 'Latte' and sweet == '0%':
        Text_box.insert(END, LA0)
    elif menu == 'Latte' and sweet == '50%':
        Text_box.insert(END, LA50)
    elif menu == 'Latte' and sweet == '100%':
        Text_box.insert(END, LA100)

# Function Cancel Order
def CancelOrder():
    Entry_Order.delete(0,END)
    Entry_Sweetness.delete(0,END)
    Text_box.delete(1.0,END)

MainWindow = Tk()
# MainWindow
MainWindow.title("Iced Coffee Recipes")
MainWindow.geometry("300x500")
Order = StringVar()
Sweetness = StringVar()

# Label
Label_Menu = Label(MainWindow, text = 'Menu List', font = 15)
Label_Menu.grid(row = 0, column = 0)
Label_SweetnessLevel = Label(MainWindow, text = 'Sweetness Level', font = 15)
Label_SweetnessLevel.grid(row = 3, column = 0)
Label_Order = Label(MainWindow, text = 'Order', font = 15)
Label_Order.grid(row = 7, column = 0)
Label_Sweetness = Label(MainWindow, text = 'Sweetness', font = 15)
Label_Sweetness.grid(row = 8, column = 0)



# Button Menu
Button_Espresso = Button(MainWindow, text = 'Espresso', command = EspressoClick, font = 10, width = 10)
Button_Espresso.grid(row = 1, column = 0)
Button_Americano = Button(MainWindow, text = 'Americano', command = AmericanoClick, font = 10, width = 10)
Button_Americano.grid(row=1, column = 1)
Button_Cappuccino = Button(MainWindow, text = 'Cappuccino', command = CappuccinoClick, font = 10, width = 10)
Button_Cappuccino.grid(row = 2, column = 0)
Button_Latte = Button(MainWindow, text = 'Latte', command = LatteClick, font = 10, width = 10)
Button_Latte.grid(row = 2, column = 1)

# Button Sweetness Level
Button_Level0 = Button(MainWindow, text = '0 %', command = Level0Click, font = 10, width = 5)
Button_Level0.grid(row = 4, column = 0)
Button_Level50 = Button(MainWindow, text = '50 %', command = Level50Click, font = 10, width = 5)
Button_Level50.grid(row = 5, column = 0)
Button_Level100 = Button(MainWindow, text = '100 %', command = Level100Click, font = 10, width = 5)
Button_Level100.grid(row = 6, column = 0)

# Button submit
Button_Submit = Button(MainWindow, text = 'Submit', command = SubmitOrder , font = 10)
Button_Submit.grid(row = 9, column = 1)

# Button cancel
Button_Cancel = Button(MainWindow, text = 'Cancel', command = CancelOrder , font = 10)
Button_Cancel.grid(row = 10, column = 1)

# Entry Order and sweetness
Entry_Order = Entry(MainWindow)
Entry_Order.grid(row = 7, column = 1)
Entry_Sweetness = Entry(MainWindow)
Entry_Sweetness.grid(row = 8, column = 1)

# Text box
Text_box = Text(MainWindow, width = 35, height = 5)
Text_box.grid(row = 11, column = 0, columnspan = 5)


# Coffee recipes
# Espresso SweetnessLevel0
ES0 = ''' 
    Espresso SweetnessLevel0
1.Espresso shot     4 oz (120 ml)
2.Milk                     45 ml
'''
# Espresso SweetnessLevel50
ES50 = ''' 
    Espresso SweetnessLevel50
1.Espresso shot     4 oz (120 ml)
2.Sweetened Condensed      15 ml
3.Milk                     30 ml
'''
# Espresso SweetnessLevel100
ES100 = ''' 
    Espresso SweetnessLevel100
1.Espresso shot     4 oz (120 ml)
2.Sweetened Condensed      30 ml
3.Milk                     15 ml 
'''
# Americano SweetnessLevel0
A0 = ''' 
    Americano SweetnessLevel0
1.Espresso shot      3 oz (90 ml)
2.Water                    90 ml
'''
# Americano SweetnessLevel50
A50 = '''
    Americano SweetnessLevel50 
1.Espresso shot      3 oz (90 ml)
2.Syrup                    15 ml
3.Water                    75 ml
'''
# Americano SweetnessLevel100
A100 = ''' 
    Americano SweetnessLevel100
1.Espresso shot      3 oz (90 ml)
2.Syrup                    30 ml
3.Water                    60 ml
'''
# Cappuccino SweetnessLevel0
Cap0 = ''' 
    Cappuccino SweetnessLevel0
1.Espresso shot      3 oz (90 ml)
2.Milk                     45 ml
'''
# Cappuccino SweetnessLevel50
Cap50 = ''' 
    Cappuccino SweetnessLevel50
1.Espresso shot      3 oz (90 ml)
2.Sweetened Condensed      15 ml
3.Milk                     30 ml
'''
# Cappuccino SweetnessLevel100
Cap100 = ''' 
    Cappuccino SweetnessLevel100
1.Espresso shot      3 oz (90 ml)
2.Sweetened Condensed      30 ml
3.Milk                     15 ml
'''
# Latte SweetnessLevel0
LA0 = ''' 
    Latte SweetnessLevel0
1.Espresso shot      2 oz (60 ml)
2.Milk                    125 ml
'''
# Latte SweetnessLevel50
LA50 = ''' 
    Latte SweetnessLevel50
1.Espresso shot      2 oz (60 ml)
2.Sweetened Condensed      15 ml
3.Milk                    110 ml
'''
# Latte SweetnessLevel100
LA100 = ''' 
    Latte SweetnessLevel100
1.Espresso shot      2 oz (60 ml)
2.Sweetened Condensed      30 ml
3.Milk                     95 ml
'''

MainWindow.mainloop()