#this file will be my first python experimentation with drawing bracketed l-systems

import turtle
from collections import deque

s = turtle.getscreen()
newTurtle = turtle.Turtle()
newTurtle.speed(3)
newTurtle.setheading(90)
axiom = "F"
rules = {"F" : "G[+F]-F",
         "G" : "GG", #G is also for moving forward, but it wont be replaced by F's rule
         "+" : "+",  
         "-" : "-",
         "[" : "[",
         "]" : "]"}
gen = 1 
desiredGenerations = 6
distance = 15
angle = 30

stack = deque()

#will hold each generation's string
newInput = ""

def drawing(i):
    for char in i:
        if (char == "F"):
            newTurtle.pencolor("green")
            newTurtle.forward(distance)
        elif (char == "G"):
            newTurtle.pencolor("black")
            newTurtle.forward(10)
        elif (char == "+"):
            newTurtle.right(angle)
        elif (char =="-"):
            newTurtle.left(angle)
        elif (char =="["):
            #save position, push to stack
            currentState = [newTurtle.pos(), newTurtle.heading()]
            stack.append(currentState)
        elif (char =="]"):
            #return to position, pop
            oldState = stack.pop()
            newTurtle.penup()
            newTurtle.setpos(oldState[0])
            newTurtle.setheading(oldState[1])
            newTurtle.pendown()

def nextGen(x):
    newX = ""
    for char in x:
        newX = newX + rules.get(char)
    return newX

def run(j):
    global gen
    global desiredGenerations
    global newInput
    if (desiredGenerations == 1):
        return axiom
    while gen < desiredGenerations:
        newInput = nextGen(j)
        gen = gen + 1
        run(newInput)
    return newInput
 
drawing(run(axiom))

turtle.done()