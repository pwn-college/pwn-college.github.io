Welcome to pwn.college BETA!

pwn.college is a first-stage education platform for students (and other interested parties) to learn about, and practice, core cybersecurity concepts in a hands-on fashion.
It is designed to take a "white belt" in cybersecurity to becoming a "yellow belt", able to approach (simple) CTFs and wargames.

The philosophy of pwn.college is "practice makes perfect".
Good luck!

# pwn.college is in BETA

Following the open-source philosophy of "release early, release often", pwn.college is in BETA.
This is not yet a polished education platform, but we're pushing there!
Right now, we are working on resolving the following **known issues**:

1. The module slides are not very useful without video (and demos).
2. Some of the module challenge sets have problems with difficulty scaling (ROP suffers from this especially).
3. Some of the module challenge sets are missing concepts (example: GOT overwrites for memory corruption, actual memory corruption in the kernel).

If you have other comments, suggestions, and feedback, please email us at [pwn.college@asu.edu](mailto:pwn.college@asu.edu)!

# Who is this for?

Consider hacking as a martial art.
Newcomers begin as _white belts_, with zero security knowledge.
Slowly and painfully, they become _yellow belts_, able to reason about simple security challenges.
Over time, they become more sure in their skills, achieving _brown belt_ status, before finally graduating to hacking masters: _black belts_.

pwn.college is meant for **white belts**.
If you already know the basics of hacking (and, thus, are a yellow belt), you will find this resource very easy.
If you are a brown belt, you will find it quite boring.
If you are a black belt, it will put you to sleep.

# Who is responsible?

pwn.college was created by [Zardus (Yan Shoshitaishvili)](http://yancomm.net) and [kanak (Connor Nelson)](https://connornelson.com) for the CSE 466 course at Arizona State University.
It has powered the Fall 2018 and Fall 2019 editions of CSE466, and is moving forward toward changing the world!

# The modules of pwn.college

pwn.college is organized as a set of modules covering different topics.
Each module has a set of lectures (slides available now, videos coming soon!) and practice problems, auto-generated for each aspiring hacker to practice on.
Challenges come in a _teaching_ variety, which will walk you through their own solutions, and a _testing_ variety, which will challenge you with less guidance.
Challenges are run directly on pwn.college, and can be launched in _practice_ mode, where you have root access but there is a fake flag, and _real_ mode, where you cannot read the flag without exploiting the challenge.
The following modules are currently available at pwn.college:

- [Module 1: Abusing SUID in Linux](modules/suid)
- [Module 2: Shellcode](modules/shellcode)
- [Module 3: Sandboxing](modules/sandbox)
- [Module 4: Reversing](modules/reversing)
- [Module 5: Memory Corruption](modules/pwning)
- [Module 6: Format Strings](modules/fmt)
- [Module 7: Return Oriented Programming](modules/rop)
- [Module 8: Heap Exploitation](modules/heap)
- [Module 9: Kernel Security](modules/kernel)

# Concepts

Aside from directed module, pwn.college contains a wiki-like set of [hacking concepts](concepts)!
These are designed to be linked directly from challenge problems.

# Further Practice

After you learn the basics of cybersecurity and achieve yellow belt status, you should move on to harder challenges.

Capture The Flags (CTFs) are a great way to practice your hacking skills in a fun and ethical way.
The most popular way to find upcoming events is at [https://ctftime.org](https://ctftime.org).
If you are at ASU, feel free to check out and join ASU's CTF Team _pwndevils_ at [https://pwndevils.com](https://pwndevils.com).

Wargames are another great way to practice your hacking skills.
Whereas CTFs are short (normally 48 hour) events, wargames are not time-based.
You can find a list of wargames at [https://github.com/zardus/wargame-nexus](https://github.com/zardus/wargame-nexus).

# Contributing

The [infrastructure powering pwn.college](https://github.com/pwn-college/pwn-college) and [the web-facing content](https://github.com/pwn-college/pwn-college.github.io) are open source, and we welcome pull requests and issues.
The modules are closed-source, because they include source code and solution scripts.
If you are an educator, or otherwise someone we trust, and are interested in collaborating on the modules themselves, please email us at [pwn-college@asu.edu](mailto:pwn-college@asu.edu).
Likewise, drop us a line if you are interested in collaborating on the slides!
