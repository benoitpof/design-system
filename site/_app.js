/* POF Design System — shared client app
 * Loads repo tree once via GitHub API, caches in sessionStorage.
 * Builds consistent topbar nav across all pages.
 * Provides helpers for cards, dynamic counts, markdown viewing.
 *
 * Source of truth = main branch on benoitpof/design-system.
 * Pages auto-update on every visit (no CI required for content changes).
 */
(function (global) {
  'use strict';

  const REPO = 'benoitpof/design-system';
  const BRANCH = 'main';
  const API_TREE = `https://api.github.com/repos/${REPO}/git/trees/${BRANCH}?recursive=1`;
  const API_BRANCH = `https://api.github.com/repos/${REPO}/branches/${BRANCH}`;
  const RAW = (path, ref) => `https://raw.githubusercontent.com/${REPO}/${ref || BRANCH}/${path}`;
  const BLOB = (path, ref) => `https://github.com/${REPO}/blob/${ref || BRANCH}/${path}`;
  const TREE_VIEW = (path, ref) => `https://github.com/${REPO}/tree/${ref || BRANCH}/${path}`;

  const TREE_CACHE_KEY = 'pof_ds_tree_v1';
  const TREE_CACHE_TTL = 30 * 60 * 1000;        // 30 min — fresh cache
  const TREE_CACHE_FALLBACK_TTL = 7 * 24 * 60 * 60 * 1000; // 7 days — fallback if API rate-limited

  // ----------- LOG -----------
  const log = (...args) => console.log('[pof-ds]', ...args);
  const err = (...args) => console.error('[pof-ds]', ...args);

  // ----------- TREE -----------
  let _treePromise = null;

  function readCache(storage) {
    try {
      const raw = storage.getItem(TREE_CACHE_KEY);
      return raw ? JSON.parse(raw) : null;
    } catch (e) { return null; }
  }
  function writeCache(storage, payload) {
    try { storage.setItem(TREE_CACHE_KEY, JSON.stringify(payload)); } catch (e) {}
  }

  async function loadTree(force = false) {
    if (_treePromise && !force) return _treePromise;
    _treePromise = (async () => {
      // 1) Fresh cache (sessionStorage > localStorage)
      const ssCache = readCache(sessionStorage);
      if (ssCache && !force && Date.now() - ssCache.t < TREE_CACHE_TTL) {
        log('tree from session cache,', ssCache.tree.length, 'entries');
        return ssCache;
      }
      const lsCache = readCache(localStorage);
      if (lsCache && !force && Date.now() - lsCache.t < TREE_CACHE_TTL) {
        log('tree from local cache (fresh),', lsCache.tree.length, 'entries');
        writeCache(sessionStorage, lsCache);
        return lsCache;
      }

      // 2) Fetch live
      log('fetching tree from API…');
      try {
        const r = await fetch(API_TREE, { headers: { Accept: 'application/vnd.github+json' } });
        if (!r.ok) {
          const remaining = r.headers.get('x-ratelimit-remaining');
          const resetEpoch = r.headers.get('x-ratelimit-reset');
          throw new Error(`HTTP ${r.status}${remaining === '0' ? ' (rate limit reached, resets at ' + new Date(+resetEpoch * 1000).toLocaleTimeString() + ')' : ''}`);
        }
        const data = await r.json();
        if (data.truncated) err('WARNING: tree truncated, some files missing');
        const payload = { t: Date.now(), sha: data.sha, tree: data.tree };
        writeCache(sessionStorage, payload);
        writeCache(localStorage, payload);
        log('tree fetched,', data.tree.length, 'entries, sha', data.sha.slice(0, 7));
        return payload;
      } catch (e) {
        err('tree fetch failed:', e.message);
        // 3) Fallback: stale localStorage if available (up to FALLBACK_TTL)
        if (lsCache && Date.now() - lsCache.t < TREE_CACHE_FALLBACK_TTL) {
          err('using stale localStorage cache,', lsCache.tree.length, 'entries (sha', lsCache.sha?.slice(0,7), ')');
          return { ...lsCache, stale: true, fetchError: e.message };
        }
        // 4) Hard fail
        return { t: Date.now(), sha: null, tree: [], fetchError: e.message };
      }
    })();
    return _treePromise;
  }

  // ----------- TREE QUERIES -----------
  function listDir(tree, path) {
    // path = "examples/charts" → return immediate children only
    const prefix = path ? path + '/' : '';
    const seen = new Set();
    const out = [];
    for (const e of tree) {
      if (!e.path.startsWith(prefix)) continue;
      const rest = e.path.slice(prefix.length);
      if (!rest || rest.includes('/') === false) {
        // direct child
        if (!seen.has(e.path)) { seen.add(e.path); out.push(e); }
      } else {
        // grandchild → mark first segment as a dir
        const seg = rest.split('/')[0];
        const dirPath = prefix + seg;
        if (!seen.has(dirPath)) {
          seen.add(dirPath);
          out.push({ path: dirPath, type: 'tree', synthesized: true });
        }
      }
    }
    return out.sort((a, b) => {
      if (a.type !== b.type) return a.type === 'tree' ? -1 : 1;
      return a.path.localeCompare(b.path);
    });
  }

  function findExact(tree, path) {
    return tree.find(e => e.path === path);
  }

  function listRecursive(tree, path) {
    const prefix = path ? path + '/' : '';
    return tree.filter(e => e.path.startsWith(prefix) && e.type === 'blob');
  }

  function countIn(tree, path, predicate) {
    const items = path ? listRecursive(tree, path) : tree.filter(e => e.type === 'blob');
    return predicate ? items.filter(predicate).length : items.length;
  }

  // ----------- TOPBAR -----------
  const NAV_ITEMS = [
    { href: 'index.html',    label: 'Overview' },
    { href: 'tree.html',     label: 'Tree' },
    { href: 'examples.html', label: 'Examples' },
    { href: 'assets.html',   label: 'Assets' },
    { href: 'charts.html',   label: 'Charts' },
    { href: 'maps.html',     label: 'Maps' },
    { href: 'icons.html',    label: 'Icons' }
  ];

  function injectTopbar(opts = {}) {
    const here = (location.pathname.split('/').pop() || 'index.html').toLowerCase();
    const breadcrumb = opts.breadcrumb || 'Design System';
    const version = opts.version || 'v4.0.1';
    const logoSrc = RAW('assets/logos/pof-logo-navy.svg');

    const links = NAV_ITEMS.map(it => {
      const active = it.href.toLowerCase() === here ? ' class="active"' : '';
      return `<a href="${it.href}"${active}>${it.label}</a>`;
    }).join('');

    const html = `
<div class="topbar">
  <a class="brand" href="index.html"><img src="${logoSrc}" alt="POF" onerror="this.style.display='none'"></a>
  <span class="crumbs">${escapeHtml(breadcrumb)}</span>
  <span class="version" id="ds-version">${escapeHtml(version)}</span>
  <nav class="topbar-nav">
    ${links}
    <a href="https://github.com/${REPO}" target="_blank" rel="noopener">GitHub ↗</a>
  </nav>
</div>`;

    const mount = document.getElementById('topbar-mount');
    if (mount) {
      mount.outerHTML = html;
    } else {
      document.body.insertAdjacentHTML('afterbegin', html);
    }
  }

  // ----------- FOOTER -----------
  function injectFooter() {
    const html = `
<footer class="ds-footer">
  POF Design System · auto-aligned to <a href="https://github.com/${REPO}/tree/${BRANCH}" target="_blank" rel="noopener">${REPO}@${BRANCH}</a>
  · <a href="#" id="ds-refresh">refresh</a>
  · <span id="ds-tree-info">loading…</span>
</footer>`;
    const mount = document.getElementById('footer-mount');
    if (mount) mount.outerHTML = html;
    else document.body.insertAdjacentHTML('beforeend', html);

    document.getElementById('ds-refresh')?.addEventListener('click', e => {
      e.preventDefault();
      sessionStorage.removeItem(TREE_CACHE_KEY);
      location.reload();
    });

    loadTree().then(t => {
      const el = document.getElementById('ds-tree-info');
      if (!el) return;
      if (!t.sha && !t.tree.length) {
        el.innerHTML = '<span style="color:var(--coral)">tree fetch failed' + (t.fetchError ? ': ' + escapeHtml(t.fetchError) : '') + ' — refresh in a few minutes.</span>';
      } else {
        const fresh = (Date.now() - t.t) < TREE_CACHE_TTL;
        const tag = t.stale ? ' · <span style="color:var(--coral)">stale (offline cache)</span>' : (fresh ? '' : ' · refreshing…');
        el.innerHTML = `${t.tree.length} entries · sha ${t.sha ? t.sha.slice(0,7) : '?'}${tag}`;
      }
    });
  }

  // ----------- CARDS HELPERS -----------
  function escapeHtml(s) {
    return String(s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  }

  function renderEmpty(container, msg) {
    container.innerHTML = `<div class="empty-state">${escapeHtml(msg)}</div>`;
  }

  function renderError(container, msg) {
    container.innerHTML = `<div class="error-state">⚠ ${escapeHtml(msg)}</div>`;
  }

  function renderLoading(container) {
    container.innerHTML = `<div class="loading-state">Loading…</div>`;
  }

  // ----------- MARKDOWN -----------
  let _markedReady = null;
  function ensureMarked() {
    if (_markedReady) return _markedReady;
    _markedReady = new Promise((resolve, reject) => {
      if (global.marked) return resolve(global.marked);
      const s = document.createElement('script');
      s.src = 'https://cdn.jsdelivr.net/npm/marked@11/marked.min.js';
      s.onload = () => resolve(global.marked);
      s.onerror = () => reject(new Error('marked load failed'));
      document.head.appendChild(s);
    });
    return _markedReady;
  }

  async function fetchRaw(path) {
    const r = await fetch(RAW(path));
    if (!r.ok) throw new Error('HTTP ' + r.status + ' on ' + path);
    return r.text();
  }

  async function renderMarkdownInto(path, container) {
    try {
      renderLoading(container);
      const [marked, text] = await Promise.all([ensureMarked(), fetchRaw(path)]);
      // Configure marked: GFM, breaks, base URL for relative links
      marked.use({
        gfm: true,
        breaks: false,
        renderer: {
          link(token) {
            // marked v11 passes a token object — destructure defensively
            const href = (token && (token.href ?? token.url)) || '';
            const title = (token && token.title) || '';
            const text = (token && (token.text ?? token.raw)) || '';
            if (!href) return text;
            const isExt = /^(https?:|mailto:|#)/.test(href);
            let out;
            try {
              if (isExt) {
                out = href;
              } else if (/\.md$/i.test(href)) {
                const baseDir = path.split('/').slice(0, -1).join('/');
                const resolved = resolvePath(baseDir, href);
                out = `docs.html?path=${encodeURIComponent(resolved)}`;
              } else if (/\.(html|htm)$/i.test(href)) {
                const baseDir = path.split('/').slice(0, -1).join('/');
                const resolved = resolvePath(baseDir, href);
                out = `view.html?path=${encodeURIComponent(resolved)}`;
              } else {
                const baseDir = path.split('/').slice(0, -1).join('/');
                const resolved = resolvePath(baseDir, href);
                out = BLOB(resolved);
              }
            } catch (e) {
              out = href;
            }
            const t = title ? ` title="${escapeHtml(title)}"` : '';
            const ext = isExt ? ' target="_blank" rel="noopener"' : '';
            return `<a href="${escapeHtml(out)}"${t}${ext}>${text}</a>`;
          },
          image(token) {
            const href = (token && (token.href ?? token.url)) || '';
            const title = (token && token.title) || '';
            const text = (token && (token.text ?? '')) || '';
            let src = href;
            if (href && !/^(https?:|data:)/.test(href)) {
              try {
                const baseDir = path.split('/').slice(0, -1).join('/');
                src = RAW(resolvePath(baseDir, href));
              } catch (e) { /* leave src as-is */ }
            }
            const t = title ? ` title="${escapeHtml(title)}"` : '';
            return `<img src="${escapeHtml(src)}" alt="${escapeHtml(text)}"${t} loading="lazy">`;
          }
        }
      });
      container.innerHTML = marked.parse(text);
    } catch (e) {
      renderError(container, 'Failed to render ' + path + ': ' + e.message);
    }
  }

  function resolvePath(baseDir, href) {
    if (href.startsWith('/')) return href.slice(1);
    const segs = (baseDir ? baseDir.split('/') : []).concat(href.split('/'));
    const out = [];
    for (const s of segs) {
      if (s === '..') out.pop();
      else if (s !== '.' && s !== '') out.push(s);
    }
    return out.join('/');
  }

  // ----------- HTML VIEWER -----------
  async function fetchHtmlAndInject(path, iframe) {
    try {
      const text = await fetchRaw(path);
      // Use srcdoc so text/plain content-type doesn't matter
      iframe.srcdoc = text;
      return true;
    } catch (e) {
      err('html fetch failed', path, e);
      return false;
    }
  }

  // ----------- BOOTSTRAP -----------
  function ready(fn) {
    if (document.readyState !== 'loading') fn();
    else document.addEventListener('DOMContentLoaded', fn);
  }

  // Auto-inject topbar/footer on every page that opts in via meta or body class
  ready(() => {
    if (document.body.classList.contains('ds-page')) {
      const breadcrumb = document.body.dataset.breadcrumb;
      injectTopbar({ breadcrumb });
      injectFooter();
    }
  });

  // ----------- PUBLIC API -----------
  global.POF = {
    REPO, BRANCH,
    RAW, BLOB, TREE_VIEW,
    loadTree, listDir, findExact, listRecursive, countIn,
    injectTopbar, injectFooter,
    escapeHtml, renderEmpty, renderError, renderLoading,
    fetchRaw, renderMarkdownInto, fetchHtmlAndInject,
    resolvePath,
    log, err
  };

})(window);
