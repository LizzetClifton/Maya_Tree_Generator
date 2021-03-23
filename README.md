# Maya_Tree_Generator

## Lindenmayer Systems (L-Systems)

A way to generate fractal patterns, conceived as a mathematical theory of plant development/ bacteria growth.

I am choosing to use these so that I can simulate this organic growth.

With L-systems, you are using recursion to apply a set of rules to a string of symbols. With each iteration, the rules are applied to each character, resulting in new characters.

An L-system has the following components:

- An alphabet, which are the characters that are allowed.
- An axiom, which is the character we start with. The character at generation 0.
- A rule set, which is the set of rules applied to each character each iteration.

For example:

Say our axiom is the letter "a", and we have two rules. The first rule is a --> aba
The second rule is b --> bb

This is what each generation would become (the generations below are spaced out for visual purposes)

Generation 0: a
Generation 1: aba
Generation 2: aba bb aba
Generation 3: aba bb aba bb bb aba bb aba

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