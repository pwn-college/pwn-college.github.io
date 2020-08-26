# Syllabus

This is the syllabus for CSE 466, Fall 2020.

## Course Description

This course will take students through an exploration of the ways that the Security of Computer Systems can fail.
Security is a complicated thing: it is only as strong as its weakest link, and a small, single mistake can often bring down otherwise extremely secure software.

Taking the intuition that, to build secure systems in the future, one must understand how security can break, we will cover a number of different failure modes of compuer systems, ranging from application security to network and operating system security to web security.
Each lecture will consist of an introduction to a new topic, examples of real-world effects of security failures related to the topic, and an assignment for students to explore these concepts.

These assignments will be very thorough, and by the end, students will have an _intuitive_ understand on how to exploit these vulnerabilities, and will have the building blocks needed to prevent them, both in the lab and in the real world.

## Prerequisites

This course will be *EXTREMELY* challenging, and students are expected to learn some of the necessary technologies on their own time.

This course requires a good understanding of low-level computer architecture (for example, students should understand x86 assembly) and low-level programming languages (specifically, C), and good command of a high-level programming language (specifically, Python).
You should have a _very_ good background in operating systems (especially Linux or UNIX variants).
If you do not have these skills, or do not plan on acquiring them very early in the course, you will have a hard time.
A good approximation of the type of material that you will be faced with is the first six levels of the [Vortex wargame](http://overthewire.org/wargames/vortex/).


# Recommended Textbook

There is no recommended textbook for this course.
Any reading material assigned will be from publicly-available sources on the internet.


# Course Communication

All announcements and communications for the class will take place through the class mailing list.
Students are *required* to subscribe to the class mailing list.

Student may use the class mailing list to ask questions or clarifications, and the TA, Instructor, or other students can answer.
Note that sharing solutions or answers is expressly prohibited.

Questions should be emailed to both the TA (connor.d.nelson@asu.edu) and the professor (yans@asu.edu), for example, via [this link](mailto:pwn-college@asu.edu).
Questions meant just for the professor should be addressed to the following email address: yans@asu.edu.

If at all possible, please use the mailing list for communication to the professor or the TAs, unless the communication is private.
This way, the entire class will benefit from your question.
Note that if we deem it necessary and helpful, we will CC the class mailing list when replying to direct emails.

# Course Topics

The course will consist of modules about:

* Linux operating system fundamentals, program misuse and privilege escalation.
* Sandboxes and sandbox failures.
* Program reverse engineering.
* Traditional memory corruption (buffer overflows).
* Binary code injection.
* Advanced exploitation scenarios.
* If we have time, some of:
   * Modern cryptographic security.
   * Content injection beyond binary code.
   * Security of machine learning and AI.
   * Serialization vulnerabilities.
   * OS kernel exploitation.
   * Automating bug hunting.

Each module will take one week, with several breaks throughout the semester for review, catch-up, and voting.

# Assessment

## Assignments only, no exams or quizzes.

Students will be evaluated on their performance on between 7 and 14 equally-weighted homework assignments.

## Assignment timing.

Assignments will be released at the end of class.
There will be no more than one assignment live at a time.
Assignments will normally be due at 3pm, one week after they are assigned (i.e., a homework assigned at the end of class on Wednesday would normally be due at 3pm the next Wednesday).
All grading is done automatically through flag submissions, and *late submissions will not be accepted under any circumstances*.

## Challenge-based assignments with flags as rewards.

Each assignment will consist of a large amount of varied, but slightly similar challenges, and will be live for between one and two weeks.
Solving these challenges may require the use or implementation of fairly complex hacking tools.
Solving each individual challenge will grant a _challenge-specific_ passcode, called a "flag".
The maximum number of flags possible to score for an assignment is equal to the maximum number of challenges in the assignment.

The existence of flags means that _there is no wrong way to solve a challenge_.
If you tricked the challenge into giving you the valid flag, good job.

## Converting flags to grades.

For each assignment, a student's grade is the ratio of the flags they earn out of the possible flags, scaled to 100%.
If a student earns 70 flags from 70 challenges on an assignment (yes, assignments may be this big), they will receive 100%.
If they earn 50 flags out of 70 possible ones, they will get 71% on the assignment.

## Extra credit: CTFs

There are cybersecurity competitions being held every weekend.
Every weekend, during the semester, you and your friends can participate in one CTF and earn one percentage point bonus in the course.
Teams can be anywhere from a minimum of 4 players to a maximum of 8 players.
Each player will have to submit a writeup about what they worked on during the weekend, what they solved, and what they learned.
Solving is not necessary, but participation is.

A maximum of 14% extra credit is possible with this method, bringing the total achievable points so far to 114%.

## More extra credit: bug bounty program.

Any *responsibly-disclosed* _serious_ security issues in course infrastructure will earn an extra 5 to 50 "bug bounty" _percentage points_ for the current assignment, for a theoretical maximum of 150% for the assignment, depending on the severity of the issue.
Blatantly spurtious reports may earn a *negative* percentage report of up to -15 percentage points.
Allowances will be made for honest mistakes leading to a spurtious bug bounty filing, but don't waste our time on purpose.

## More extra credit: making up missed challenges.

On the last day of the course, we will calculate the grade of an aggregate assignment comprising of all challenges ever released.
This way, if you didn't manage to solve a given challenge of a module before the deadline, you'll have an extra chance to do so at the end for some partial credit.

## Final grade calculation.

The final grade will be calculated by averaging the grades of each homework assignment, equally weighted.
For example, if there are 10 assignments, and a student scores 100% on each assignment and participates in a CTF every weekend, they will score 114%.
If they score 100% on each assignment and ignore CTFs, they will score 100%.
If they score 100% on each assignment except for one assignment that they blow off completely, they will get a grade of 90%.

Percentages will be translated to letter grades with the following initial cutoffs:

| Percentage Grade | Letter Grade |
|------------------|--------------|
| >= 99            | A+           |
| >= 92            | A            |
| >= 90            | A-           |
| >= 88            | B+           |
| >= 82            | B            |
| >= 80            | B-           |
| >= 78            | C+           |
| >= 70            | C            |
| >= 60            | D            |
| < 60             | E            |

With the exception of the cutoff for A+, these cutoffs can be curved _downward_ in the event that students do worse than expected.
That is, if you earn an 88% in the course, you are guaranteed at least a B+, but if everyone else does super poorly, the curve might pull you up to an A, but never an A+.
Updates on the theme of "what would the cutoffs be if the course ended today" will be provided at the conclusion of each assignment.

# Special Accommodations

Students requesting disability accommodations should register with the Disability Resource Center (DRC) and present the instructor with appropriate documentation from the DRC.

# Plagiarism and Cheating

Plagiarism or any form of cheating in assignments or projects is subject to serious academic penalty. To understand your responsibilities as a student read: [ASU Student Code of Conduct](http://www.asu.edu/aad/manuals/usi/usi104-01.html) and [ASU Student Academic Integrity Policy](http://provost.asu.edu/academicintegrity/policy).
There is a zero tolerance policy in this class: any violation of the academic integrity policy will result in a zero on the assignment and the violation will be reported to the Dean’s office.
Plagiarism is taken very seriously in this course.

Examples of academic integrity violations include (but are not limited to):

- Sharing code with a fellow student (even if it’s only a few lines).
- Collaborating on code with a fellow student (unless explicitly allowed).
- Using another students solution to solve a challenge and get a flag.
- Sharing a flag with another student (NEVER ALLOWED UNDER ANY CIRCUMSTANCES).

Posting your assignment solutions online _before the due date of the assignment_ is expressly forbidden, and will be considered a violation of the academic integrity policy.
Note that this includes working out of a public Github repository.
The [Github Student Developer Pack](https://education.github.com/pack) provides unlimited private repositories while you are a student, making it easy to begin with a private GitHub repository and easily make it public after the assignment deadline.

**Collaboration policy:** New this year: we will set aside the last hour of class for _active collaboration time_ for students. We will split up the class into groups, randomly, and you may freely collaborate on solutions during class time. Be extremely careful not to share code or flags (ESPECIALLY flags); only ideas.

# Syllabus Update

Information in the syllabus may be subject to change with reasonable advance notice and an email to the class mailing list.

# Misc

Syllabus copyright 2020 Yan Shoshitaishvili, along with all lectures and course-related written materials.
During this course students are prohibited from making audio, video, digital, or other recordings during class, or selling notes to or being paid for taking notes by any person or commercial firm without the express written permission of the faculty member teaching this course.
Be reasonable.

Title IX is a federal law that provides that no person be excluded on the basis of sex from participation in, be denied benefits of, or be subjected to discrimination under any education program or activity.  Both Title IX and university policy make clear that sexual violence and harassment based on sex is prohibited.  An individual who believes they have been subjected to sexual violence or harassed on the basis of sex can seek support, including counseling and academic support, from the university.  If you or someone you know has been harassed on the basis of sex or sexually assaulted, you can find information and resources at https://sexualviolenceprevention.asu.edu/faqs. 

 As a mandated reporter, I am obligated to report any information I become aware of regarding alleged acts of sexual discrimination, including sexual violence and dating violence. ASU Counseling Services, https://eoss.asu.edu/counseling, is available if you wish discuss any concerns confidentially and privately.


