---
layout: page
title: Wiki
icon: fas fa-book
order: 6
---

<p class="lead text-muted mb-4">Personal knowledge base synthesised from notes, articles, and research sessions.</p>

<div class="d-flex flex-wrap gap-2 mb-4">
  <a href="/wiki-graph/" class="btn btn-sm btn-outline-primary">
    <i class="fas fa-project-diagram me-1"></i> Knowledge Graph
  </a>
</div>

<style>
.wiki-domain { margin-bottom: 2.5rem; }
.wiki-domain h3 {
  font-size: 1rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: .06em;
  color: var(--text-muted-color, #6c757d);
  border-bottom: 2px solid var(--border-color, #e9ecef);
  padding-bottom: .4rem;
  margin-bottom: 1rem;
}
.wiki-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: .75rem;
}
.wiki-card {
  display: block;
  padding: .75rem 1rem;
  border: 1px solid var(--border-color, #e9ecef);
  border-radius: .5rem;
  text-decoration: none !important;
  transition: border-color .15s, box-shadow .15s, transform .15s;
  background: var(--card-bg, #fff);
}
.wiki-card:hover {
  border-color: var(--link-color, #4a9eff);
  box-shadow: 0 2px 8px rgba(0,0,0,.08);
  transform: translateY(-1px);
}
.wiki-card-title {
  font-size: .875rem;
  font-weight: 600;
  color: var(--heading-color, #2d2d2d);
  line-height: 1.3;
}
.wiki-domain-badge {
  display: inline-block;
  font-size: .7rem;
  font-weight: 600;
  padding: .15rem .5rem;
  border-radius: 999px;
  margin-bottom: .35rem;
}
</style>

{% assign domain_order = "AI / LLM,C++ / Systems,Architecture,DevOps,Linux,Python,Obsidian,PKM,Web,Meta" | split: "," %}
{% assign domain_icons = "fas fa-robot,fas fa-microchip,fas fa-sitemap,fas fa-tools,fab fa-linux,fab fa-python,fas fa-vault,fas fa-brain,fas fa-globe,fas fa-tag" | split: "," %}
{% assign domain_colors = "#6366f1,#f59e0b,#10b981,#3b82f6,#f97316,#8b5cf6,#a855f7,#14b8a6,#06b6d4,#6b7280" | split: "," %}

{% for domain in domain_order %}
  {% assign idx = forloop.index0 %}
  {% assign icon = domain_icons[idx] %}
  {% assign color = domain_colors[idx] %}
  {% assign pages = site.wiki | where: "domain", domain | sort: "title" %}
  {% if pages.size > 0 %}
<div class="wiki-domain">
  <h3><i class="{{ icon }}" style="color:{{ color }};margin-right:.4rem;"></i>{{ domain }}</h3>
  <div class="wiki-grid">
    {% for p in pages %}
    <a href="{{ p.url }}" class="wiki-card">
      <div class="wiki-card-title">{{ p.title | remove: "AI — " | remove: "C++ — " | remove: "Architecture — " | remove: "DevOps — " | remove: "Linux — " | remove: "Python — " | remove: "Obsidian — " | remove: "PKM — " | remove: "WEB — " }}</div>
    </a>
    {% endfor %}
  </div>
</div>
  {% endif %}
{% endfor %}
