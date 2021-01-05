# Module: Dynamic Allocator Misuse

This module explores the abuse of heap operations and heap datastructures during exploitation.

## Lectures

The lectures for this module are:

- [Dynamic Allocator Misuse: What is the Heap?](https://youtu.be/coAJ4KyrWmY) (slides [here](https://docs.google.com/presentation/d/16XMoNQQB_jP0odRvQFhgMi3Neo9VR0g1jBvBXKYBnh0/edit))
- [Dynamic Allocator Misuse: Dangers of the Heap](https://youtu.be/Cr9IeGQxFoc) (slides [here](https://docs.google.com/presentation/d/1T5XruKzTxlpslT50op_wxvFsnsa4gshIM0Tue1f8zc4/edit))
- [Dynamic Allocator Misuse: tcache](https://youtu.be/0jHtqqdVv1Y) (slides [here](https://docs.google.com/presentation/d/13NbUlNvj1Rm-Cc_E_Crp678c-mgzCi0BYfzXIzFB3zI/edit))
- [Dynamic Allocator Misuse: Chunks and Metadata](https://youtu.be/osFevdDR0Xw) (slides [here](https://docs.google.com/presentation/d/1BlapIDslDaWeBPUamdG0i35-yveGvWJHZaW_0dan6sU/edit))
- [Dynamic Allocator Misuse: Metadata Corruption](https://youtu.be/PtpPcGcX020) (slides [here](https://docs.google.com/presentation/d/14SYq0TTVxEGWHNUG1BP66A8liPDD2pqJUs2WrXlCZNE/edit))

## Practice

- Challenges: `babyheap`

Again, you will practice on a set of generated challenges.
There is a `/flag` file, and you get to choose one binary on which the SUID flag will be set.

Each program will misuse the heap in some way.
You can subvert the program functionality through this misuse.
If you are successful, you can use it to read the `/flag` file.

If you are ready to tackle the challenges, go to [https://cse466.pwn.college](https://cse466.pwn.college)!

## Further reading

- Documentation about [malloc internals](https://sourceware.org/glibc/wiki/MallocInternals).
- A repository with heap misuse examples: [how2heap](https://github.com/shellphish/how2heap).
