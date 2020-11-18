# Module: Race Conditions

This module explores the bugs and vulnerabilities arising from incorrect handling of concurrency, and other related issues.

## Slides

The slides for this module are:

- [Race Conditions: Introduction](https://youtu.be/jXQ8Y5B2sc0) (slides [here](https://docs.google.com/presentation/d/1cwaI8mwYBAj_GBrDqfCHM4_ansWHlkT5tBIFo8zJqsI/edit))
- [Race Conditions: Races in the Filesystem](https://youtu.be/dpsWLu8jxBg) (slides [here](https://docs.google.com/presentation/d/1aMSJoBqDIY0cYwFwEa4uq4mzjScGzZDFbmkvVcrbF-4/edit))

## Practice

Again, you will practice on a set of generated challenges.
There is a `/flag` file, and you get to choose one binary on which the SUID flag will be set.

Each program will be vulnerable to some sort of race condition.
You can subvert the program by cleverly taking advantage of concurrency mishandling.
If you are successful, you can use it to read the `/flag` file.

If you are ready to tackle the challenges, go to [https://cse466.pwn.college](https://cse466.pwn.college)! **CHALLENGES WILL LAUNCH ON 11/18**
