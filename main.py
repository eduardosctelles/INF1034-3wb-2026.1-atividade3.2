from turtle import *
from time import sleep
t = Turtle()
t.hideturtle()
t.speed(100)

def ir(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def limpa():
    sleep(5)
    t.clear()
    t.left(90)

def estrela(tamanho, cor):
    t.begin_fill()
    t.fillcolor(cor)
    for i in range(5):
       t.forward(tamanho)
       t.right(144)
    t.end_fill()

def retangulo(comprimento, largura, cor):
    t.forward(comprimento)
    t.begin_fill()
    t.fillcolor(cor)
    t.right(90)
    t.forward(largura)
    t.right(90)
    t.forward(comprimento)
    t.right(90)
    t.forward(largura)
    t.right(90)
    t.forward(comprimento)
    t.right(90)
    t.end_fill()

def polonia():
    retangulo(500, 150, 'white')
    ir(-200, 50)
    t.left(90)
    retangulo(500, 150,'red')

ir(-200,200)
polonia()
limpa()

def ucrania():
    retangulo(500, 150, 'blue')
    ir(-200, 50)
    t.left(90)
    retangulo(500, 150, 'yellow')

ir(-200, 200)
ucrania()
limpa()

def emiradosarabes():
    retangulo(166, 300, 'red')
    t.left(90)
    retangulo(334,100,'green')
    ir(-34, 0)
    t.left(90)
    retangulo(334, 100, 'black')
    t.left(180)
    t.forward(100)

ir(-200, 200)
emiradosarabes()
limpa()

def gana():
    t.left(180)
    retangulo(500, 100, 'red')
    ir(-200, 100)
    t.left(90)
    retangulo(500, 100, 'yellow')
    ir(-200, 0)
    t.left(90)
    retangulo(500, 100, 'green')
    ir(0, 60)
    t.left(90)
    estrela(100, 'black')
    t.begin_fill()
    t.forward(38)
    for i in range(5):
        t.forward(24)
        t.right(72)
    t.end_fill()

ir(-200, 200)
gana()
limpa()

def mianmar():
    t.right(90)
    retangulo(500, 100, 'yellow')
    ir(-200, 100)
    t.left(90)
    retangulo(500, 100, 'green')
    ir(-200, 0)
    t.left(90)
    retangulo(500, 100, 'red')
    ir(-50, 64)
    t.color('white')
    t.left(90)
    estrela(200, 'white')
    t.begin_fill()
    t.forward(76)
    for i in range(5):
        t.forward(48)
        t.right(72)
    t.end_fill()

ir(-200, 200)
mianmar()

mainloop()