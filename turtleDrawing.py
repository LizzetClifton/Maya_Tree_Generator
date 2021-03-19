#in this file, I will experiment with a simple L-System using a common alphabet

#F: Draw a line and move forward
#G: Move forward without drawing a line
#+: Turn right
#-: Turn left
#[: Save current location
#]: Restore previous location

import turtle

#starting screen
s = turtle.getscreen()
newTurtle = turtle.Turtle()

distance = 25
angle = 60

axiom = "F++F++F"

gen = 0
desiredGenerations = 1
newInput = ""

def drawing(i):
    print("running drawing for: ", i)
    for char in i:
        if (char == "F"):
            newTurtle.forward(distance)
        elif (char == "G"):
            newTurtle.penup()
            newTurtle.forward(distance)
            newTurtle.pendown()
        elif (char == "+"):
            newTurtle.right(angle)
        elif (char =="-"):
            newTurtle.left(angle)

def nextGen(x):
    newX = ""
    print("x: ", x)
    for char in x:
        if (char == "F"):
            newX = newX + "F-F++F-F"
        elif (char == "G"):
            newX = newX + "G"
        elif (char == "+"):
            newX = newX + "+"
        elif (char =="-"):
            newX = newX + "-"
    # print("newX: ", newX)
    return newX

def run(j):
    print("running run for :", j)
    global gen
    global desiredGenerations
    global newInput
    while gen < desiredGenerations:
        print("we are on gen", gen)
        newInput = nextGen(j)
        print("newinput", newInput)
        gen = gen + 1
        run(newInput)
    print("double checking new input:", newInput)
    return newInput
        

drawing(run(axiom))

turtle.done()

#made dev branch
