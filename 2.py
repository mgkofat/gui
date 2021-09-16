from tkinter import *

expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    try:
 
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
 
    except:
        equation.set(" ERROR ")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("0")
 
gui = Tk()
gui.option_add('*font','tahoma10')
gui.title("Calculator")
gui.resizable(False,False)
equation = StringVar()

en = Entry(gui,textvariable=equation,width=23,borderwidth=5,justify = RIGHT).grid(row=0, column=0,columnspan=4)
button1 = Button(gui, text=' 1 ',width=5,command=lambda: press(1)).grid(row=4, column=0)
button2 = Button(gui, text=' 2 ',width=5,command=lambda: press(2)).grid(row=4, column=1)
button3 = Button(gui, text=' 3 ',width=5,command=lambda: press(3)).grid(row=4, column=2)
button4 = Button(gui, text=' 4 ',width=5,command=lambda: press(4)).grid(row=3, column=0)
button5 = Button(gui, text=' 5 ',width=5,command=lambda: press(5)).grid(row=3, column=1)
button6 = Button(gui, text=' 6 ',width=5,command=lambda: press(6)).grid(row=3, column=2)
button7 = Button(gui, text=' 7 ',width=5,command=lambda: press(7)).grid(row=2, column=0)
button8 = Button(gui, text=' 8 ',width=5,command=lambda: press(8)).grid(row=2, column=1)
button9 = Button(gui, text=' 9 ',width=5,command=lambda: press(9)).grid(row=2, column=2)
button0 = Button(gui, text=' 0 ',width=11,command=lambda: press(0)).grid(row=5, column=0,columnspan=2)
plus = Button(gui, text=' + ',width=5,height=3,command=lambda: press("+")).grid(row=2, column=3,rowspan=2)
minus = Button(gui, text=' - ',width=5,command=lambda: press("-")).grid(row=1, column=3)
multiply = Button(gui, text=' * ',width=5,command=lambda: press("*")).grid(row=1, column=2)
divide = Button(gui, text=' / ',width=5,command=lambda: press("/")).grid(row=1, column=1)
equal = Button(gui, text=' EN ',width=5,height=3, command=equalpress).grid(row=4, column=3,rowspan=2)
clear = Button(gui, text='clr',width=5,command=clear).grid(row=1, column=0)
decimal= Button(gui, text='.',width=5,command=lambda: press('.')).grid(row=5, column=2)

equation.set("0")
gui.mainloop()
