from tkinter import *
import requests
import matplotlib.pyplot as plt
import numpy as np

root = Tk()
root.title("Ginicoff.py")
root.geometry("800x450+700+500")
root.resizable(width=True,height=True)


file_post = {}
url = "http://localhost:500/items"
stroka = StringVar()
def peredacha(event):
    poor = float(e1.get())
    midleclass = float(e2.get())
    poor_income = float(e4.get())
    midleclass_income = float(e5.get())
    x1=poor
    x2=poor + midleclass
    x3=1
    y1=poor_income
    y2=poor_income + midleclass_income
    y3=1
    x = [0,x1,x2,x3]
    y = [0,y1,y2,y3]
    plt.plot(x,y)
    plt.title("Кривая Лоренца")
    plt.ylabel("Доходы")
    plt.xlabel("Численность")
    x01=[0,1]
    y01=[0,1]
    plt.plot(x01,y01)
    plt.savefig("gini_coff.png")
    file_post["poor"] = float(e1.get())
    file_post["midleclass"] = float(e2.get())
    file_post["rich"] = float(e3.get())
    file_post["poor_income"] = float(e4.get())
    file_post["midleclass_income"] = float(e5.get())
    file_post["rich_income"] = float(e6.get())
    result = requests.post(url, json = file_post)
    ginicoff_result = float(result.content)
    result_change["text"] = ginicoff_result
    
    
l = Label(text = "Калькулятор коэффициента Джини")
l1 = Label(text = "Инструкция: Введите в поля значения численности и дохода того или иного класса от общей численности населения и от общего дохода")
l2 = Label(text = "в десятичных дробях, чтобы сумма численностей и доходов не превышала единицу")
e1 = Entry()
e2 = Entry()
e3 = Entry()
e4 = Entry()
e5 = Entry()
e6 = Entry()

h1 = Label(text = "Численность бедных:").place(x=10,y=30)
h2 = Label(text = "Численность среднего класса:").place(x=10,y=50)
h3 = Label(text = "Численность богатых:").place(x=10,y=70)
h4 = Label(text = "Доход бедных:").place(x=10,y=90)
h5 = Label(text = "Доход среднего класса:").place(x=10,y=110)
h6 = Label(text = "Доход богатых:").place(x=10,y=130)
result = Label(text = "Результат:").place(x=10,y=240)
result_change = Label(text = "").place(x=100,y=240)
canvas = Canvas(root, height=400, width=700)
img = PhotoImage(file = 'gini_coff.png') 
image = canvas.create_image(0, 0, anchor='nw',image=img)

b = Button(text = "Отправить")
l.place(x=300,y=10)
l1.place(x=10,y=200)
l2.place(x=10,y=220)
e1.place(x=200,y=30, width=130, height=15)
e2.place(x=200,y=50, width=130, height=15)
e3.place(x=200,y=70, width=130, height=15)
e4.place(x=200,y=90, width=130, height=15)
e5.place(x=200,y=110, width=130, height=15)
e6.place(x=200,y=130, width=130, height=15)
b.place(x=335,y=115, width=70, height=30)
b.bind("<Button-1>", peredacha)



root.mainloop()
