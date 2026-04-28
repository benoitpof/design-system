// Shared topbar navigation — arrows + dropdown — injected into all chart pages
(function () {
  const PAGES = [
    { group: 'Data viz',      num: '02', file: '02-bar.html',      label: '02 · Bar chart' },
    { group: 'Data viz',      num: '03', file: '03-stacked.html',  label: '03 · Stacked bar' },
    { group: 'Data viz',      num: '04', file: '04-grouped.html',  label: '04 · Grouped bar' },
    { group: 'Data viz',      num: '05', file: '05-line.html',     label: '05 · Line chart' },
    { group: 'Data viz',      num: '06', file: '06-donut.html',    label: '06 · Donut chart' },
    { group: 'Data viz',      num: '11', file: '11-sankey.html',   label: '11 · Sankey' },
    { group: 'Data viz',      num: '15', file: '15-radar.html',    label: '15 · Radar' },
    { group: 'Stat & callout',num: '01', file: '01-kpi.html',      label: '01 · KPI cards' },
    { group: 'Stat & callout',num: '07', file: '07-progress.html', label: '07 · Progress' },
    { group: 'Stat & callout',num: '08', file: '08-funnel.html',   label: '08 · Funnel' },
    { group: 'Structure',     num: '09', file: '09-timeline.html', label: '09 · Timeline' },
    { group: 'Structure',     num: '10', file: '10-gantt.html',    label: '10 · Gantt' },
    { group: 'Structure',     num: '12', file: '12-process.html',  label: '12 · Process' },
    { group: 'Structure',     num: '13', file: '13-org.html',      label: '13 · Org chart' },
    { group: 'Data display',  num: '14', file: '14-table.html',    label: '14 · Financial table' },
    { group: 'Data display',  num: '14', file: '14-table-v1.html', label: '14 · Simple table (legacy)' },
    { group: 'Geo',           num: '16', file: '16-map.html',      label: '16 · Maps' },
    { group: 'Library',       num: '17', file: '17-icons.html',    label: '17 · Icon library' },
    { group: 'Library',       num: '18', file: '18-images.html',   label: '18 · Photos & images' },
  ];

  const here = location.pathname.split('/').pop().toLowerCase();
  const currentIdx = PAGES.findIndex(p => p.file.toLowerCase() === here);

  // Build optgroups
  const groups = {};
  PAGES.forEach((p, i) => {
    if (!groups[p.group]) groups[p.group] = [];
    groups[p.group].push({ ...p, idx: i });
  });

  // SVG helpers
  function arrowSVG(dir) {
    const d = dir === 'left'
      ? 'M8.5 3L5 7l3.5 4'
      : 'M5.5 3L9 7l-3.5 4';
    return `<svg width="14" height="14" viewBox="0 0 14 14" fill="none"><path d="${d}" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>`;
  }

  function caretSVG() {
    return `<svg class="nav-select-caret" width="10" height="10" viewBox="0 0 10 10" fill="none"><path d="M2 3.5L5 6.5L8 3.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>`;
  }

  // Build select options
  let optionsHTML = '<option value="" disabled selected>— Aller à une planche —</option>';
  Object.entries(groups).forEach(([grpName, items]) => {
    optionsHTML += `<optgroup label="${grpName}">`;
    items.forEach(p => {
      const sel = p.idx === currentIdx ? ' selected' : '';
      optionsHTML += `<option value="${p.file}"${sel}>${p.label}</option>`;
    });
    optionsHTML += '</optgroup>';
  });

  // Build nav HTML
  const prevDisabled = currentIdx <= 0;
  const nextDisabled = currentIdx >= PAGES.length - 1;

  const navHTML = `
    <nav class="topbar-nav">
      <a class="nav-arrow" id="nav-prev" href="${currentIdx > 0 ? PAGES[currentIdx - 1].file : '../index.html'}" title="Planche précédente"${prevDisabled ? ' style="opacity:.35;pointer-events:none"' : ''}>${arrowSVG('left')}</a>
      <div class="nav-select-wrap">
        <select class="nav-select" id="nav-select">${optionsHTML}</select>
        ${caretSVG()}
      </div>
      <a class="nav-arrow" id="nav-next" href="${currentIdx < PAGES.length - 1 ? PAGES[currentIdx + 1].file : '#'}" title="Planche suivante"${nextDisabled ? ' style="opacity:.35;pointer-events:none"' : ''}>${arrowSVG('right')}</a>
    </nav>`;

  // Inject: replace #types-nav if present, else append to topbar
  const typesNav = document.getElementById('types-nav');
  if (typesNav) {
    typesNav.outerHTML = navHTML;
  } else {
    const topbar = document.querySelector('.topbar');
    if (topbar) topbar.insertAdjacentHTML('beforeend', navHTML);
  }

  // Dropdown change → navigate
  document.addEventListener('change', function (e) {
    if (e.target && e.target.id === 'nav-select') {
      window.location.href = e.target.value;
    }
  });

  // Keyboard shortcuts ← →
  document.addEventListener('keydown', function (e) {
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'SELECT' || e.target.tagName === 'TEXTAREA') return;
    if (e.key === 'ArrowLeft'  && currentIdx > 0)              { e.preventDefault(); window.location.href = PAGES[currentIdx - 1].file; }
    if (e.key === 'ArrowRight' && currentIdx < PAGES.length-1) { e.preventDefault(); window.location.href = PAGES[currentIdx + 1].file; }
  });
})();
