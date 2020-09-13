# Module: Sandboxing

The slides for this module are:

- [Sandboxing: Introduction](https://youtu.be/Ide_eg-eQZ0) (slides [here](https://docs.google.com/presentation/d/1TpMjTimroiC3Jm0dsteHWEUw06yZ5Oh7iM8YBmbOUkI/edit))
- [Sandboxing: chroot](https://youtu.be/C81lO7pG5aA) (slides [here](https://docs.google.com/presentation/d/1AWl9Gko_L1kDLBtrTFB3EohQU4vQjykpQE5dm9uxYi0/edit))
- [Sandboxing: seccomp](https://www.youtube.com/watch?v=hrT1xvxGKS4) (slides [here](https://docs.google.com/presentation/d/1jOTktFSo-TwQklYdsOyC3f-2ba8XuJA8ZFWHjMQyQVI/edit))
- [Sandboxing: Escaping seccomp](https://www.youtube.com/watch?v=h1L9mF6PHlQ) (slides [here](https://docs.google.com/presentation/d/1tkBhW2JG-_jRaRDwSpuUYdT-Dg-odtZTdqanQu8vqow/edit))

Additionally, you should be quite familiar with the following fundamental knowledge:

- [Fundamentals: Linux Process Execution](https://www.youtube.com/watch?v=Vtb5wIlthRg) (slides [here](https://docs.google.com/presentation/d/1ezY9Q8I0tzDD-7ZDXMbQM5RQ7z1dvB9-U_nDEhc6qdE/edit#slide=id.g8a9f5b81a5_0_0))

## Practice


Again, you will practice on a set of generated challenges.
Each challenge will sandbox you to protect the flag.
If you can escape the sandbox, you can use read the `/flag` file and score!

If you are ready to tackle the challenges, go to [https://cse466.pwn.college](https://cse466.pwn.college)!

## Errata

Some tips and tricks for the challenge problems!

- Be very careful to understand the timeline of what the challenge does. A file opened BEFORE `chroot()` is very different from a file opened AFTER `chroot()`. The sequence of actions makes a big difference.
- There aren't any restrictions on shellcode (other than syscalls), so we highly recommend making sure your shellcode exits cleanly. That will make it easier to debug.
- You can determine the value of constants such as `AT_FDCWD` by writing a quick C program that includes the relevant header files and does `printf("%d\n", AT_FDCWD);`.
- `chroot()` will fail if you're not running as root. `strace` causes the SUID bit to be ignored, so you must use `sudo strace` to properly trace these challenges. Of course, this will only be possible in practice mode.
- There is a known issue with strace that, in certain configurations, it will improperly resolve the syscall number of 32-bit syscalls in amd64. Using a newer Linux VM sometimes helps. If you're using `int 0x80` to trigger system calls, the 32-bit ones ARE being used; strace is just lying to you.
- On the subject of 32-bit syscalls: you do not have to assemble your shellcode in 32-bit mode (i.e., you don't need `-m32`). It is perfectly valid to just up and `int 0x80` in the middle of an otherwise-64-bit shellcode.
- Read [this](https://www.gnu.org/software/bash/manual/html_node/Redirections.html) thoroughly, especially Section 3.6.1.
