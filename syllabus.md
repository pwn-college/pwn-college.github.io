# Syllabus

This is the syllabus for CSE 466, Fall 2018.

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

Questions should be emailed to both the TA (connor.d.nelson@asu.edu) and the professor (yans@asu.edu), for example, via [this link](mailto:connor.d.nelson@asu.edu?&cc=yans@asu.edu&subject=Question%20about%20CSE466).
Questions meant just for the professor should be addressed to the following email address: yans@asu.edu.

If at all possible, please use the mailing (cse-466@googlegroups.com) list for communication to the professor or the TAs, unless the communication is private.
This way, the entire class will benefit from your question.
Note that if we deem it necessary and helpful, we will CC the class mailing list when replying to direct emails.

# Course Topics

The course will consist of weekly modules about:

* Linux operating system fundamentals, program misuse and privilege escalation.
* Linux system call filtering and abuse.
* Sandboxes and sandbox failures.
* Serialization vulnerabilities.
* Program reverse engineering.
* Traditional memory corruption (buffer overflows).
* Binary code injection.
* Advanced exploitation scenarios.
* Modern symmetric encryption security.
* Modern asymmetric encryption security.
* Content injection beyond binary code.

In addition, there will be a review/midterm week and a review/finals week.
There is a buffer to spend two weeks on one module (most likely, advanced exploitation scenarios).

# Assessment

Students will be evaluated on their performance on 13 equal one-week homework assignments, a one-week take-home midterm exam, and a one-week takehome final exam.
Each assignment will consist of a large amount of varied, but slightly similar challenges.
Exams will consist of a large amount of different challenges seen in previous assignments.
Solving these challenges may require the use or implementation of fairly complex hacking tools.
Solving each individual challenge will grant a _student- and challenge-specific_ passcode, called a "flag".
Redemption of this flag will count toward some amount of _points_, depending on the assignment.

For each assignment, earned points map to a _percent_ that directly impacts the student's grade, from 0 to 110 _percent_.
70 _percent_ is a 1:1 mapping from points: that is, every student to get 70 points on an assignment is guaranteed to get 70 _percent_ from that assignment toward their final score.
The other 40 percent (to a maximum of 110) is awarded on a curve, with students receiving anywhere from 0 to 40 percent based on their performance compared to other students.
These percentages will be assigned by sorting students (with more than 70 points) by their point amount and giving the top student 40 points, the next 39, and so on.
If several students tie for a spot, they will both receive that amount of points.
If fewer than 40 students have more than 70 points, the slots will be awarded in descending order from the maximum point value.
For example, if only four students have more than 70 points, the top will get 110 points, the next 109, the next 108, and the last 107.

Each homework assignment will have some amount of percent (between 0 and 10) that will _only_ be redeemable in the last hour of class, after the end of the lecture component, after the homework is assigned.
If you miss class, you will have to make up for this lost percentage by getting 110 percent on a future next assignment.

Additionally, any *responsibly-disclosed* serious security issues in course infrastructure will earn an extra 5 to 50 "bug bounty" _percent_, depending on the severity of the issue.
Spurtious reports may earn a *negative* percentage report of up to -15 _percent_.
Don't waste our time.

The percentages from each homework, midterm, and exam will be equally weighted.
Each student's final grade will be the sum of their accumulated percentages across assignments and exams (where the maximum is 1650 percent plus any extra bug bounty percentages) divided by 1500 percent.
This translates to a letter grade range of:

| Score | Letter Grade |
|-------|--------------|
| >= 99 | A+           |
| >= 92 | A            |
| >= 90 | A-           |
| >= 88 | B+           |
| >= 82 | B            |
| >= 80 | B-           |
| >= 78 | C+           |
| >= 70 | C            |
| >= 60 | D            |
| < 60  | E            |

## Homework Due Dates

Homework will be assigned toward the end of each class every week, and will be due noon before the next class.
All grading is done automatically through flag submissions, and *late submissions will not be accepted under any circumstances*.

## Special Accommodations

Students requesting disability accommodations should register with the Disability Resource Center (DRC) and present the instructor with appropriate documentation from the DRC.

## Plagiarism and Cheating

Plagiarism or any form of cheating in assignments or projects is subject to serious academic penalty. To understand your responsibilities as a student read: [ASU Student Code of Conduct](http://www.asu.edu/aad/manuals/usi/usi104-01.html) and [ASU Student Academic Integrity Policy](http://provost.asu.edu/academicintegrity/policy).
There is a zero tolerance policy in this class: any violation of the academic integrity policy will result in a zero on the assignment and the violation will be reported to the Dean’s office.
Plagiarism is taken very seriously in this course.

Examples of academic integrity violations include (but are not limited to):

- Sharing code with a fellow student (even if it’s only a few lines).
- Collaborating on code with a fellow student (unless explicitly allowed).
- Using another students solution to solve a challenge and get a flag.

Posting your assignment solutions online _before the due date of the assignment_ is expressly forbidden, and will be considered a violation of the academic integrity policy.
Note that this includes working out of a public Github repository.
The [Github Student Developer Pack](https://education.github.com/pack) provides unlimited private repositories while you are a student, making it easy to begin with a private GitHub repository and easily make it public after the assignment deadline.

# Syllabus Update

Information in the syllabus may be subject to change with reasonable advance notice and an email to the class mailing list.

# Misc

This syllabus based on the syllabi of Adam Doupé (with permission).
Otherwise copyright 2017 Yan Shoshitaishvili, along with all lectures and course-related written materials.
During this course students are prohibited from making audio, video, digital, or other recordings during class, or selling notes to or being paid for taking notes by any person or commercial firm without the express written permission of the faculty member teaching this course.
Be reasonable.

Title IX is a federal law that provides that no person be excluded on the basis of sex from participation in, be denied benefits of, or be subjected to discrimination under any education program or activity.  Both Title IX and university policy make clear that sexual violence and harassment based on sex is prohibited.  An individual who believes they have been subjected to sexual violence or harassed on the basis of sex can seek support, including counseling and academic support, from the university.  If you or someone you know has been harassed on the basis of sex or sexually assaulted, you can find information and resources at https://sexualviolenceprevention.asu.edu/faqs. 

 As a mandated reporter, I am obligated to report any information I become aware of regarding alleged acts of sexual discrimination, including sexual violence and dating violence. ASU Counseling Services, https://eoss.asu.edu/counseling, is available if you wish discuss any concerns confidentially and privately.


