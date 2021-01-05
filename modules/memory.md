# Module: Memory Errors

Because of the lack of memory safety in low-level languages, such as C, memory corruption vulnerabilities manifest quite frequently, to brutal effect.
This module will explore a number of different exploitation scenarios, using different types of flaws to achieve control over software.

## Lectures

The lectures for this module are:

- [Memory Errors: Introduction](https://youtu.be/z_XOhfsVKnU) (slides [here](https://docs.google.com/presentation/d/10cq3gCAvYjh_fzqiLLc1hCyqchux7x8pcskk6xGdVL8/edit#slide=id.p))
- [Memory Errors: High-level Problems](https://youtu.be/4PJvcZZIyT8) (slides [here](https://docs.google.com/presentation/d/1umxk_Gq_yGeCcBEz9toQ6Wil8G1bmK3NdrkFITadPhs/edit#slide=id.p))
- [Memory Errors: Smashing the Stack](https://youtu.be/PVx1hUlMxtQ) (slides [here](https://docs.google.com/presentation/d/1_Zs7s7O_VqXd8prv0GIjUT993qL3KgjVby8qC0Ixs_w/edit#slide=id.p))
- [Memory Errors: Causes of Corruption 1](https://www.youtube.com/watch?v=u80_j06HkpM) (slides [here](https://docs.google.com/presentation/d/1N5ybP1-SyU-PbQKMBRfFdNntbLPCOkROOybf_ZYBBBI/edit#slide=id.p))
- [Memory Errors: Causes of Corruption 2](https://www.youtube.com/watch?v=fVa2xahshik) (slides [here](https://docs.google.com/presentation/d/1N5ybP1-SyU-PbQKMBRfFdNntbLPCOkROOybf_ZYBBBI/edit#slide=id.p))
- [Memory Errors: Stack Canary Mitigations](https://youtu.be/55zWlEFflgE) (slides [here](https://docs.google.com/presentation/d/19bO811-RSjez-E8zGMJYvUwFi5jW-vRTv19z1g8ZT3I/edit#slide=id.p))
- [Memory Errors: ASLR Mitigations](https://youtu.be/SBqERAbDdAk) (slides [here](https://docs.google.com/presentation/d/1EOUvQsDsk5eg1Ysq9Us-CnLgCOP5IRIR8P6FThBVeGo/edit#slide=id.p))
- [Memory Errors: Causes of Disclosure](https://youtu.be/S9IIGVK6K0I) (slides [here](https://docs.google.com/presentation/d/1Qonbh98U_s3aN9Ut0dgdHFnm_ymb9e2yUqT6bkY4FbU/edit#slide=id.p))

The following lectures from previous modules are also quite relevant:

- [Shellcoding: Data Execution Prevention](https://www.youtube.com/watch?v=GH4NBLtPmyo) (slides [here](https://docs.google.com/presentation/d/1tH6jbnpX2_T5ZeDzZBfpLZ-ngpIZp3g25PPQaTr52JU/edit#slide=id.g6c717ad36e_1_0))

Additionally, you should be quite familiar with the following fundamental knowledge:

- [Fundamentals: Computer Architecture](https://www.youtube.com/watch?v=9jc0eSnrzF4) (slides [here](https://docs.google.com/presentation/d/1sVyPL92gbzg_it9aIeC-CjXtF2tpvAmZTKjWc-SlU0c/edit?usp=sharing))
- [Fundamentals: Assembly](https://www.youtube.com/watch?v=ImdnOGNZflU) (slides [here](https://docs.google.com/presentation/d/1pN0nuhQIhn92QBitMznFNSRABDkMtbUW4MEJBYFwtwM/edit?usp=sharing))
- [Fundamentals: Binary Files](https://www.youtube.com/watch?v=nKqFeYJ483U) (slides [here](https://docs.google.com/presentation/d/1wrX8tvwaxIEk5hx4OtQmPqps-MScIaDO-9bTKQqr8vI/edit?usp=sharing))
- [Fundamentals: Linux Process Loading](https://www.youtube.com/watch?v=kUMCAzSOY-o) (slides [here](https://docs.google.com/presentation/d/1TwM5WLWnTqrNkpXjGKkaXYbKZEpatEQYA7ckBVXAOhs/edit?usp=sharing))
- [Fundamentals: Linux Process Execution](https://www.youtube.com/watch?v=Vtb5wIlthRg) (slides [here](https://docs.google.com/presentation/d/1ezY9Q8I0tzDD-7ZDXMbQM5RQ7z1dvB9-U_nDEhc6qdE/edit#slide=id.g8a9f5b81a5_0_0))


## Practice

- Challenges: `babymem`

The goal of the challenge sets in this module is to get the flag.
There are a number of difficulty levels, but the programs are structured similarly.
Each program takes user input on stdin (or otherwise) and contains at least one (intentional) vulnerability.
If you exploit it, you can get it to read the flag and print it out to you.

The up-shot is this: to read the `/flag` for a binary, you will have to understand how to exploit it.

If you are ready to tackle the challenges, go to [https://cse466.pwn.college](https://cse466.pwn.college)!
