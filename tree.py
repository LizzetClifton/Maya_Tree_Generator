#this file will be my first python experimentation with drawing bracketed l-systems

import turtle

s = turtle.getscreen()

axiom = "F++F++F"

rules = {"F" : "F-F++F-F",  
         "+" : "+",  
         "-" : "-",
         "[" : "",
         "]" : ""}

gen = 1 
desiredGenerations = 3

#will hold each generation's string
newInput = ""

def drawing(i):
    for char in i:
        if (char == "F"):
            newTurtle.forward(distance)
        elif (char == "+"):
            newTurtle.right(angle)
        elif (char =="-"):
            newTurtle.left(angle)
        elif (char =="["):
            #save position, push to stack
            push()
        elif (char =="]"):
            #return to position, pop
            pop()

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