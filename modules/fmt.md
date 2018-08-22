# Module: Format Strings

This module is an exploration of what can go wrong when unsanitized attacker input is processed by _string formatting_ functions.

## Slides

The slides for this module are:

- [Format Strings](https://docs.google.com/presentation/d/1RKxlfzff0mZdp-98dNfAMOOa1wQLSK9UN7Nh4E1GlNY/edit?usp=sharing)

## Practice


Again, you will practice on a set of generated challenges.
There is a `/flag` file, and you get to choose one binary on which the SUID flag will be set.

Each program takes user input and will eventually printf() it.
You can subvert the program functionality by injecting a malicious format string.
If you are successful, you can use it to read the `/flag` file.
