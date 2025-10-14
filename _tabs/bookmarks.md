---
# the default layout is 'page'
icon: fas fa-bookmark
order: 6
---

<!-- <h1>{{ page.title }}</h1> -->

<input type="text" id="search" placeholder="Search bookmarks..." style="width:100%; padding:8px; margin:12px 0;">

<div id="bookmark-container">
  {% assign bookmarks = site.data.bookmarks %}
  {% include bookmarks.html items=bookmarks %}
</div>

<script>
  const searchInput = document.getElementById('search');
  searchInput.addEventListener('input', () => {
    const q = searchInput.value.toLowerCase();
    document.querySelectorAll('.bookmark').forEach(el => {
      el.style.display = el.innerText.toLowerCase().includes(q) ? '' : 'none';
    });
  });
</script>
