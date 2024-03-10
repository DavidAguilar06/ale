import turtle as tur
import colorsys as cs
from tkinter import *
#from customtkinter import CTk, CTkFrame

def teamo():
    #A
    tur.penup()
    tur.goto(-250, 200)
    tur.pendown()
    tur.right(70)
    tur.forward(100)
    tur.right(180)
    tur.penup()
    tur.forward(100)
    tur.pendown()
    tur.right(220)
    tur.forward(100)
    tur.right(180)
    tur.penup()
    tur.forward(50)
    tur.pendown()
    tur.right(70)
    tur.forward(35)
    tur.penup()
    tur.right(70)
    tur.forward(50)
    tur.right(200)
    tur.forward(95)
    tur.right(90)
    tur.forward(40)
    #L
    tur.pendown()
    tur.right(90)
    tur.forward(95)
    tur.left(90)
    tur.forward(55)
    tur.penup()
    #E
    tur.forward(95)
    tur.pendown()
    tur.right(180)
    tur.forward(55)
    tur.right(90)
    tur.forward(95)
    tur.right(90)
    tur.forward(55)
    tur.right(90)
    tur.penup()
    tur.forward(47.25)
    tur.right(90)
    tur.forward(55)
    tur.right(180)
    tur.pendown()
    tur.forward(55)
    tur.left(90)
    tur.penup()
    tur.forward(47.25)
    tur.right(90)
    tur.forward(40)
    #X
    tur.pendown()
    tur.right(60)
    tur.forward(110)
    tur.right(180)
    tur.penup()
    tur.forward(55)
    tur.pendown()
    tur.left(120)
    tur.penup()
    tur.forward(55)
    tur.pendown()
    tur.left(180)
    tur.forward(110)
    
    tur.right(60)
    tur.penup()
    tur.forward(75)
    tur.pendown()
    tur.right(70)
    tur.forward(100)
    tur.right(180)
    tur.penup()
    tur.forward(100)
    tur.pendown()
    tur.right(220)
    tur.forward(100)
    tur.right(180)
    tur.penup()
    tur.forward(50)
    tur.pendown()
    tur.right(70)
    tur.forward(35)
    tur.penup()
    tur.right(70)
    tur.forward(50)
    tur.right(200)
    tur.forward(95)
    tur.right(90)
    tur.forward(40)
    #tur.clear()
    tur.hideturtle()
    tur.done()
    
    


def click():
    tur.setup(800,800)
    tur.speed(0)
    tur.width(2)
    tur.bgcolor("black")
    for j in range(25):
        for i in range(15):
            tur.color(cs.hsv_to_rgb(i/15,j/25,1))
            tur.right(90)
            tur.circle(200-j*4,90)
            tur.left(90)
            tur.circle(200-j*4,90)
            tur.right(180)
            tur.circle(50,24)
        
    tur.hideturtle()

    tur.done()
    
window  = Tk()
button = Button(window,
                text ="hiiii",
                command=teamo,
                state=ACTIVE)
button.pack()
button = Button(window,
                text ="te amo",
                command=click,
                state=ACTIVE)
button.pack()
window.mainloop()




