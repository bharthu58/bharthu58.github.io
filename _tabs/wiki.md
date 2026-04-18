---
layout: page
title: Wiki
icon: fas fa-book
order: 6
---

Personal knowledge base synthesised from notes, articles, and research sessions.
Covers AI/LLM, C++/systems programming, DevOps, Linux, Python, and Obsidian tooling.

---

{% assign wiki_pages = site.wiki | sort: 'title' %}
{% for p in wiki_pages %}
- [{{ p.title }}]({{ p.url }})
{% endfor %}
