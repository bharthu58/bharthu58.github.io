---
# the default layout is 'page'
icon: fas fa-bookmark
title: C++ Links
permalink: /cpp-links/
---

<div class="cpp-links">
  <ul>
  {% for link in site.data.cpp_links %}
    <li>
      <strong>{{ link.name }}</strong> — 
      <a href="{{ link.url }}" target="_blank">{{ link.url }}</a>
    </li>
  {% endfor %}
  </ul>
</div>

<style>
.cpp-links {
  background: #fffaf0;
  border-radius: 12px;
  padding: 2rem;
  box-shadow: 0 4px 10px rgba(0,0,0,0.05);
}
</style>
---