# Maya_Tree_Generator

## Lindenmayer Systems (L-Systems)

L-Systems have many uses, but the application relevant to this project is for generating realistic models of organic plant development and growth.

With L-systems, you are using simple rules to rewrite and replace parts of an object in order to create a larger and more complex whole. This is usually accomplished with recursion. I will explain this concept with an example for rewriting strings.

An L-system for rewriting strings generally has the following components:

- An alphabet, which contains the allowed characters.
- An axiom, which is the character we start with.
- A rule set, which is the set of rules applied to each character each generation.

For example:

Say our axiom is the letter "a", and we have two rules. 
- The first rule is a --> aba (meaning that the character "a" will become the string "aba" the next generation)
- The second rule is b --> bb (meaning that the character "b" will become the string "bb" the next generation)

This is what each generation would become
- Generation 0: a
- Generation 1: aba
- Generation 2: ababbaba
- Generation 3: ababbababbbbababbaba

When we are dealing with graphical objects instead of strings, we would begin with an initiator (similar to the axiom) and a generator (our rule set). In this repository, there is a file called turtleDrawing.py where I implement a common graphical object known as a "Snowflake Curve"using an L-system. Here you can see the construction of this curve.

![Snowflake Curve Construction](/snowflake.png?raw=true "Title")

As you can see, we are starting with an equilateral triangle as the initiator. The generator is a line with additional angles added in the middle. For this particular curve, we are replacing every line segment with the generator. The first iteration would create a hexagon, and the following generations would begin to create a snowflake shape.

### Context-Free vs. Context-Sensitive L-Systems

These types of L-Systems are what is called "context-free". This means that when each character is being translated, the rules don't take into account who its neighbors are or where it is in the string. The opposite is known as a context-sensitive L-System

### Deterministic vs. Non-Deterministic L-Systems

If an L-System is deterministic, this means that there is always exactly one output for each symbol.

In contrast, non-deterministic L-Systems, or Stochastic systems, means that there are several possible outputs for each symbol and each output has a probability of being chosen. These systems usually create outputs that resemble organic figures.

### Bracketed L-Systems

### My Project

In this project, I will be implementing a Stochastic L-System within a tree generator. 

### References

https://jsantell.com/l-systems/ 

https://medium.com/@hhtun21/l-systems-draw-your-first-fractals-139ed0bfcac2
