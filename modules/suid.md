# Module: Abusing Linux SUID

This module explores the impact of SUID misuse on the security of a system.

## Slides

The slides for this module are:

- [Linux in Depth](https://docs.google.com/presentation/d/1fdQ4fBVKmWpyNIp0PDAJ4WUsCjYaCA37mkUxdW7tRl8/edit#slide=id.p)

## Practice

Practice challenges for this module let aspiring hackers practice the (mis)use of Linux software!
For each challenge, the hacker can choose a single binary on the system to be set SUID, and will then be provided a shell on a Linux environment.
In this environment, there is a file `/flag`, containing the secret flag that you must read out.
However, the file is only readable by root user!
Using your single SUID binary, you must elevate your privileges enough to read out the flag.

A single SUID binary will net you a single flag.
That is, specifying `cat` and using it to leak out the flag (as in the example below) will get you one point, and specifying `tail` and using it to leak out the flag (as in another example below) will get you another.
In a more complex case, specifying `chmod` (as in the example below) and then using that to change the permission of other programs and read out the flag that way will get you a flag for `chmod` regardless of what other permissions you change, since `chmod` was the specified command.

If you are ready to tackle the challenges, go to [https://ctf.pwn.college](https://ctf.pwn.college)!

## Example Interactions

Here is a sample interaction that successfully retrieves the flag by setting the SUID flag on `/bin/cat` (you may use this for one of your solutions!), thus allowing `cat` to run as root.
`cat` is a program that concatenates files and prints them out to standard out (if this is confusing, you are behind. You _need_ to read the resources linked below to get un-confused).
Thus, retrieving the flag with it is quite simple:

```
myuser@mylaptop:~$ ssh ctf@cse466.pwn.college
ctf@b38bdd753b5b:~$ /bin/cat /flag
CSE466{747985b99bd25b8805ced639297720ae71e87a7acef580dc6b514143e5152133}
ctf@b38bdd753b5b:~$ exit
```

As you can see, this gives you the flag associated with `cat`.
Let's choose another program: say, `/usr/bin/tail` (you may use this for another solution!).
`tail` is a program that prints out the last few lines of a file.
Since the `/flag` file only has one line (the flag), this is perfect for us!
Specifying `tail`, you will receive another flag:

```
ctf@b38bdd753b5b:~$ tail /flag
CSE466{7ca9d3c2fcbaa0c0cde22777bfefff2a5f5ac707f5194f91cd24226dbae0b74b}
ctf@b38bdd753b5b:~$ exit
```

Note that this is a _different_ flag from `/bin/cat`!
Now, you have two flags: one for `cat` and one for `tail`.
Note that, while `/bin/cat` and `/usr/bin/tail` is easy, other programs are not so simple to read the flag with.
No matter how convoluted retrieving the flag is with a given program, one unique SUID binary path will only ever yield _one_ flag.

For a slightly more complex example, let's look at `/bin/chmod`.
`chmod` is a program that can change permissions of files.
There are _many_ ways to read the `/flag` file with `chmod`.
We'll cover a few here (feel free to use this for one of your solutions!).

First, we can simply change the permissions of the `/flag` file to allow us to read it:

```
ctf@5d1f52fff4e8:~$ chmod 644 /flag
ctf@5d1f52fff4e8:~$ cat /flag
CSE466{36ef1e24753a8e3119eeac953e44f47f48aa388f9a72e2cb2d54fc9a622c5ef8}
ctf@5d1f52fff4e8:~$ exit
```

Second, we can make the `/bin/cat` binary SUID, so that _it_ runs as root and lets us read the flag.

```
ctf@5d1f52fff4e8:~$ chmod 4755 /bin/cat
ctf@5d1f52fff4e8:~$ cat /flag
CSE466{36ef1e24753a8e3119eeac953e44f47f48aa388f9a72e2cb2d54fc9a622c5ef8}
ctf@5d1f52fff4e8:~$ exit
```

And we can do the same with other binaries, such as `/usr/bin/tail`:

```
ctf@5d1f52fff4e8:~$ chmod 4755 /usr/bin/tail
ctf@5d1f52fff4e8:~$ cat /flag
CSE466{36ef1e24753a8e3119eeac953e44f47f48aa388f9a72e2cb2d54fc9a622c5ef8}
ctf@5d1f52fff4e8:~$ exit
```

Note that all three ways of getting the flag after specifying `/usr/bin/chmod` _get the same flag_.
This is because the flag depends on the path to the binary that you specify in the `Path to Binary:` prompt.
`chmod` is great, and it'll let you run _any_ binary with SUID, but it'll only get you one flag.

Now you have _three_ freebies.
Go get the rest!

## HINT: Reading program documentation

To get a flag using a given program, you need to understand how the program works.
For `cat` and `tail` it's easy.
Can you get the flag using `/bin/whiptail`, a program that is used to create TUIs (Text User Interfaces)?
Hint: yes, but you need to know how to use whiptail!

So, how do you learn?
There are two main ways: the program help and the program manual.
The program help is generally accessed by using the `-h`, `--help`, or `--usage` options (i.e., `whiptail --usage`).
The program manual is generally accessible using the `man` or `info` commands (`man whiptail` or `info whiptail`).

You can also find manuals on google.
For example, googling `man whiptail` will bring up the `whiptail` manual.

This is a _hacking_ challenge. You will have to *abuse* these programs.
They might not be originally intended to read out files, but you can often misuse their functionality to do so.
Their documentation is your friend.

## HINT: Dealing with errors

In the course of trying to abuse programs into giving you the flag, they might fail in weird ways.
They might also fail in weird ways because of the way the container is run.
As a rule of thumb, you should google all the errors that you get.
Sometimes, the solution is quite simple!

`/bin/whiptail` is a great example of this: it doesn't work at all right out of the box, but the error that it gives you (`TERM environment variable needs set.`), and the [first result on google](https://stackoverflow.com/questions/16242025/term-environment-variable-not-set) shows you how to fix that.
There are other good examples of this (such as `/bin/nano`).

## HINT: Picking your targets

There are a _lot_ of targets to pick from.
To succeed in this class, you should already have a good idea of which programs to start with.
In general, almost any application that moves data from a file to somewhere else (the screen, another file, etc) can be used to leak the flag.
For example, in the context of the useful resources below, consider how you would use `/bin/cp` to leak the flag?
It is doable.

Once you have leaked the flag with a given program, look for similar programs.
For example, `tail` and `head` are very similar, and can both be used to leak the flag.

## Other hints

Also keep in mind a few hints:

1. The flag is stable across connections and program executions, for the same SUID binary. That means that you don't necessarily have to read the entire flag, cleanly, in one swoop. Some programs might mangle it (but in a way that you can unmangle), and some programs might only be able to leak a small amount of it in a single execution, but can leak the whole flag when executed multiple times. If you find the flag changing for a single program, that probably means that the program itself is mangling it.
1. This is a hacking challenge. There may be some "metagaming" that you can do. Look into how all parts of Linux work; it might help!
1. Think very carefully about how programs present information to you when they don't think that information is something critical. Debug info when debug flags are enabled. Error messages containing data that isn't sensitive when it's data you have access to anyways, but could be sensitive when the program has access to data that you don't have access to. These situations expose methods that you can abuse certain programs to get flags.
1. Sometimes, lazy programmers call out to other utilities instead of writing the functionality themselves. What happens if those other utilities are SUID root? What happens if you can influence where those other utilities are launched from (i.e., check out the PATH variable). This relies on lazy programming of the utilities that you are attacking, so you might want to pick up other targets before going down this path.

## Other useful resources

Some other useful resources:

- Searching for executable files: https://stackoverflow.com/questions/4458120/unix-find-search-for-executable-files
- A primer on Linux file permissions: https://wiki.archlinux.org/index.php/File_permissions_and_attributes
- A primer on privilege escalation attacks against Linux hosts. The SUID abuse section has obvious implications for this assignment: https://payatu.com/guide-linux-privilege-escalation/
- Some thoughts on abusing dangers in SUID executables: https://www.pentestpartners.com/security-blog/exploiting-suid-executables/
- Another SUID attack tutorial: https://null-byte.wonderhowto.com/how-to/use-misconfigured-suid-bit-escalate-privileges-get-root-0173929/
- Another SUID tutorial. It is focused on shell scripts, but there are insights that can be used: http://www.drdobbs.com/dangers-of-suid-shell-scripts/199101190
- A treatise on I/O redirection in Linux, which has applications in this assignment: https://bencane.com/2012/04/16/unix-shell-the-art-of-io-redirection/
- A guide on Linux symbolic links. Might be useful to confuse some challenges: https://www.nixtutor.com/freebsd/understanding-symbolic-links/
