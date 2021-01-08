---
---

# The Belted

The hacker ethos goes beyond the acquisition of a satisfactory grade in a college course.
A true hacker is never satisfied with the state of their knowledge.
They strive, or are irresistably driven towards, the achievement of absolute mastery of technical topics.

Below is a list of true hackers: those who stared at the yellow box, and rather than flinching, dove in.

## Blue Belts

For demonstrating hacker mastery in the completion of all active challenges on pwn.college, the following individuals have been awarded the rank of BLUE BELT.

{% for element in site.data.blue %}
{% assign belt = element[1] %}
- {{ belt.handle | escape }} {% if belts.name %}({{ belts.name }}){% endif %} {{ belt.emoji }} {% if belts.site %}[site]({{ belts.site }}){% endif %} {% if belts.mail %}[mail](mailto:{{ belts.mail }}){% endif %} *(ascended {{ belt.date | date: "%Y-%m-%d" }})*
{% endfor %}

## Yellow Belts

Like saplings that shall one day grow into mighty trees, the following individuals have built their foundation of hacking knowledge, earning rank of YELLOW BELT.

- holocircuit 👑 [web](https://holocircuit.github.io/) *(ascended 10/12/2020)*
- propio (Mohammad Saboor) 😑 [mail] (mailto:msaboor35@gmail.com) *(ascended 10/18/2020)*
- Pascal0x90 (Nathan) 🍞 [mail](mailto:pascal-0x90@protonmail.com) [web](https://twitter.com/Pascal_0x90) *(ascended 10/20/2020)*
- Narnix 🙃 [mail](mailto:xxie29@asu.edu) *(ascended 11/4/2020)*
- qrla (Carla) 🥺 [mail](mailto:loresfca.flores1@gmail.com) [web](https://carla.is.mad.af/) *(ascended 11/16/2020)*
- Cascadian (Steven Peterson) [mail](mailto:scpeter9@asu.edu) *(ascended 12/7/2020)*
- codacker (Sunny Mishra) 😏 [mail](mailto:mishrasunny174@gmail.com) [web](https://mishrasunny174.tech) *(ascended 12/13/2020)*

## How to get on the above lists

You, too, can be listed among the legends above.
For your yellow belt, complete all pwn.college challenges through the Exploitation module.
For your blue belt, complete all active pwn.college challenges.
Once you fulfil the requirements for a belt, [email us](mailto:pwn-college@asu.edu) from the email address associated with your pwn.college account to request your belt and inclusion on this page.
