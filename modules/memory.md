# Module: Memory Errors

Because of the lack of memory safety in low-level languages, such as C, memory corruption vulnerabilities manifest quite frequently, to brutal effect.
This module will explore a number of different exploitation scenarios, using different types of flaws to achieve control over software.

## Slides

The slides for this module are:

- [Memory Errors: Introduction](https://youtu.be/z_XOhfsVKnU) (slides [here](https://docs.google.com/presentation/d/10cq3gCAvYjh_fzqiLLc1hCyqchux7x8pcskk6xGdVL8/edit#slide=id.p))
- [Memory Errors: High-level Problems](https://youtu.be/4PJvcZZIyT8) (slides [here](https://docs.google.com/presentation/d/1umxk_Gq_yGeCcBEz9toQ6Wil8G1bmK3NdrkFITadPhs/edit#slide=id.p))
- **COMING SOON** [Memory Errors: Smashing the Stack]() (slides [here]())
- **COMING SOON** [Memory Errors: Signedness Mixups]() (slides [here]())
- **COMING SOON** [Memory Errors: Off-by-one Errors]() (slides [here]())
- **COMING SOON** [Memory Errors: Termination Problems]() (slides [here]())
- **COMING SOON** [Memory Errors: NX Mitigations]() (slides [here]())
- **COMING SOON** [Memory Errors: ASLR Mitigations]() (slides [here]())
- **COMING SOON** [Memory Errors: Stack Canary Mitigations]() (slides [here]())

Additionally, you should be quite familiar with the following fundamental knowledge:

- [Fundamentals: Computer Architecture](https://www.youtube.com/watch?v=9jc0eSnrzF4) (slides [here](https://docs.google.com/presentation/d/1sVyPL92gbzg_it9aIeC-CjXtF2tpvAmZTKjWc-SlU0c/edit?usp=sharing))
- [Fundamentals: Assembly](https://www.youtube.com/watch?v=ImdnOGNZflU) (slides [here](https://docs.google.com/presentation/d/1pN0nuhQIhn92QBitMznFNSRABDkMtbUW4MEJBYFwtwM/edit?usp=sharing))
- [Fundamentals: Binary Files](https://www.youtube.com/watch?v=nKqFeYJ483U) (slides [here](https://docs.google.com/presentation/d/1wrX8tvwaxIEk5hx4OtQmPqps-MScIaDO-9bTKQqr8vI/edit?usp=sharing))
- [Fundamentals: Linux Process Loading](https://www.youtube.com/watch?v=kUMCAzSOY-o) (slides [here](https://docs.google.com/presentation/d/1TwM5WLWnTqrNkpXjGKkaXYbKZEpatEQYA7ckBVXAOhs/edit?usp=sharing))
- [Fundamentals: Linux Process Execution](https://www.youtube.com/watch?v=Vtb5wIlthRg) (slides [here](https://docs.google.com/presentation/d/1ezY9Q8I0tzDD-7ZDXMbQM5RQ7z1dvB9-U_nDEhc6qdE/edit#slide=id.g8a9f5b81a5_0_0))


## Practice

The goal of the challenge sets in this module is to get the flag.
There are a number of difficulty levels, but the programs are structured similarly.
Each program takes user input on stdin (or otherwise) and contains at least one (intentional) vulnerability.
If you exploit it, you can get it to read the flag and print it out to you.

The up-shot is this: to read the `/flag` for a binary, you will have to understand how to exploit it.

If you are ready to tackle the challenges, go to [https://cse466.pwn.college](https://cse466.pwn.college)!
