# Concept: Position Independent Executables

Modern architectures have good support for Program Counter-relative addressing, which has enabled the use of Position-Independent Executables \[[2](https://en.wikipedia.org/wiki/Position-independent_code)\].
Information about underlying concepts is available online \[[1](http://www.codegurus.be/Programming/riprelativeaddressing_en.htm)\].
This page will cover the concept as it relates to hacking.

## Challenges of PIE

Since modern systems tend to [map memory](virtual_memory) at random locations, 
The biggest challenge of PIE is that _you don't know where anything is in memory_.
This presents two problems: you don't know _where_ to write, and you don't know _what_ to write.

### Problem: where to write

First, you must figure out where to write.
Depending on the [type of write primitive](write_types) you can leverage, this might or might not be hard:

- If you have an [overflow](write_types), the write itself doesn't need any knowledge of where you're writing: the data will get written onto the buffer you're overflowing!
- If you have a [relative write](write_types), then you can write into any adjacent data without having to know the actual location of that data.
- Otherwise, if you have an [absolute write](write_types), you will need to first leak the address of the executable using another vulnerability.

### Problem: what to write

If you solve the problem of _where_ to write, you must still understand _what_ to write.
In the context of PIE, there is a useful [exploitation technique](exploit_techniques): a **partial pointer overwrite** \[[4](http://ly0n.me/2015/07/30/bypass-aslr-with-partial-eip-overwrite/)\].
Because memory pages are always aligned to `0x1000` \[[3](virtual_memory)\], the three [least-significant nibbles](words) will always be the same, regardless of where the page is mapped.
Thus, you can overwrite the least-significant byte of a pointer with impunity to re-target that pointer to any other resource (such as a different instruction) that has the same other bytes as the pointer that you're overwriting.
This will always work, since that byte is always the same.
You can also overwrite _two_ bytes (four nibbles), giving you more options to re-target the pointer at.
This is more risky: because the most significant nibble you overwrite is _not_ fixed, and you must overwrite it (as memory writtes typically happen on a byte-by-byte basis, not nibble-by-nibble or bit-by-bit), you have to take a guess for a value to overwrite it with and brute-force it.
Your guess will match the actual value in memory one out of 16 times (the number of values, 0x0 through 0xf, that a nibble can hold), and your exploit will work.

## References

- \[1\] [http://www.codegurus.be/Programming/riprelativeaddressing_en.htm](http://www.codegurus.be/Programming/riprelativeaddressing_en.htm)
- \[2\] [https://en.wikipedia.org/wiki/Position-independent_code](https://en.wikipedia.org/wiki/Position-independent_code)
- \[3\] [virtual_memory](virtual_memory)
- \[4\] [http://ly0n.me/2015/07/30/bypass-aslr-with-partial-eip-overwrite/](http://ly0n.me/2015/07/30/bypass-aslr-with-partial-eip-overwrite/)
