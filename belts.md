---
---

# The Belted

The hacker ethos goes beyond the acquisition of a satisfactory grade in a college course.
A true hacker is never satisfied with the state of their knowledge.
They strive, or are irresistably driven towards, the achievement of absolute mastery of technical topics.

Below is a list of true hackers: those who stared at the yellow box, and rather than flinching, dove in.

## Blue Belts

For demonstrating hacker mastery in the completion of all active challenges on pwn.college, the following individuals have been awarded the rank of BLUE BELT.

<ul>
{% for element in site.data.blue %}
{% assign belt = element[1] %}
  <li>
    <raw>{{ belt.handle | xml_escape }}</raw>
    {% if belts.name %}({{ belts.name }}){% endif %}
    {% if belts.emoji %}{{ belt.emoji }}{% endif %}
    {% if belts.site %}<a href="{{ belts.site }}">site</a>{% endif %}
    {% if belts.mail %}<a href="mailto:{{ belts.mail }}">mail</a>{% endif %}
    <em>(ascended {{ belt.date | date: "%Y-%m-%d" }})</em>
  </li>
{% endfor %}
</ul>

## Yellow Belts

Like saplings that shall one day grow into mighty trees, the following individuals have built their foundation of hacking knowledge, earning rank of YELLOW BELT.

<ul>
{% for element in site.data.yellow %}
{% assign belt = element[1] %}
  <li>
    <raw>{{ belt.handle | xml_escape }}</raw>
    {% if belts.name %}({{ belts.name }}){% endif %}
    {% if belts.emoji %}{{ belt.emoji }}{% endif %}
    {% if belts.site %}<a href="{{ belts.site }}">site</a>{% endif %}
    {% if belts.mail %}<a href="mailto:{{ belts.mail }}">mail</a>{% endif %}
    <em>(ascended {{ belt.date | date: "%Y-%m-%d" }})</em>
  </li>
{% endfor %}
</ul>

## How to get on the above lists

You, too, can be listed among the legends above.
For your yellow belt, complete all pwn.college challenges through the Exploitation module.
For your blue belt, complete all active pwn.college challenges.
Once you fulfil the requirements for a belt, [email us](mailto:pwn-college@asu.edu) from the email address associated with your pwn.college account to request your belt and inclusion on this page.
