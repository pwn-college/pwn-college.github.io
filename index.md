# Welcome to pwn.college!

pwn.college is a first-stage education platform for students (and other interested parties) to learn about, and practice, core cybersecurity concepts in a hands-on fashion.
It is designed to take a "white belt" in cybersecurity to becoming a "yellow belt", able to approach (simple) CTFs and wargames.
The philosophy of pwn.college is "practice makes perfect".

pwn.college was created by [Zardus (Yan Shoshitaishvili)](http://yancomm.net) and [kanak (Connor Nelson)](https://connornelson.com) at Arizona State University.
It powers ASU's Computer Systems Security course, CSE466, and is now open, for free, to participation for interested people around the world!

pwn.college is hosted across a number of internet services:
- We record our [lectures on YouTube](https://www.youtube.com/channel/UCBaWwFw7KmCN8YlfX4ERYKg/).
- We stream our [classes on Twitch](https://www.twitch.tv/pwncollege/) every Wednesday from 4:30pm to 7:30pm AZ time.
- We host [practice problems on our infrastructure](https://cse466.pwn.college).
- We answer questions about pwn.college on [the public google group](https://groups.google.com/g/pwn-college-users).

If you have other comments, suggestions, and feedback, please email us at [pwn-college@asu.edu](mailto:pwn-college@asu.edu)!

# Who is this for? (prerequisites)

Consider hacking as a martial art.
Newcomers begin as _white belts_, with zero security knowledge.
Slowly and painfully, they become _yellow belts_, able to reason about simple security challenges and start down the road of, for example, CTF competitions.
Over time, they become more sure in their skills, achieving _brown belt_ status (and able to, for example, contribute to the cybersecurity industry), before finally graduating to hacking masters: _black belts_.

pwn.college is meant for **white belts**.
If you already know the basics of hacking (and, thus, are a yellow belt), you will find this resource very easy.
If you are a brown belt, you will find it quite boring.
If you are a black belt, it will put you to sleep.

That being said, just because the material is for beginners does _not_ mean that the concepts are basic.
The course tackles complex concepts, up to and including the inner working of OS kernels.
Good Computer Organization and OS courses covering the following are recommended.
- C programming.
- C compilation.
- x86\_64 assembly.
- OS internals (system calls, etc).
- Linux operations (FS layout, permissions, shell scripting, etc).

Though pwn.college has an [introduction](modules/intro) module that covers some fundamentals, a lack of knowledge in these areas will lead to heavy difficulties in the course.

# How do I jump in?

pwn.college is organized as a set of modules covering different topics.
Each module has a set of lecture slides and videos and practice problems auto-generated for each aspiring hacker to practice on.
Challenges come in a _teaching_ variety, which will walk you through their own solutions, and a _testing_ variety, which will challenge you with less guidance.
Challenges are run directly on pwn.college, and can be launched in _practice_ mode, where you have root access but there is a fake flag, and _real_ mode, where you cannot read the flag without exploiting the challenge.

pwn.college has come out of beta, and modules are being launched alongside the progress of ASU's Fall 2020 CSE466 class.
So far, the following modules are live:

- [Module 0: Introduction](modules/intro)

Additional modules will be launched on a weekly basis!
If you are impatient, you can check out archived modules from the pwn.college beta at the bottom of the page.





# Further Practice

After you learn the basics of cybersecurity and achieve yellow belt status, you should move on to harder challenges.

Capture The Flags (CTFs) are a great way to practice your hacking skills in a fun and ethical way.
The most popular way to find upcoming events is at [https://ctftime.org](https://ctftime.org).
If you are at ASU, feel free to check out and join ASU's CTF club _pwndevils_ at [https://pwndevils.com](https://pwndevils.com).

Wargames are another great way to practice your hacking skills.
Whereas CTFs are short (normally 48 hour) events, wargames are not time-based.
You can find a list of wargames at [https://github.com/zardus/wargame-nexus](https://github.com/zardus/wargame-nexus).

If you want to get involved with cybersecurity research, but don't know how, consider joining us for an [internship at ASU](https://sefcom.asu.edu/apprenticeship).

# Contributing

The [infrastructure powering pwn.college](https://github.com/pwncollege/pwn-college) and [the web-facing content](https://github.com/pwncollege/pwn-college.github.io) are open source, and we welcome pull requests and issues.
The modules are closed-source, because they include source code and solution scripts.
If you are an educator, or otherwise someone we trust, and are interested in collaborating on the modules themselves, please email us at [pwn-college@asu.edu](mailto:pwn-college@asu.edu).
Likewise, drop us a line if you are interested in collaborating on the slides!

# ARCHIVED MODULES FROM THE PWN-COLLEGE BETA

The pwn-college beta was announced at HITCON 2019 and ran until August 2020.
All of the old material is still available below:

- [Module 1: Abusing SUID in Linux](modules-old/suid)
- [Module 2: Shellcode](modules-old/shellcode)
- [Module 3: Sandboxing](modules-old/sandbox)
- [Module 4: Reversing](modules-old/reversing)
- [Module 5: Memory Corruption](modules-old/pwning)
- [Module 6: Format Strings](modules-old/fmt)
- [Module 7: Return Oriented Programming](modules-old/rop)
- [Module 8: Heap Exploitation](modules-old/heap)
- [Module 9: Kernel Security](modules-old/kernel)
