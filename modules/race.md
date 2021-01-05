# Module: Race Conditions

This module explores the bugs and vulnerabilities arising from incorrect handling of concurrency, and other related issues.

## Lectures

The lectures for this module are:

- [Race Conditions: Introduction](https://youtu.be/jXQ8Y5B2sc0) (slides [here](https://docs.google.com/presentation/d/1cwaI8mwYBAj_GBrDqfCHM4_ansWHlkT5tBIFo8zJqsI/edit))
- [Race Conditions: Races in the Filesystem](https://youtu.be/dpsWLu8jxBg) (slides [here](https://docs.google.com/presentation/d/1aMSJoBqDIY0cYwFwEa4uq4mzjScGzZDFbmkvVcrbF-4/edit))
- [Race Conditions: Processes and Threads](https://youtu.be/_hDP1wZKkaI) (slides [here](https://docs.google.com/presentation/d/11Fq9HwG6yYB9fkEJ-ZJ4kHbu-hL4WizAiUoX9prPN8Y/edit))
- [Race Conditions: Races in Memory](https://youtu.be/jNIgU4kI6wY) (slides [here](https://docs.google.com/presentation/d/1u-aSz-mqwkMIZEDAR-AEPKw5JPn-1q_3Ek_C6JjQUzY/edit))
- [Race Conditions: Signals and Reentrancy](https://youtu.be/bPWQFhsUkbs) (slides [here](https://docs.google.com/presentation/d/1LOmzo79U_QmdggdfQwDej47886iqHIPDGXpl506_SYY/edit))

## Practice

- Challenges: `babyrace`

Again, you will practice on a set of generated challenges.
There is a `/flag` file, and you get to choose one binary on which the SUID flag will be set.

Each program will be vulnerable to some sort of race condition.
You can subvert the program by cleverly taking advantage of concurrency mishandling.
If you are successful, you can use it to read the `/flag` file.

If you are ready to tackle the challenges, go to [https://cse466.pwn.college](https://cse466.pwn.college)!
