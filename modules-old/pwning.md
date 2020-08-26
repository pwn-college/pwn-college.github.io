# Module: Memory Corruption

Because of the lack of memory safety in low-level languages, such as C, memory corruption vulnerabilities manifest quite frequently, to brutal effect.
This module will explore a number of different exploitation scenarios, using different types of flaws to achieve control over software.

## Slides

The slides for this module are:

- [Memory Corruption](https://docs.google.com/presentation/d/1_TY-uq1ddMDIgQTKep8xF5eHaP2XDUEmSBa3kszQu_A/edit?usp=sharing)

## Practice

The goal of the challenge sets in this module is to get the flag.
There is a `/flag` file, and you get to choose one binary on which the SUID flag will be set.

There are a number of difficulty levels, but the programs are structured similarly.
Each program takes user input on stdin and contains at least one (intentional) vulnerability.
If you exploit it, you can get it to read the flag and print it out to you.

The up-shot is this: to read the `/flag` for a binary, you will have to understand how to exploit it.

If you are ready to tackle the challenges, go to [https://ctf.pwn.college](https://ctf.pwn.college)!
