# Maya Tree Generator Project

L-Systems have many uses, but the application relevant to this project is for generating realistic models of organic plant development and growth. In this project, I will be implementing a Stochastic L-System within a tree generator.

It is important to recognize that in the natural world, different parts of a plants grow at different rates and to varying sizes. For example, the branches of a tree will always be smaller and thinner than its trunk. 

# Lindenmayer Systems (L-Systems)

L-Systems are mathematical systems for using rules to rewrite and replace parts of an object in order to create a larger and more complex whole. You begin with one object and use your rules to change it every generation (iteration, frame, etc.). This is usually accomplished with recursion. 

Below, I will first explain the basic concept of L-Systems in a more painless way with an example for rewriting strings. If you are familiar with L-Systems, feel free to skip to the "My Project" section. 

An L-system for rewriting strings generally has the following components:

- An alphabet, which contains the allowed characters.
- An axiom, which is the character we start with.
- A rule set, which is the set of rules applied to each character each generation.

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

When we are dealing with graphical objects instead of strings, we would begin with an initiator (similar to the axiom) and a generator (similar to our rule set). In computer graphics, we can use something called turtle graphics to draw on a plane. These turtles draw on a canvas using directions from your program. In this repository, there is a file called snowflakeCurve.py where I implement a common graphical object known as a "Snowflake Curve" using an L-system and a turtle. Here you can see the construction of this curve.

![Snowflake Curve Construction](/snowflake.png?raw=true "Title")

As you can see, we are starting with an equilateral triangle as the initiator. The generator is a line with additional angles added in the middle. For this particular curve, we are replacing every line segment with the generator on every new generation. The first iteration after the initiator would create a hexagon, and the following generations would begin to create a snowflake shape.

### Context-Free vs. Context-Sensitive L-Systems

These types of L-Systems are what is called "context-free". This means that when each character is being translated, the rules don't take into account who its neighbors are or where it is in the string. The opposite is known as a context-sensitive L-System

### Deterministic vs. Stochastic L-Systems

If an L-System is deterministic, this means that there is always exactly one output for each input, in other words, there is one rule that will always occur for a given symbol.

In contrast, if a system is non-deterministic, or Stochastic, it means that there are several possible outputs for each symbol and an output is chosen based on probability. Stochastic systems utilize randomness and evolve over time, which makes them a good choice for creating outputs that resemble organic figures.

### Bracketed L-Systems

With L-Systems, brackets are typically used to represent branching. In an alphabet, the open bracket symbol, "[", signifies that the program should save the current location and orientation of the turtle (this would be the start of a new branch). The symbols between the brackets represent the parts of that branch. The closing bracket symbol, "]", signifies that the program should return to the last saved location. Essentially, this allows us to save a location, go off in a certain direction, come back to the saved location and go off in another direction (branching). A stack data structure is used in this case to store and pop the various states.


# References

"Lecture Notes in Biomathematics" by Przemyslaw Prusinkiewicz & James Hanan

https://jsantell.com/l-systems/ 

https://medium.com/@hhtun21/l-systems-draw-your-first-fractals-139ed0bfcac2

http://mypages.iit.edu/~maslanka/KochSnowflake.pdf 

https://help.autodesk.com/view/MAYAUL/2016/ENU/?guid=__files_GUID_B968733D_B288_4DAF_9685_4676DC3E4E94_htm

