---
layout: page
title: Knowledge Graph
icon: fas fa-project-diagram
order: 7
---

<p class="text-muted mb-3" style="font-size:.9rem;">
  Interactive map of the wiki knowledge base. Each node is a page; edges are backlinks.
  <strong>Click</strong> a node to open the page · <strong>Drag</strong> to explore · <strong>Scroll</strong> to zoom.
</p>

<style>
#wiki-graph-wrap {
  position: relative;
  width: 100%;
  height: 78vh;
  min-height: 480px;
  border: 1px solid var(--border-color, #e9ecef);
  border-radius: .75rem;
  overflow: hidden;
  background: var(--card-bg, #fafafa);
}
#wiki-graph-svg { width: 100%; height: 100%; }
#graph-tooltip {
  position: absolute;
  pointer-events: none;
  background: var(--card-bg, #fff);
  border: 1px solid var(--border-color, #dee2e6);
  border-radius: .4rem;
  padding: .4rem .7rem;
  font-size: .78rem;
  font-weight: 600;
  box-shadow: 0 4px 12px rgba(0,0,0,.12);
  opacity: 0;
  transition: opacity .12s;
  max-width: 220px;
  white-space: normal;
  line-height: 1.35;
  z-index: 10;
}
#graph-legend {
  position: absolute;
  bottom: 12px;
  left: 14px;
  background: var(--card-bg, rgba(255,255,255,.9));
  border: 1px solid var(--border-color, #e9ecef);
  border-radius: .45rem;
  padding: .5rem .75rem;
  font-size: .72rem;
  line-height: 1.8;
  backdrop-filter: blur(4px);
}
#graph-legend .dot {
  display: inline-block;
  width: 10px; height: 10px;
  border-radius: 50%;
  margin-right: 5px;
  vertical-align: middle;
}
#graph-controls {
  position: absolute;
  top: 10px;
  right: 12px;
  display: flex;
  flex-direction: column;
  gap: 4px;
}
#graph-controls button {
  width: 28px; height: 28px;
  border: 1px solid var(--border-color, #dee2e6);
  border-radius: .3rem;
  background: var(--card-bg, #fff);
  font-size: 14px;
  cursor: pointer;
  display: flex; align-items: center; justify-content: center;
  color: var(--text-color, #333);
}
#graph-controls button:hover { background: var(--hover-bg, #f0f0f0); }
</style>

<div id="wiki-graph-wrap">
  <svg id="wiki-graph-svg"></svg>
  <div id="graph-tooltip"></div>
  <div id="graph-controls">
    <button id="btn-zoom-in"  title="Zoom in">+</button>
    <button id="btn-zoom-out" title="Zoom out">−</button>
    <button id="btn-reset"    title="Reset view">⊙</button>
  </div>
  <div id="graph-legend"></div>
</div>

<script src="https://d3js.org/d3.v7.min.js"></script>
<script>
(function () {
  const RAW = {{ site.data.wiki_graph | jsonify }};

  const DOMAIN_COLOR = {
    "AI / LLM":       "#6366f1",
    "C++ / Systems":  "#f59e0b",
    "Architecture":   "#10b981",
    "DevOps":         "#3b82f6",
    "Linux":          "#f97316",
    "Python":         "#8b5cf6",
    "Obsidian":       "#a855f7",
    "PKM":            "#14b8a6",
    "Web":            "#06b6d4",
    "Meta":           "#6b7280",
  };

  const wrap    = document.getElementById("wiki-graph-wrap");
  const svg     = d3.select("#wiki-graph-svg");
  const tooltip = document.getElementById("graph-tooltip");
  const legend  = document.getElementById("graph-legend");

  // Build legend
  const domains = [...new Set(RAW.nodes.map(n => n.domain))].sort();
  legend.innerHTML = domains.map(d =>
    `<div><span class="dot" style="background:${DOMAIN_COLOR[d] || '#999'}"></span>${d}</div>`
  ).join("");

  const W = () => wrap.clientWidth;
  const H = () => wrap.clientHeight;

  // Deep-clone nodes/links so D3 mutation doesn't corrupt RAW
  const nodes = RAW.nodes.map(d => ({ ...d }));
  const nodeById = Object.fromEntries(nodes.map(n => [n.id, n]));
  const links = RAW.links
    .filter(l => nodeById[l.source] && nodeById[l.target])
    .map(l => ({ source: l.source, target: l.target }));

  // Degree for sizing nodes
  const degree = {};
  nodes.forEach(n => { degree[n.id] = 0; });
  links.forEach(l => {
    degree[l.source] = (degree[l.source] || 0) + 1;
    degree[l.target] = (degree[l.target] || 0) + 1;
  });
  const nodeRadius = n => Math.max(6, Math.min(18, 5 + (degree[n.id] || 0) * 1.5));

  const g = svg.append("g");

  // Arrow marker
  svg.append("defs").append("marker")
    .attr("id", "arrow")
    .attr("viewBox", "0 -4 8 8")
    .attr("refX", 18)
    .attr("refY", 0)
    .attr("markerWidth", 6)
    .attr("markerHeight", 6)
    .attr("orient", "auto")
    .append("path")
    .attr("d", "M0,-4L8,0L0,4")
    .attr("fill", "#aaa");

  const link = g.append("g").attr("class", "links")
    .selectAll("line")
    .data(links)
    .join("line")
    .attr("stroke", "#ccc")
    .attr("stroke-width", 1)
    .attr("stroke-opacity", 0.6)
    .attr("marker-end", "url(#arrow)");

  const node = g.append("g").attr("class", "nodes")
    .selectAll("circle")
    .data(nodes)
    .join("circle")
    .attr("r", nodeRadius)
    .attr("fill", n => DOMAIN_COLOR[n.domain] || "#6b7280")
    .attr("stroke", "#fff")
    .attr("stroke-width", 1.5)
    .style("cursor", "pointer")
    .on("mouseover", (event, n) => {
      tooltip.textContent = n.title;
      tooltip.style.opacity = "1";
      d3.select(event.currentTarget).attr("stroke", "#333").attr("stroke-width", 2.5);
    })
    .on("mousemove", (event) => {
      const rect = wrap.getBoundingClientRect();
      let x = event.clientX - rect.left + 14;
      let y = event.clientY - rect.top - 10;
      if (x + 230 > rect.width) x -= 240;
      tooltip.style.left = x + "px";
      tooltip.style.top  = y + "px";
    })
    .on("mouseout", (event) => {
      tooltip.style.opacity = "0";
      d3.select(event.currentTarget).attr("stroke", "#fff").attr("stroke-width", 1.5);
    })
    .on("click", (_, n) => { window.location.href = n.url; })
    .call(d3.drag()
      .on("start", (event, n) => {
        if (!event.active) simulation.alphaTarget(0.3).restart();
        n.fx = n.x; n.fy = n.y;
      })
      .on("drag", (event, n) => { n.fx = event.x; n.fy = event.y; })
      .on("end", (event, n) => {
        if (!event.active) simulation.alphaTarget(0);
        n.fx = null; n.fy = null;
      })
    );

  const simulation = d3.forceSimulation(nodes)
    .force("link",    d3.forceLink(links).id(d => d.id).distance(90).strength(0.4))
    .force("charge",  d3.forceManyBody().strength(-220))
    .force("center",  d3.forceCenter(W() / 2, H() / 2))
    .force("collide", d3.forceCollide().radius(n => nodeRadius(n) + 6))
    .on("tick", () => {
      link
        .attr("x1", d => d.source.x)
        .attr("y1", d => d.source.y)
        .attr("x2", d => d.target.x)
        .attr("y2", d => d.target.y);
      node
        .attr("cx", d => d.x)
        .attr("cy", d => d.y);
    });

  // Zoom
  const zoom = d3.zoom()
    .scaleExtent([0.2, 4])
    .on("zoom", e => g.attr("transform", e.transform));
  svg.call(zoom);

  const zoomBy = factor => svg.transition().duration(250)
    .call(zoom.scaleBy, factor);

  document.getElementById("btn-zoom-in").onclick  = () => zoomBy(1.4);
  document.getElementById("btn-zoom-out").onclick = () => zoomBy(1 / 1.4);
  document.getElementById("btn-reset").onclick    = () =>
    svg.transition().duration(400).call(zoom.transform, d3.zoomIdentity);

  // Re-center force when container resizes
  new ResizeObserver(() => {
    simulation.force("center", d3.forceCenter(W() / 2, H() / 2)).alpha(0.1).restart();
  }).observe(wrap);
})();
</script>
