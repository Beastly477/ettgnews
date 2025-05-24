const mapSvgContainer = document.getElementById('map-svg-container');
const detailsBox = document.getElementById('details-box');
const TOOLTIP_OFFSET_Y = 20;

if (mapSvgContainer && detailsBox) {
  mapSvgContainer.addEventListener('mouseover', function (e) {
    // Look for any SVG element with data-id (path, g, rect, etc.)
    const stateEl = e.target.closest('[data-id]');
    if (stateEl && mapSvgContainer.contains(stateEl)) {
      const content = stateEl.dataset.name || '';
      detailsBox.innerHTML = content;
      detailsBox.style.opacity = "100%";
    } else {
      detailsBox.style.opacity = "0%";
    }
  });

  mapSvgContainer.addEventListener('click', function (e) {
    const stateEl = e.target.closest('[data-id]');
    if (stateEl && mapSvgContainer.contains(stateEl)) {
      const stateName = stateEl.dataset.name;
      if (stateName) {
        const slug = stateName.toLowerCase().replace(/\s+/g, '-');
        window.location.href = `/states/${slug}`;
      }
    }
  });

  window.addEventListener('mousemove', function (e) {
    detailsBox.style.top = (e.clientY + TOOLTIP_OFFSET_Y) + 'px';
    detailsBox.style.left = (e.clientX) + 'px';
  });
} else {
  console.warn('Map SVG container or details box not found.');
}

console.log('map loaded');