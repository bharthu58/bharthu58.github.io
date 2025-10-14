---
# the default layout is 'page'
icon: fas fa-external-link
order: 5
---

<!-- <h1>{{ page.title }}</h1> -->

<input type="text" id="search" placeholder="Search bookmarks..." style="width: 100%; padding: 8px; margin: 12px 0;">

<div id="tags"></div>

<ul id="bookmark-list">
  {% for item in site.data.references %}
    <li class="reference" data-tags="{{ item.tags | join: ' ' }}">
      <a href="{{ item.url }}" target="_blank">{{ item.title }}</a>
      <p>{{ item.description }}</p>
      <small>Tags: {{ item.tags | join: ', ' }}</small>
    </li>
  {% endfor %}
</ul>

<script>
  const searchInput = document.getElementById('search');
  const bookmarks = document.querySelectorAll('.bookmark');

  // Collect tags
  const tagSet = new Set();
  bookmarks.forEach(b => {
    b.dataset.tags.split(' ').forEach(tag => tagSet.add(tag));
  });

  // Render tag buttons
  const tagsDiv = document.getElementById('tags');
  tagSet.forEach(tag => {
    const btn = document.createElement('button');
    btn.textContent = tag;
    btn.onclick = () => filterByTag(tag);
    tagsDiv.appendChild(btn);
  });

  function filterByTag(tag) {
    bookmarks.forEach(b => {
      b.style.display = b.dataset.tags.includes(tag) ? '' : 'none';
    });
  }

  // Search filter
  searchInput.addEventListener('input', () => {
    const q = searchInput.value.toLowerCase();
    bookmarks.forEach(b => {
      const text = b.innerText.toLowerCase();
      b.style.display = text.includes(q) ? '' : 'none';
    });
  });
</script>

