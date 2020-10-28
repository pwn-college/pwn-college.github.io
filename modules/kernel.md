# Module: Kernel Security

Let's do a quick dive into the kernel to get familiar with the fundamental concepts.
We'll use these concepts to explore vulnerabilities in the kernel as part of the second combo module!

## Lectures

The lectures for this module are:

- [Kernel: Introduction](https://youtu.be/j0I2AakUAxk) (slides [here](https://docs.google.com/presentation/d/1oUaPUtLIDEMcK49gwvEMmXTyMBVQAeCWvSONV3OkIio/edit#slide=id.p))
- [Kernel: Environment Setup](https://youtu.be/mDn5IxMetgQ) (slides [here](https://docs.google.com/presentation/d/1Ik7EWjn_9ywzCW3MpJJ0eVdIvhIMP6brObBQQDtYDCo/edit#slide=id.p))
- [Kernel: Kernel Modules](https://youtu.be/DLWBWeN2ebM) (slides [here](https://docs.google.com/presentation/d/1JP1VBpK-kapHanMT4rAF9UtGglId_ZXD2Xh46gPQZFM/edit#slide=id.p))

## Practice

The goal of the challenge sets in this module is to get the flag.
Each challenge will lock you inside the userspace of an emulated system, and you will have to interact with the emulated kernel to get the flag.
There are a number of difficulty levels, and each challenge explores increasingly complex concepts in OS kernels.

If you are ready to tackle the challenges, go to [https://cse466.pwn.college](https://cse466.pwn.college)! **CHALLENGES GO LIVE ON 10/28/2020**

## Further Reading

- For interested students, we highly recommend reading the excellent [Linux Inside](https://0xax.gitbooks.io/linux-insides/content/) book!
- A [guide](https://www.kernel.org/doc/Documentation/dev-tools/gdb-kernel-debugging.rst) to debugging a kernel running in qemu from gdb.
- Our [kernel dev and pwn environment](https://github.com/pwncollege/pwnkernel).
- A much more feature-rich [kernel dev and pwn environment](https://github.com/cirosantilli/linux-kernel-module-cheat).
