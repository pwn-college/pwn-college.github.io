# Concept: Virtual Memory

Modern architectures use _virtual memory_ to separate process memory spaces.
There are a number of resources online to catch up on the basics \[[1](https://en.wikipedia.org/wiki/Paging),[2](https://www.tldp.org/LDP/tlk/mm/memory.html)\].
This page deals with virtual memory concepts relevant to cybersecurity.

## Mapping Memory

Memory is mapped in a number of ways:

- By applications, using the `mmap` family of system calls.
- By the [program loader](loader), using `mmap` to map programs into memory.
- By the kernel, when allocating space for the stack and other necessary parts of a process.

In modern systems, most allocations are at _random_ addresses for security purposes (see \[[3](https://en.wikipedia.org/wiki/Address_space_layout_randomization)\]).
Fixed addresses are still used for two purposes:

- When loading programs that are not [Position Independent](pie) into memory.
- To map memory at a specific address due to custom application behavior.

Fixed mapping is accomplished by passing the `MAP_FIXED` argument to `mmap` or `mmap2` \[[4](http://man7.org/linux/man-pages/man2/mmap.2.html)\].

## Memory Pages

Memory is mapped in _pages_ \[[5](https://en.wikipedia.org/wiki/Page_(computer_memory))\].
Normal pages are `0x1000` bytes (4096 in decimal) in size, though other sizes are possible \[[6](https://en.wikipedia.org/wiki/Page_(computer_memory)#Multiple_page_sizes)\].

Aside from being `0x1000` in size, pages are also aligned to `0x1000`.
That is, the base address of any page will _always_ end in three null [nibbles](words).
For example, potential page addresses are:

- `0x00007ffcff1b1000` (library code is frequently mapped at `0x7f`-something)
- `0x55ea43e0b000` ([PIE](pie) executables are typically loaded at `0x55`-something)
- `0x555555554000` (the base address that [GDB](debuggers) uses when use it to load a PIE executable)
- `0xffffffffff600000` (typical location of `vsyscall`, a page that is shared between the [kernel](kernel) and program for performance reasons \[[7](https://lwn.net/Articles/446528/)\])

You can look at what pages a process has mapped by doing:

- `cat /proc/$PID/maps` with the process' [PID](pid)
- `pmap $PID` with the process' PID
- `info proc maps` inside GDB

## Weaknesses in Page Address Selection

While modern systems tend to map pages at random locations, recent research has shed light on a problem: the random location is chosen _once per process_, and, by default, other pages tend to be mapped contiguously to that location \[[10](https://github.com/kirschju/wiedergaenger)\].
This is a problem for all [shared libraries](libraries), and many other types of mapped pages, though typically, the main [PIE](pie) binary itself does *not* have this issue.

At any rate, this enables a set of potential attacks:

- Having a leak in one library (or many other types of pages) exposes the addresses of _all_ libraries.
- Having a [controlled relative write](write_types) relative to a library location allows you to influence data in any library (along with other allocated data).

## Page Permissions

Modern operating systems are careful about protecting process memory \[[8](https://en.wikipedia.org/wiki/Memory_protection)\].
Each page has three permission bits:

- `PROT_READ`, which determines whether the process can access memory in the page
- `PROT_WRITE`, which determines whether the process can write memory in the page
- `PROT_EXEC`, which determines whether the process can execute memory in the page

A page that is both writable and executable could allow an attacker to perform inject and execute [shellcode](shellcode).
Page permissions can be modified with `mprotect` \[[9](http://man7.org/linux/man-pages/man2/mprotect.2.html)\].

## Resources

- \[1\] [https://en.wikipedia.org/wiki/Paging](https://en.wikipedia.org/wiki/Paging)
- \[2\] [https://www.tldp.org/LDP/tlk/mm/memory.html](https://www.tldp.org/LDP/tlk/mm/memory.html)
- \[3\] [https://en.wikipedia.org/wiki/Address_space_layout_randomization](https://en.wikipedia.org/wiki/Address_space_layout_randomization)
- \[4\] [http://man7.org/linux/man-pages/man2/mmap.2.html](http://man7.org/linux/man-pages/man2/mmap.2.html)
- \[5\] [https://en.wikipedia.org/wiki/Page_(computer_memory)](https://en.wikipedia.org/wiki/Page_(computer_memory))
- \[6\] [https://en.wikipedia.org/wiki/Page_(computer_memory)#Multiple_page_sizes](https://en.wikipedia.org/wiki/Page_(computer_memory)#Multiple_page_sizes)
- \[7\] [https://lwn.net/Articles/446528/](https://lwn.net/Articles/446528/)
- \[8\] [https://en.wikipedia.org/wiki/Memory_protection](https://en.wikipedia.org/wiki/Memory_protection)
- \[9\] [http://man7.org/linux/man-pages/man2/mprotect.2.html](http://man7.org/linux/man-pages/man2/mprotect.2.html)
- \[10\] [https://github.com/kirschju/wiedergaenger](https://github.com/kirschju/wiedergaenger)
