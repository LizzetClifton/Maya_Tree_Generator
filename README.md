# Maya Tree Generator Project

L-Systems have many uses, but the application relevant to this project is for generating realistic models of organic plant development and growth. In this project, I will be implementing a Stochastic L-System as a tree generator.

Below, I will explain the concepts I researched in order to create this project.

# Lindenmayer Systems (L-Systems)

L-Systems are mathematical systems that use rules to replace parts of an initial object every generation (iteration, frame, etc.). This creates a larger and more complex whole, and is usually accomplished with recursion. I will illustrate this concept with an example of an L-System for rewriting strings.

An L-system for rewriting strings generally has the following components:

- An alphabet, which contains the allowed characters.
- An axiom, which is the character we begin with.
- A rule set, which is the set of rules applied to each character(s) each generation.

For example:

Say our axiom is the letter "a", and we have two rules. 
- a --> aba (meaning that the character "a" will become the string "aba" the next generation)
- b --> bb (meaning that the character "b" will become the string "bb" the next generation)

This is what each generation would be. Note that generation 0 is "a" because that is our axiom.

- Generation 0: a
- Generation 1: aba
- Generation 2: ababbaba
- Generation 3: ababbababbbbababbaba

When we apply the rules to generation 0, "a" becomes "aba". In the next generation, we apply our rules to "aba", with the first "a" becoming "aba", the "b" becoming "bb" and the second "a" becoming "aba". Thus, we end up with "ababbaba" for generation 2. This continues for any number of desired generations.

-------

L-Systems for rewriting strings are different than those for replacing parts of a visual or graphical object. When we deal with L-Systems for graphical objects, we begin with an initiator (similar to the axiom) and a generator (similar to our rule set). With these systems, each new generation will apply the generator to an image, as I will show below.

In computer graphics, we can use something called turtle graphics to draw on a plane using directions from a program. In this repository, there is a file called snowflakeCurve.py where I implement a common graphical object known as a "Snowflake Curve" using an L-system and a turtle. Here you can see the construction of this curve.

![Snowflake Curve Construction](/snowflake.png?raw=true "Title")

As you can see, we are starting with an equilateral triangle as the initiator. The generator is a line with additional angles added in the middle. For this particular curve, we are replacing every line segment with the generator on every new generation. The first iteration after the initiator would create a hexagon, and the following generations would begin to create a snowflake shape.

### Context-Free vs. Context-Sensitive L-Systems

These types of L-Systems are what is called "context-free". This means that when each character is being translated, the rules don't take into account who its neighbors are or where it is in the string. The opposite is known as a context-sensitive L-System

### Deterministic vs. Stochastic L-Systems

If an L-System is Deterministic, this means that there is always exactly one output for each input, in other words, there is one rule that will always occur for a given symbol.

In contrast, if a system is Non-Deterministic, or Stochastic, it means that there are several possible outputs for each symbol and an output is chosen based on probability. Stochastic systems utilize randomness and evolve over time, which makes them a good choice for creating outputs that resemble organic figures.

### Bracketed L-Systems

With L-Systems, brackets in an alphabet are typically used to represent branching. The open bracket symbol, "[", signifies that the program should save the current location and orientation of the turtle (this would be the start of a new branch). The closing bracket symbol, "]", signifies that the program should return to the last saved location. The symbols between the brackets represent the parts of that branch. Essentially, this allows us to save a location as the start of a branch, go off in a certain direction, come back to the saved location and go off in another direction (branching). A stack data structure is used in this case to store and pop the various states.

Let's assume we have the following alphabet:

- "F" : Draw a line and move forward
- "+" : Turn right
- "-" : Turn left
- "[" : Store location and orientation of turtle
- "]" : Pop the location and orientation of the turtle

If we had a string like this "F[+F]-F", this would read as "move forward, save your location, turn right, move forward, return to your old location, turn left, move forward" and it would result in what looks like a line with two branches.

# References

"Lecture Notes in Biomathematics" by Przemyslaw Prusinkiewicz & James Hanan

https://jsantell.com/l-systems/ 

https://medium.com/@hhtun21/l-systems-draw-your-first-fractals-139ed0bfcac2

http://mypages.iit.edu/~maslanka/KochSnowflake.pdf 

https://help.autodesk.com/view/MAYAUL/2016/ENU/?guid=__files_GUID_B968733D_B288_4DAF_9685_4676DC3E4E94_htm

