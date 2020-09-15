# Module: Binary Reverse Engineering

This module is an introduction to reverse engineering of binary code.
Oftentimes, developers pack secret information into binary code, assuming that it is safe there.
You will prove that this assumption is flawed.

## Slides

This module consists of the following lectures:

- [Reverse Engineering: Introduction]() (slides [here](https://docs.google.com/presentation/d/1hw_STBTJh4xqMv4TZAPRqt2rYIEAXXaCQlaBetxUufU/edit))
- [Reverse Engineering: Functions and Frames]() (slides [here](https://docs.google.com/presentation/d/125gIw6rNKvwa-1DO6j3HTWbWtr2q3xD2coTCb0CgmAw/edit))
- [Reverse Engineering: Data Access]() (slides [here](https://docs.google.com/presentation/d/154CQfQtpleaAQv9xNI1FVosbXc_18VZvXVpcs9Ljzzo/edit#slide=id.p))
- **Coming soon** [Reverse Engineering: Static Tools]() (slides [here]())
- **Coming soon** [Reverse Engineering: Dynamic Tools]() (slides [here]())
- **Coming soon** [Reverse Engineering: Examples]() (slides [here]())

Additionally, you should be quite familiar with the following fundamental knowledge:

- [Fundamentals: Assembly](https://www.youtube.com/watch?v=ImdnOGNZflU) (slides [here](https://docs.google.com/presentation/d/1pN0nuhQIhn92QBitMznFNSRABDkMtbUW4MEJBYFwtwM/edit?usp=sharing))
- [Fundamentals: Binary Files](https://www.youtube.com/watch?v=nKqFeYJ483U) (slides [here](https://docs.google.com/presentation/d/1wrX8tvwaxIEk5hx4OtQmPqps-MScIaDO-9bTKQqr8vI/edit?usp=sharing))
- [Fundamentals: Linux Process Loading](https://www.youtube.com/watch?v=kUMCAzSOY-o) (slides [here](https://docs.google.com/presentation/d/1TwM5WLWnTqrNkpXjGKkaXYbKZEpatEQYA7ckBVXAOhs/edit?usp=sharing))

## Practice

The goal of the challenge sets in this module is, as always, to get the flag.
Most challenge take user input (via a variety of methods), does some operations, and verifies the result.
If you produce correct input, you can get it to read the flag and print it out to you.
Some challenges will force you to "crack" them.
Good luck!

If you are ready to tackle the challenges, go to [https://cse466.pwn.college](https://cse466.pwn.college)! **CHALLENGES WILL LAUNCH DURING THE LIVE TWITCH STREAM ON 9/16/2020!**

## Useful Tools

As mentioned in the slides, there are a number of useful tools for this assignment!
Here is a (non-exhaustive) list:

* `ltrace` is invaluable in understanding how the binary is trying to get input from you.
  The input method of most of these binaries can be determined just by using `ltrace`.
* `gdb` will let you run and inspect the state of these programs.
  Some useful gdb concepts:
   * Know the difference between `step instruction` (`si`) and `next instruction` (`ni`).
     It boils down to the fact that `si` will follow jumps, and `ni` will step over jumps.
     This means that if you use `si`, you will quickly find yourself crawling through libc code, which is insane and unnecessary.
   * You can use `x/i $rip` to disassemble the next instruction that will be executed.
     You can call `display/i $rip` to make the next instruction display every time gdb prompts you for input.
     You can also do `x/2i` and `display/2i` to print two (or other quantities of) instructions.
   * The `disas` command will disassemble the current function that you are looking at.
   * gdb can be scripted!
     Look up conditional breakpoints and scriptable breakpoints in the gdb manual.
   * Modern binaries are _position independent_, meaning that they can be loaded anywhere in memory when they run.
     GDB will load them at the offset `0x555555554000`.
     This means that if objdump is telling you that main starts at some address like, `0x100`, the address when debugging with GDB will be `0x555555554100`
* `objdump -d -M intel the_binary` will disassemble the binary you want to look at.
  `-M intel`, in that command, makes objdump give you nice and readable Intel assembly syntax.
* `kill` is a useful tool to send signals to binaries.
  To make this possible with the SUID binaries, I have made `kill` SUID for you.
* `strings` will list printable strings in the file.
  This is useful for looking for constant strings that the program checks for (such as file names and so on) in the course of getting input.
  Keep in mind that the options for string include a minimum size that it will print.
* pwntools lets you interact with processes in exactly the same way as you interact with network connections.
  Look into `pwn.process`.
* `rappel` is a nice tool to help you figure out what certain instructions do.
* [Binary Ninja](https://cloud.binary.ninja) is a free, web-based static binary reverse engineering tool.

You should be able to solve the first-level challenges by simply using `ltrace`.

## Programs accessing arguments and environment variables

Some of the challenges will take input from an [environment variable](https://wiki.archlinux.org/index.php/environment_variables) or commandline arguments.
The linked material for it above is useful --- read it.

This subsection is a quick example of how to reverse-engineer a program that accesses commandline variables and environment variables.
As discussed in class, in C, this data is provided as arguments to the `main` function, like this:

```
int main(int argc, char **argv, char **envp)
{
	printf("The number of arguments is: %d\n", argc);
	printf("The program name is: %s\n", argv[0]);
	printf("The first argument is: %s\n", argv[1]);
	printf("The first environment variable is: %s\n", envp[0]);
	printf("The second environment variable is: %s\n", envp[1]);
}
```

`argc` is the number of arguments.
`argv` is a pointer to an array of pointers that each point to an argument, where each argument is a string.
More information is available [here](http://pages.cs.wisc.edu/~smoler/cs354/onyourown/C.argv.html), with more discussion (and some nit-picking) [here](https://stackoverflow.com/questions/17254853/argv-pointer-to-an-array-of-pointers).
`envp` is the same structure as `argv` (a pointer to an array of pointers), but each entry is an environment variable string in the format `NAME=value`.

Let's run it and see what happens!

```
$ gcc -o test test.c
$ ./test testing
The number of arguments is: 2
The program name is: ./test
The first argument is: testing
The first environment variable is: PWD=/home/yans
The second environment variable is: SHLVL=1
```

A few things to unpack here.
First, why is `number of arguments` 2?
That's because the name of the program (`./test`) comes across as the first entry in `argv` (`argv[0]`), and the actual first argument is the second (`argv[1]`).
If there were more arguments, they would be pointed to by `argv[2]`, `argv[3]`, and so on.
What if there are no arguments?

```
$ ./test testing
The number of arguments is: 1
The program name is: ./test
The first argument is: (null)
The first environment variable is: PWD=/home/yans
The second environment variable is: SHLVL=1
```

Interestingly, it prints `(null)` for the second argument.
`printf` does this when the argument passed to `%s` is a NULL pointer.
The last element of the `argv` and `envp` arrays is always a NULL pointer, so that you know when to stop if you are looping through them (you can also use `argc` to tell when to stop for `argv`, but there's no equivalent to `argc` for `envp`).

Now, what about the environment variables?
They're stored similarly to environment variables, with the difference that each variable value is prepended by its variable name in a `NAME=value` pair.
The order is arbitrary; they just happen to be in some order (probably chronologically in the order that they were set).
In the shell above, the first environment variable is `PWD` (the process working directory), with a value of `/home/yans`, and the second is `SHLVL`, with a value of 1.
There are a _lot_ of environment variables in a normal shell.
Here is a program that counts the number:

```
int main(int argc, char **argv, char **envp)
{
	int num_vars = 0;
	while (*envp)
	{
		envp++;
		num_vars++;
	}
	printf("There are %d environment variables.\n", num_vars);
}
```

This program increments the `envp` environment (using [pointer arithmetic](https://www.tutorialspoint.com/cprogramming/c_pointer_arithmetic.htm), which you should know) until it points to the NULL value that terminates the `envp` array, at which point dereferencing the `envp` pointer (`*envp`) will result in NULL, and the `while` loop will terminate.
The number of times it had to increment it (`num_vars`) is the number of environment variables we have.
If I run it in my shell, I get:

```
$ gcc countenv.c -o countenv
$ ./countenv 
There are 59 environment variables.
```

Quite a few.
`env` runs a command with a modified environment.
For example, `env -i` will run it with an empty environment.

```
$ env -i ./countenv
There are 0 environment variables.
```

I can also use `env` to set environment variables.

```
$ env -i NAME=Yan JOB=Professor ./countenv
There are 2 environment variables.
```

And we can view them:

```
$ env -i NAME=Yan JOB=Professor ./test
The number of arguments is: 1
The program name is: ./test
The first argument is: (null)
The first environment variable is: NAME=Yan
The second environment variable is: JOB=Professor
```

Amazing.
Let's look at these programs on the assembly level, starting by disassembling the `test` binary using `objdump -d -M intel test`.
This gives us:

```
000000000000064a <main>:
 64a:	55                   	push   rbp
 64b:	48 89 e5             	mov    rbp,rsp
 64e:	48 83 ec 20          	sub    rsp,0x20
 652:	89 7d fc             	mov    DWORD PTR [rbp-0x4],edi
 655:	48 89 75 f0          	mov    QWORD PTR [rbp-0x10],rsi
 659:	48 89 55 e8          	mov    QWORD PTR [rbp-0x18],rdx
 65d:	8b 45 fc             	mov    eax,DWORD PTR [rbp-0x4]
 660:	89 c6                	mov    esi,eax
 662:	48 8d 3d 0f 01 00 00 	lea    rdi,[rip+0x10f]        # 778 <_IO_stdin_used+0x8>
 669:	b8 00 00 00 00       	mov    eax,0x0
 66e:	e8 ad fe ff ff       	call   520 <printf@plt>
 673:	48 8b 45 f0          	mov    rax,QWORD PTR [rbp-0x10]
 677:	48 8b 00             	mov    rax,QWORD PTR [rax]
 67a:	48 89 c6             	mov    rsi,rax
 67d:	48 8d 3d 14 01 00 00 	lea    rdi,[rip+0x114]        # 798 <_IO_stdin_used+0x28>
 684:	b8 00 00 00 00       	mov    eax,0x0
 689:	e8 92 fe ff ff       	call   520 <printf@plt>
 68e:	48 8b 45 f0          	mov    rax,QWORD PTR [rbp-0x10]
 692:	48 83 c0 08          	add    rax,0x8
 696:	48 8b 00             	mov    rax,QWORD PTR [rax]
 699:	48 89 c6             	mov    rsi,rax
 69c:	48 8d 3d 0e 01 00 00 	lea    rdi,[rip+0x10e]        # 7b1 <_IO_stdin_used+0x41>
 6a3:	b8 00 00 00 00       	mov    eax,0x0
 6a8:	e8 73 fe ff ff       	call   520 <printf@plt>
 6ad:	48 8b 45 e8          	mov    rax,QWORD PTR [rbp-0x18]
 6b1:	48 8b 00             	mov    rax,QWORD PTR [rax]
 6b4:	48 89 c6             	mov    rsi,rax
 6b7:	48 8d 3d 12 01 00 00 	lea    rdi,[rip+0x112]        # 7d0 <_IO_stdin_used+0x60>
 6be:	b8 00 00 00 00       	mov    eax,0x0
 6c3:	e8 58 fe ff ff       	call   520 <printf@plt>
 6c8:	48 8b 45 e8          	mov    rax,QWORD PTR [rbp-0x18]
 6cc:	48 83 c0 08          	add    rax,0x8
 6d0:	48 8b 00             	mov    rax,QWORD PTR [rax]
 6d3:	48 89 c6             	mov    rsi,rax
 6d6:	48 8d 3d 1b 01 00 00 	lea    rdi,[rip+0x11b]        # 7f8 <_IO_stdin_used+0x88>
 6dd:	b8 00 00 00 00       	mov    eax,0x0
 6e2:	e8 39 fe ff ff       	call   520 <printf@plt>
 6e7:	b8 00 00 00 00       	mov    eax,0x0
 6ec:	c9                   	leave  
 6ed:	c3                   	ret    
```

Here, we see the function prologue (as discussed in class) at `0x64a` and `0x64b`, which saves off the previous frame pointer and sets up the current frame.
Then, at `0x64e`, the stack pointer is decremented (at `0x64e`) to make room for local storage of the three arguments to `main` (at `0x652`, `0x655`, and `0x659`).
They are our familiar friends from above:

* `argc`, passed in as `rdi` (but accessed as `edi`, because the number of arguments is capped at 2^16, which fits fine into `edi` and, as you can see, results in a shorter instruction).
* `argv`, passed in as `rsi`
* `envp`, passed in as `rdx`

Having safely stored the arguments on the stack, the program goes on to _set up the argument to_ and _call_ `printf` several times: to print the number of arguments, the value of the first argument, the value of the second argument, the first environment variable, and the second environment variable.
Let's start with printing the number of arguments:

```
 65d:	8b 45 fc             	mov    eax,DWORD PTR [rbp-0x4]
 660:	89 c6                	mov    esi,eax
 662:	48 8d 3d 0f 01 00 00 	lea    rdi,[rip+0x10f]        # 778 <_IO_stdin_used+0x8>
 669:	b8 00 00 00 00       	mov    eax,0x0
 66e:	e8 ad fe ff ff       	call   520 <printf@plt>
```

If you recall, at `0x652`, we stored `argc` onto the stack at the location `rbp-0x4`.
At `0x65d`, we load it into `eax` (again, it's small enough to fit into a 32-bit register.
At `0x660`, we transfer it to `esi`, which will be the second argument to `printf` (you can check the calling convention slide from lecture 3).
At `0x662`, we _l_oad the _e_effective _a_ddress (the `lea` instruction) of our format string (`The number of arguments is: %d`) into `rdi`.
You can verify this in GDB using `x/s $rip+0x10f` (note that, because these are Position Independent Executables, the instruction will be at memory address `0x555555554000662` in gdb).
With the format string in `rdi` and `argc` in `rsi`, when the `call` to `printf` happens at `0x66e`, we will have performed exactly `printf("The number of arguments is: %d", argc);` from our code!

Why do we move `0` into `eax` at `0x669`?
`rax` is the register that will contain the _return value_ from printf.
I'm not sure why `gcc` decided to zero it out before the call --- these things don't always make 100% sense.

Also, why do we re-load `argc` from memory, even though it was comfortably hanging out in `rdi`?
This is also a result of the compiler being lazy at this stage.
We compiled the program without _optimizations_, so it doesn't bother to optimize these issues away.
If we compiled with `gcc -O3`, these unnecessary memory operations would not happen, but the code would be a lot less readable in other ways.

So, that's `argc` taken care of.
Let's look at how `argv[0]` is printed out.
That assembly is:

```
 673:	48 8b 45 f0          	mov    rax,QWORD PTR [rbp-0x10]
 677:	48 8b 00             	mov    rax,QWORD PTR [rax]
 67a:	48 89 c6             	mov    rsi,rax
 67d:	48 8d 3d 14 01 00 00 	lea    rdi,[rip+0x114]        # 798 <_IO_stdin_used+0x28>
 684:	b8 00 00 00 00       	mov    eax,0x0
 689:	e8 92 fe ff ff       	call   520 <printf@plt>
```

This is a bit more complicated, because of the `argv[0]` array lookup.
First, we retrieve the second argument (`argv`) into `rax` at `0x673`.
Then, at `0x677`, we read the value stored at the address pointed to by `argv`, and put _that_ into `rax`.
This is `argv[0]`, our program name.
The rest of the snippet is the same as the `argc` case, just with a different format string.

Finally, let's look at the `argv[1]` printf:

```
 68e:	48 8b 45 f0          	mov    rax,QWORD PTR [rbp-0x10]
 692:	48 83 c0 08          	add    rax,0x8
 696:	48 8b 00             	mov    rax,QWORD PTR [rax]
 699:	48 89 c6             	mov    rsi,rax
 69c:	48 8d 3d 0e 01 00 00 	lea    rdi,[rip+0x10e]        # 7b1 <_IO_stdin_used+0x41>
 6a3:	b8 00 00 00 00       	mov    eax,0x0
 6a8:	e8 73 fe ff ff       	call   520 <printf@plt>
```

Things here are almost identical to `argv[0]`, with the exception of the instruction at `0x692`.
This instruction adds 8 to `rax`, which before this had the value of `argv`, and after this will point 8 bytes _after_ `argv`.
Since argv is an array of pointers, each element in the array is 64 bits (on a 64-bit system), which is 8 bytes.
By incrementing `rax` by 8, we are making it point to `argv[1]` instead of `argv[0]`.
Note that, using pointer arithmetic in C, we would accomplish the same thing by doing `argv+1`!
C knows that the elements pointed to by `argv` are 8 bytes long, so it translates `argv+1` in C to `argv+8` in assembly.
This is an example of semantic information being lost: C knows that `argv` is a pointer to pointers, and assembly does not have this information.

The rest of this snippet should now be quite familiar.
We move the format string into `rdi` (at `0x69c`), and do the call to printf.

Furthermore, the two snippets for printing environment variables follow the pattern of the `argv` printfs perfectly.

Let's move on to `countenv`, since that does some more interesting pointer arithmetic as it scans through the environment to count the number of variables.
Disassembling it, we get:

```
000000000000064a <main>:
 64a:	55                   	push   rbp
 64b:	48 89 e5             	mov    rbp,rsp
 64e:	48 83 ec 30          	sub    rsp,0x30
 652:	89 7d ec             	mov    DWORD PTR [rbp-0x14],edi
 655:	48 89 75 e0          	mov    QWORD PTR [rbp-0x20],rsi
 659:	48 89 55 d8          	mov    QWORD PTR [rbp-0x28],rdx
 65d:	c7 45 fc 00 00 00 00 	mov    DWORD PTR [rbp-0x4],0x0
 664:	eb 09                	jmp    66f <main+0x25>
 666:	48 83 45 d8 08       	add    QWORD PTR [rbp-0x28],0x8
 66b:	83 45 fc 01          	add    DWORD PTR [rbp-0x4],0x1
 66f:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
 673:	48 8b 00             	mov    rax,QWORD PTR [rax]
 676:	48 85 c0             	test   rax,rax
 679:	75 eb                	jne    666 <main+0x1c>
 67b:	8b 45 fc             	mov    eax,DWORD PTR [rbp-0x4]
 67e:	89 c6                	mov    esi,eax
 680:	48 8d 3d a1 00 00 00 	lea    rdi,[rip+0xa1]        # 728 <_IO_stdin_used+0x8>
 687:	b8 00 00 00 00       	mov    eax,0x0
 68c:	e8 8f fe ff ff       	call   520 <printf@plt>
 691:	b8 00 00 00 00       	mov    eax,0x0
 696:	c9                   	leave  
 697:	c3                   	ret  
```

This is shorter, but it has an more complex _control flow_ than `test`.
Right away, we can see a jump at `0x679`, which goes back to `0x666`.
This jump is a conditional with a `not equal` condition (hence, `jne`).
As you recall from the lecture, these conditions check flags in the `rflags` register, and the flags are set by many different instructions.
Usually, when you are explicitly doing comparisons in C, they get compiled into the `cmp X, Y` instruction (which subtracts the value in Y from the value in X and updates flags based on the result) or the `test X, Y` (which does a _bitwise and_ between the value in X and the value in Y and updates flags based on the result).
In this case, the `test` instruction is actually right before that jump, at `0x676`.
And, it compares the value in `rax` against the value in `rax`.
Why does this happen?
`test` is most frequently used to check for whether a value is non-zero, while `cmp` is used to check if a value is equal/less/greater than another value.
Here, we are checking if `rax` is zero.
Why do we use `jne` (jump if not equal) instead of `jnz` (jump if not zero) for the actual jump?
If you look at the lecture notes, both instructions actually use the same logic: they check the _zero flag_ to see if the result of the previous operation was zero, and the jump is taken if it was not.
The difference is that you would use a `cmp` before a `jne` (so the zero flag would mean that the two compared values were equal, and the result of the subtraction was zero), and you would use `test` before a zero check (so if the result of the bitwise AND was zero, that means the value being ANDed is zero).
In fact, `jne` and `jnz` is [_actually the same instruction_](http://ref.x86asm.net/coder64.html#x75)!

Anyways, the upshot is that this jump checks that something is non-zero, and jumps backwards if that is the case!
We can safely assume that this is the backwards edge of our `while(*envp)` (i.e., if it decides to loop again).
We can track backwards to make sure that this is actually what is happening: looking at `0x673`, we see that `rax` is the value stored at what `rax` _from before that instruction_ was pointing at (i.e., the instruction at `0x673` _dereferences_ `rax`).
This bodes well for the hypothesis that we're looking at `*envp`.
Looking back at `0x66f`, we can see `rax` being loaded from `[rbp-0x28]`.
Looking back farther, to `0x659`, we see `rdx` being _stored_ into `[rbp-0x28]`.
`rdx` is the third argument to `main`, which _is_ `envp`!
Our hypotehsis was correct!

But, in our C code for `countenv`, we increment `envp`.
Where does this happen?
We can see it happen at `0x666` (which is also the target of the backwards jump), where `[rbp-0x28]` has 8 added to it.
Again, like the `argv` case above, this ends up pointing `envp` at the next environment variable.
Right after this, by the way, at `0x66b`, we see `[rbp-0x4]` get 1 added to it.
This smells suspiciously like our `num_vars` variable that we increment, and if we look at `0x67b` (immediately after the conditional jump at `0x679` _stops_ making us loop back, which means that the loop is over), we can see `[rbp-0x4]` being loaded into `esi` to be printed out, as the number of environment variables!

The one remaining mystery is the unconditional jump at `0x664`.
It jumps over the two `add` instructions (which comprise the increment of `envp` and of `num_vars` that is the body of our loop) and goes straight to the loop check that leads to the conditional jump.
Why does this happen?
The answer is because of the difference between `while() { }` and `do { } while();`.
The former checks the condition before entering the loop, while the latter only checks it after the first iteration.
Without the jump at `0x664`, we would always execute the body of the loop at least once, which would make this a `do { } while();`.
With that jump, we go straight to the check, and only execute the loop body if the condition is satisfied.
The jump is the compiler's way of having the correct semantics without having to have that condition check duplicated in the assembly before the loop begins.

Hopefully, this overview was helpful for getting you started with how these programs retrieve arguments and environment variables on the assembly level.
Good luck!

## COMPLICATION: The binaries try to read or write files that I don't have permission to!

You'll notice that the directory where all of the challenges reside is not writable by non-root users.
This is a problem because some of the challenges will attempt to create or open files in this directory, which will fail.

All of the challenges open files using a _relative path_ (i.e., `open("blah", 0);`).
Relative paths are relative to the _current working directory_ of the process.
You should google this concept to understand what to do to make these challenges work.

## Other resources

There are many resources related to reverse engineering around the internet.
A good place to start is a series of walkthroughs of several hacking challenges by ASU's own Adam Doupe on his [YouTube channel](https://www.youtube.com/watch?v=qGt-0OOAFcM&list=PLK06XT3hFPziMAZj8QuoqC8iVaEbrlZWh).

For information about communicating through FIFOs, check out [this article](https://www.geeksforgeeks.org/named-pipe-fifo-example-c-program/).
