# Module: Shellcode Injection

Shellcoding is the art of injecting code into a program, usually during exploitation, to get it to carry out actions desired by the attacker \[[1](https://en.wikipedia.org/wiki/Shellcode)\].

## Lectures

This module consists of the following lectures:

- [Shellcoding: Introduction](https://youtu.be/715v_-YnpT8) (slides [here](https://docs.google.com/presentation/d/1kkfh-dhgxfIZPB1ziyW2JQiC1MbQWn8c7e24kOoDxJ4/edit#slide=id.g6c717ad36e_1_0))

Additionally, you should be quite familiar with the following fundamental knowledge:

- [Fundamentals: Computer Architecture](https://www.youtube.com/watch?v=9jc0eSnrzF4) (slides [here](https://docs.google.com/presentation/d/1sVyPL92gbzg_it9aIeC-CjXtF2tpvAmZTKjWc-SlU0c/edit?usp=sharing))
- [Fundamentals: Assembly](https://www.youtube.com/watch?v=ImdnOGNZflU) (slides [here](https://docs.google.com/presentation/d/1pN0nuhQIhn92QBitMznFNSRABDkMtbUW4MEJBYFwtwM/edit?usp=sharing))
- [Fundamentals: Binary Files](https://www.youtube.com/watch?v=nKqFeYJ483U) (slides [here](https://docs.google.com/presentation/d/1wrX8tvwaxIEk5hx4OtQmPqps-MScIaDO-9bTKQqr8vI/edit?usp=sharing))
- [Fundamentals: Linux Process Loading](https://www.youtube.com/watch?v=kUMCAzSOY-o) (slides [here](https://docs.google.com/presentation/d/1TwM5WLWnTqrNkpXjGKkaXYbKZEpatEQYA7ckBVXAOhs/edit?usp=sharing))
- [Fundamentals: Linux Process Execution](https://www.youtube.com/watch?v=Vtb5wIlthRg) (slides [here](https://docs.google.com/presentation/d/1ezY9Q8I0tzDD-7ZDXMbQM5RQ7z1dvB9-U_nDEhc6qdE/edit#slide=id.g8a9f5b81a5_0_0))

## Practice

You will practice on a set of generated challenges.
There is a `/flag` file, and you get to choose one binary on which the SUID flag will be set.

Each program takes your shellcode as input over stdin and will filter and execute your shellcode.
If your shellcode passes the filters and successfully runs, you can use it to read the `/flag` file.

If you are ready to tackle the challenges, go to [https://cse466.pwn.college](https://cse466.pwn.college)!
**NOTE: THE CHALLENGES WILL LAUNCH ON WEDNESDAY, SEPTEMBER 2ND! STAY TUNED!!!**

## Resources

Lots of external resources are referred to in the module videos.
Additionally, the following reading material is useful:

- [Wikipedia](https://en.wikipedia.org/wiki/Shellcode)
- [x86_64 assembly listing](http://ref.x86asm.net/coder64.html)
