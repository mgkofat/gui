from tkinter import *

def btn1_Click():
 x=int(ent_weight.get())
 y=int(ent_height.get())
 y=y/100
 z=float(x/(y*y))
 tlb_BMI.set(f'{z:.4f}')
 btn2_Click(z)

def btn2_Click(c):
    if c<18.7:
     tlb_Status.set(f'Underweight')
     lb8 = Label(root, text='', textvariable=tlb_Status,bg='white').grid(row=8, columnspan=3)
    elif c<24.9:
     tlb_Status.set(f'Normal')
     lb8 = Label(root, text='', textvariable=tlb_Status,bg='green').grid(row=8, columnspan=3)
    elif c<29.9:
     tlb_Status.set(f'Overweight')
     lb8 = Label(root, text='', textvariable=tlb_Status,bg='yellow').grid(row=8, columnspan=3)
    else :
     tlb_Status.set(f'Obese')
     lb8 = Label(root, text='', textvariable=tlb_Status,bg='red').grid(row=8, columnspan=3)
     
root = Tk()
root.geometry('270x250')
root.resizable(False, False)
root.option_add('*font','tahoma 10')
root.title('Body-Mass Index(BMI)')
tlb_BMI = StringVar()
tlb_Status = StringVar()
ent_weight = StringVar()
ent_height = StringVar()

lb3 = Label(root, text='').grid(row=0, column=0)
lb1 = Label(root, text='Weight').grid(row=1, column=1,padx=(0,30))
lb2 = Label(root, text='Height').grid(row=2, column=1,padx=(0,30))
ent1 = Entry(root, textvariable=ent_weight, width=10).grid(row=1, column=2,padx=(0,60))
ent2 = Entry(root, textvariable=ent_height, width=10).grid(row=2, column=2,padx=(0,60))
lb3 = Label(root, text='').grid(row=3, column=0)
btn1 = Button(root, text='คำนวณค่า', command=btn1_Click, width=25).grid(row=4,column=1,columnspan=2,padx=(0,20))
lb3 = Label(root, text='').grid(row=5, column=0)
lb4 = Label(root, text='ผลการคำนวณ',width=20).grid(row=6, column=1)
lb5 = Label(root, text='BMI    =     ').grid(row=7, column=1)
lb6 = Label(root, text='Status =     ').grid(row=8, column=1)
lb7 = Label(root, text='', textvariable=tlb_BMI).grid(row=7, columnspan=3)
lb8 = Label(root, text='', textvariable=tlb_Status).grid(row=8, columnspan=3)

tlb_BMI.set("n/a")
tlb_Status.set("n/a")

root.mainloop()
