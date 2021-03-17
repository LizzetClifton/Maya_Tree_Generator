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

This is what each generation would become.

Generation 0: a
Generation 1: aba
Generation 2: ababbaba
Generation 3: ababbababbbbababbaba
