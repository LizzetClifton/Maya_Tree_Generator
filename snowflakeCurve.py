#in this file, I will implement a Koch Snowflake Curve using an L-System

#F: Draw a line and move forward
#+: Turn right
#-: Turn left

import turtle

s = turtle.getscreen()
newTurtle = turtle.Turtle()

distance = 25 #length of forward move
angle = 60 #angle for turns

#the string that we are starting with
axiom = "F++F++F"

#creating a dictionary that will store the rules.
rules = {"F" : "F-F++F-F",  
         "+" : "+",  
         "-" : "-"}

gen = 1 #counter for the generation we are on
desiredGenerations = 3 #variable for how many generations we want to run

#will hold each generation's string
newInput = ""

#here, we use the alphabet we identified earlier to define what actions our turtle needs to take for every character it comes across in the string
def drawing(i):
    for char in i:
        if (char == "F"):
            newTurtle.forward(distance)
        elif (char == "+"):
            newTurtle.right(angle)
        elif (char =="-"):
            newTurtle.left(angle)

#function for translating the current string to the next generation based on our rules
def nextGen(x):
    #I added an empty string here because replacing and translating each character in the original string would be messy. this way, we can go through each character in the input, translate it using the dictionary, and add that to the new string "newX"
    newX = ""
    for char in x:
        newX = newX + rules.get(char)
    return newX

#our recursive function
def run(j):
    global gen
    global desiredGenerations
    #remember, newInput is the variable that will hold each generation's string
    global newInput
    #checking if we only want to run this once (the axiom would not be translated)
    if (desiredGenerations == 1):
        return axiom
    while gen < desiredGenerations:
        newInput = nextGen(j)
        gen = gen + 1
        run(newInput)
    #we return newInput when our gen variable is equal to our desiredGen variable because this is the final string that we will feed into the drawing function
    return newInput
 
drawing(run(axiom))
turtle.done()

#References: 
# https://opentechschool.github.io/python-beginners/en/simple_drawing.html#:~:text=%E2%80%9CTurtle%E2%80%9D%20is%20a%20python%20feature,can%20move%20the%20turtle%20around. 
# https://realpython.com/beginners-guide-python-turtle/#:~:text=turtle%20is%20a%20pre%2Dinstalled,gives%20the%20library%20its%20name.