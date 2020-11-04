# Module: Dynamic Allocator Misuse

This module explores the abuse of heap operations and heap datastructures during exploitation.

## Slides

The slides for this module are:

- [Dynamic Allocator Misuse: What is the Heap?]() (slides [here](https://docs.google.com/presentation/d/16XMoNQQB_jP0odRvQFhgMi3Neo9VR0g1jBvBXKYBnh0/edit))
- [Dynamic Allocator Misuse: Dangers of the Heap]() (slides [here](https://docs.google.com/presentation/d/1T5XruKzTxlpslT50op_wxvFsnsa4gshIM0Tue1f8zc4/edit))
- [Dynamic Allocator Misuse: tcache]() (slides [here](https://docs.google.com/presentation/d/13NbUlNvj1Rm-Cc_E_Crp678c-mgzCi0BYfzXIzFB3zI/edit))

## Practice

Again, you will practice on a set of generated challenges.
There is a `/flag` file, and you get to choose one binary on which the SUID flag will be set.

Each program will misuse the heap in some way.
You can subvert the program functionality through this misuse.
If you are successful, you can use it to read the `/flag` file.

If you are ready to tackle the challenges, go to [https://cse466.pwn.college](https://cse466.pwn.college)!