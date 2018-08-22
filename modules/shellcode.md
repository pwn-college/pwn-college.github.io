# Module: Shellcode Injection

Shellcoding is the art of injecting code into a program, usually during exploitation, to get it to carry out actions desired by the attacker \[[1](https://en.wikipedia.org/wiki/Shellcode)\].

## Slides

The slides for this module are:

- [Shellcoding!](https://docs.google.com/presentation/d/1isbgMuuauLrFxMaibi4Z8LCwQbgMszrMe12o0WvpyY0/edit?usp=sharing)

## Practice

You will practice on a set of generated challenges.
There is a `/flag` file, and you get to choose one binary on which the SUID flag will be set.

Each program takes your shellcode as input over stdin and will filter and execute your shellcode.
If your shellcode passes the filters and successfully runs, you can use it to read the `/flag` file.

## Resources

Useful resources:

- [Wikipedia](https://en.wikipedia.org/wiki/Shellcode)
- [x86_64 assembly listing](http://ref.x86asm.net/coder64.html)
