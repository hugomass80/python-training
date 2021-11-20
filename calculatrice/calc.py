from tkinter import *
from math import *
from re import sub

main = Tk()
main.title("Calculatrice")
main.geometry("350x270")
main.resizable(width=False, height=False)

menubar = Menu(main)
main.config(menu=menubar)
menuMode = Menu(menubar,tearoff=0)
menuParam = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Mode", menu=menuMode)
menubar.add_cascade(label="Paramètres", menu=menuParam)


def classique():
    print("Non scientifique")
    modeScientifique = False
    boutonScientifique(modeScientifique)

def scientifique():
    print("Scientifique")
    modeScientifique = True
    boutonScientifique(modeScientifique)


menuMode.add_command(label="Classique", command=classique)
menuMode.add_command(label="Scientifique", command=scientifique)
menuParam.add_command(label="Quitter", command=main.destroy)


nb1 = ""

def ajout(nb):
    global nb1
    nb1 += nb
    label["text"] = nb1

def num1():
    ajout("1")

def num2():
    ajout("2")

def num3():
    ajout('3')

def num4():
    ajout("4")

def num5():
    ajout("5")

def num6():
    ajout("6")

def num7():
    ajout("7")

def num8():
    ajout("8")

def num9():
    ajout("9")

def zero():
    ajout("0")

def parentheseOuverte():
    ajout("(")

def parentheseFermee():
    ajout(")")

def point():
    ajout(".")

def clear():
    global nb1,nb2
    nb1 = ""
    nb2 = ""
    label["text"] = ""

def add():
    ajout("+")

def sous():
    ajout("-")


def fois():
    ajout("*")


def div():
    ajout("/")

def egal():
    global nb1
    result = eval(nb1)
    nb = "("+nb1+")"
    nb1 = nb
    label["text"] = result
    result = 0


label = Label(main,text="0")
label.place(x=130,y=50)

Bouton = Button(main,text=" 1 ",command=num1).place(x=10,y=110)
Bouton = Button(main,text="  2  ",command=num2).place(x=70,y=110)
Bouton = Button(main,text="  3  ",command=num3).place(x=130,y=110)
Bouton = Button(main,text="  4  ",command=num4).place(x=10,y=150)
Bouton = Button(main,text="  5  ",command=num5).place(x=70,y=150)
Bouton = Button(main,text="  6  ",command=num6).place(x=130,y=150)
Bouton = Button(main,text="  7  ",command=num7).place(x=10,y=190)
Bouton = Button(main,text="  8  ",command=num8).place(x=70,y=190)
Bouton = Button(main,text="  9  ",command=num9).place(x=130,y=190)
Bouton = Button(main,text=" . ",command=point).place(x=10,y=230)
Bouton = Button(main,text=" 0 ",command=zero).place(x=70,y=230)
Bouton = Button(main,text=" ( ",command=parentheseOuverte).place(x=130,y=230)
Bouton = Button(main,text=" ) ",command=parentheseFermee).place(x=190,y=230)

Bouton = Button(main,text=" C ",command=clear).place(x=190,y=110)
Bouton = Button(main,text=" + ",command=add).place(x=190,y=150)
Bouton = Button(main,text="  -  ",command=sous).place(x=190,y=190)
Bouton = Button(main,text="  x  ",command=fois).place(x=250,y=110)
Bouton = Button(main,text="  /  ",command=div).place(x=250,y=150)
Bouton = Button(main,text=" = ",command=egal).place(x=250,y=190)

def pourcentage():
    global nb1
    if nb1.find("+") != -1:
        a = float(nb1.partition("+")[0])
        print(a)

        b = float(nb1.partition("+")[2])
        print(b)

        result = a+((a*b)/100)
        print(a)
        print(b)
    elif nb1.find("-") != -1:
        a = float(nb1.partition("-")[0])
        print(a)

        b = float(nb1.partition("-")[2])
        print(b)

        result = a-((a*b)/100)
        print(a)
        print(b)
    elif nb1.find("*") != -1:
        a = float(nb1.partition("*")[0])
        print(a)

        b = float(nb1.partition("*")[2])
        print(b)

        result = a*((a*b)/100)
        print(a)
        print(b)
    elif nb1.find("/") != -1:
        a = float(nb1.partition("/")[0])
        print(a)

        b = float(nb1.partition("/")[2])
        print(b)

        result = a/((a*b)/100)
        print(a)
        print(b)
    nb = "(" + str(result) + ")"
    nb1 = nb
    label["text"] = result

def racineCarree():
    global nb1
    result = sqrt(eval(nb1))
    nb = "(" + str(result) + ")"
    nb1 = nb
    label["text"] = result
def carre():
    global nb1
    result = pow(eval(nb1),2)
    nb = "(" + str(result) + ")"
    nb1 = nb
    label["text"] = result
def sinus():
    global nb1
    result = sin(eval(nb1))
    nb = "(" + str(result) + ")"
    nb1 = nb
    label["text"] = result
def cosinus():
    global nb1
    result = cos(eval(nb1))
    nb = "(" + str(result) + ")"
    nb1 = nb
    label["text"] = result
def tangente():
    global nb1
    result = tan(eval(nb1))
    nb = "(" + str(result) + ")"
    nb1 = nb
    label["text"] = result
def exponentielle():
    global nb1
    result = exp(eval(nb1))
    nb = "(" + str(result) + ")"
    nb1 = nb
    label["text"] = result
def logarithme():
    global nb1
    result = log(eval(nb1))
    nb = "(" + str(result) + ")"
    nb1 = nb
    label["text"] = result

frame = Frame(main)
frame.pack()

BoutonScientifique = Button(frame,text=" % ",command=pourcentage)
BoutonScientifique.pack( side = RIGHT )

BoutonScientifique = Button(frame,text=" √ ",command=racineCarree)
BoutonScientifique.pack( side = RIGHT )

BoutonScientifique = Button(frame,text=" x2 ",command=carre)
BoutonScientifique.pack( side = RIGHT )

BoutonScientifique = Button(frame,text=" sin ",command=sinus)
BoutonScientifique.pack( side = RIGHT )

BoutonScientifique = Button(frame,text=" cos ",command=cosinus)
BoutonScientifique.pack( side = RIGHT )

BoutonScientifique = Button(frame,text=" tan ",command=tangente)
BoutonScientifique.pack( side = RIGHT )

BoutonScientifique = Button(frame,text=" exp ",command=exponentielle)
BoutonScientifique.pack( side = RIGHT )

BoutonScientifique = Button(frame,text=" log ",command=logarithme)
BoutonScientifique.pack( side = RIGHT )






def boutonScientifique(modeScientifique):
    if modeScientifique:
        frame.pack()
    else:
        frame.pack_forget()

modeScientifique = False
boutonScientifique(modeScientifique)

main.mainloop()

