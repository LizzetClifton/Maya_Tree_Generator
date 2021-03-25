# Maya_Tree_Generator

## Lindenmayer Systems (L-Systems)

L-Systems are mathematical systems for using rules to rewrite and replace parts of an object in order to create a larger and more complex whole. You begin with one object and use your rules to change it every generation (iteration, frame, etc.). This is usually accomplished with recursion. 

I will demonstrate the basic concept of L-Systems in a more painless way with an example for rewriting strings. An L-system for rewriting strings generally has the following components:

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

### Context-Free vs. Context-Sensitive L-Systems

These types of L-Systems are what is called "context-free". This means that when each character is being translated, the rules don't take into account who its neighbors are or where it is in the string. The opposite is known as a context-sensitive L-System

### Deterministic vs. Non-Deterministic L-Systems

If an L-System is deterministic, this means that there is always exactly one output for each symbol.

In contrast, non-deterministic L-Systems, or Stochastic systems, means that there are several possible outputs for each symbol and each output has a probability of being chosen. These systems usually create outputs that resemble organic figures.

### Bracketed L-Systems

### My Project

In this project, I will be implementing a Stochastic L-System within a tree generator. 

## My Project

L-Systems have many uses, but the application relevant to this project is for generating realistic models of organic plant development and growth. 

When we are dealing with graphical objects instead of strings, we would begin with an initiator (similar to the axiom) and a generator (similar to our rule set). In this repository, there is a file called snowflakeCurve.py where I implement a common graphical object known as a "Snowflake Curve" using an L-system. Here you can see the construction of this curve.

![Snowflake Curve Construction](/snowflake.png?raw=true "Title")

As you can see, we are starting with an equilateral triangle as the initiator. The generator is a line with additional angles added in the middle. For this particular curve, we are replacing every line segment with the generator on every new generation. The first iteration after the initiator would create a hexagon, and the following generations would begin to create a snowflake shape.

### References

"Lecture Notes in Biomathematics" by Przemyslaw Prusinkiewicz & James Hanan

https://jsantell.com/l-systems/ 

https://medium.com/@hhtun21/l-systems-draw-your-first-fractals-139ed0bfcac2

