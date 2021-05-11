import turtle
from random import *
from time import sleep

WIDTH, HEIGHT = 600, 600
COLOURS = ["blue","red","black","cyan","orange","brown","pink","green","yellow","violet"]

def intro():
    while True:
        num = input("How many turtles would you like to play with?(2-10): ")
        if num.isdigit():
            num = int(num)
            if 2 <= num <= 10:
                break
            print("Your number is out of range. Try again!")
        else:
            print("Invalid input. Try again!")
    return num

def create_screen():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle race!")

def create_turtles(colours):
    turtles = []
    for i in range(len(colours)):
        racer = turtle.Turtle()
        racer.shape("turtle")
        racer.color(colours[i])
        racer.penup()
        racer.left(90)
        racer.setpos(-WIDTH / 2 + (i + 1) * (WIDTH / (len(colours) + 1)), -HEIGHT / 2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles

def race(colours):
    turtles = create_turtles(colours)
    while True:
        for racer in turtles:
            racer.forward(randint(1,20))
            x,y=racer.pos()
            if y>=HEIGHT/2:
                sleep(2)
                return colours[turtles.index(racer)]

turtlenum = intro()
create_screen()
shuffle(COLOURS)
colours=COLOURS[:turtlenum]
winner = race(colours)
print(f"The {winner} turtle won the race!")
sleep(5)
