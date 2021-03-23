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
#making a turtle
newTurtle = turtle.Turtle()

#creating a distance variable (for moving forward)
distance = 25
#creating an angle variable (for turns)
angle = 60

#this is the string that we are starting with
axiom = "F++F++F"

#setting a counter for the generations
gen = 1
#setting a variable for how many generations we want to run
desiredGenerations = 4

#created a string variable to hold each generation's string
newInput = ""

#our drawing function. Here, we use the alphabet we identified earlier to define what actions our turtle needs to take for every character it comes across in the string
def drawing(i):
    for char in i:
        if (char == "F"):
            newTurtle.forward(distance)
        elif (char == "G"):
            #we are adding the pun up and down because we want this movement to be a translation without drawing
            newTurtle.penup()
            newTurtle.forward(distance)
            newTurtle.pendown()
        elif (char == "+"):
            newTurtle.right(angle)
        elif (char =="-"):
            newTurtle.left(angle)

#our function for translating the current string to the next generation based on our rules
def nextGen(x):
    #I added an empty string here because replacing and translating each character in the original string would be messy. this way, we can go through each character in the input, translate it, and add that to the new string "newX"
    newX = ""
    for char in x:
        if (char == "F"):
            newX = newX + "F-F++F-F"
        elif (char == "G"):
            newX = newX + "G"
        elif (char == "+"):
            newX = newX + "+"
        elif (char =="-"):
            newX = newX + "-"
    return newX

#our recursive function
def run(j):
    global gen
    global desiredGenerations
    #remember, newInput is the variable that will hold each generation's string
    global newInput
    while gen < desiredGenerations:
        #we are putting the value from our nextGen function into newInput
        newInput = nextGen(j)
        #incrementing gen variable
        gen = gen + 1
        #using recursion to run this function with the new input
        run(newInput)
    #checking if we only want to run this once (the axiom would not be translated)
    if (desiredGenerations == 1):
        return axiom
    #finally, we return newInput when our gen variable is equal to our desiredGen variable. We are returning newInput because this is the final string that we will feed into the drawing function
    return newInput

#calling our drawing function with the output of run(axiom) as the parameter 
drawing(run(axiom))

#finished with turtle
turtle.done()

#References: 
# https://opentechschool.github.io/python-beginners/en/simple_drawing.html#:~:text=%E2%80%9CTurtle%E2%80%9D%20is%20a%20python%20feature,can%20move%20the%20turtle%20around. 
# https://realpython.com/beginners-guide-python-turtle/#:~:text=turtle%20is%20a%20pre%2Dinstalled,gives%20the%20library%20its%20name.