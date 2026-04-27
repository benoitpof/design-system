#!/usr/bin/env python3
"""Build POF Design System gallery for GitHub Pages.

- Copies site/* templates to _site root
- Copies examples/ and assets/ wholesale (so links work)
- Renders all md files (rules, layouts, memory, root docs) to styled HTML
- Generates icons.html (594 SVG gallery)
- Generates architecture.html (full git tree)
- Generates workflows.html (4 skills) + workflows/<name>.html each
- Generates databases.html + databases/<name>.html
- No 404 anywhere.
"""
import os, shutil, subprocess, html, json, re, pathlib
from datetime import datetime

ROOT = pathlib.Path(__file__).parent.parent
BUILD = ROOT / '_site'
SITE = ROOT / 'site'

GH_RAW = 'https://raw.githubusercontent.com/benoitpof/design-system/main'
GH_BLOB = 'https://github.com/benoitpof/design-system/blob/main'
GH_TREE = 'https://github.com/benoitpof/design-system/tree/main'

# ---------- 0. Clean and prepare ----------
if BUILD.exists():
    shutil.rmtree(BUILD)
BUILD.mkdir()

# ---------- 1. Copy site/ to root ----------
for f in SITE.iterdir():
    dst = BUILD / f.name
    if f.is_file():
        shutil.copy(f, dst)
    elif f.is_dir():
        shutil.copytree(f, dst)
print(f'[1] Copied site/ -> _site/')

# ---------- 1c. Fix charts.html static template links if examples/ is missing ----------
def fix_charts_static_links():
    """If examples/ folder doesn't exist (post-cleanup), patch site/charts.html and maps.html
    so links to ../examples/* go to GitHub instead of broken local paths."""
    if (ROOT / 'docs/Exemple').exists():
        return
    for filename in ['charts.html', 'maps.html']:
        f = BUILD / filename
        if not f.exists():
            continue
        text = f.read_text()
        # Replace href="../examples/X.html" or "examples/X.html" with GitHub URL
        import re
        text = re.sub(r'href="(?:\.\./)?examples/charts/([^"]+)"',
                      r'href="https://github.com/benoitpof/design-system/blob/main/examples/charts/\1" target="_blank"',
                      text)
        text = re.sub(r'href="(?:\.\./)?assets/maps/([^"]+\.html)"',
                      r'href="https://github.com/benoitpof/design-system/blob/main/assets/maps/\1" target="_blank"',
                      text)
        f.write_text(text)
    print('[1c] Patched charts.html/maps.html links since examples/ is missing')

fix_charts_static_links()


# ---------- 2. Copy examples/ and assets/ ----------
if (ROOT / 'docs/Exemple').exists():
    shutil.copytree(ROOT / 'docs/Exemple', BUILD / 'examples')
shutil.copytree(ROOT / 'assets', BUILD / 'assets')
print(f'[2] Copied examples/ + assets/ -> _site/')


# ---------- 2b. Rewrap chart pages with DS topbar ----------
def rewrap_chart_pages():
    """Wrap each examples/charts/*.html with a DS topbar at the top of body.
    The chart content stays as-is (preserves the SVG previews and chart-specific styles).
    """
    charts_dir = BUILD / 'examples' / 'charts'
    if not charts_dir.exists():
        return 0
    
    DS_TOPBAR = """
<style>
.ds-topbar{{position:sticky;top:0;z-index:100;background:#fff;border-bottom:1px solid #EAEBED;padding:12px 32px;display:flex;align-items:center;gap:14px;font-family:'Poppins',sans-serif}}
.ds-topbar img{{height:24px}}
.ds-topbar .crumbs{{font-size:10px;font-weight:600;color:#6C757D;letter-spacing:1px;text-transform:uppercase}}
.ds-topbar .version{{font-size:9px;font-weight:600;letter-spacing:1.5px;text-transform:uppercase;color:#2BA595;background:rgba(128,199,194,.12);padding:3px 8px;border-radius:3px}}
.ds-topbar .nav{{margin-left:auto;display:flex;gap:6px;flex-wrap:wrap}}
.ds-topbar .nav a{{font-size:9px;font-weight:600;color:#1C1F3B;text-decoration:none;padding:7px 12px;border:1px solid #EAEBED;border-radius:4px;text-transform:uppercase;letter-spacing:.5px}}
.ds-topbar .nav a:hover{{border-color:#80C7C2;background:rgba(128,199,194,.07)}}
</style>
<div class="ds-topbar">
  <a href="/design-system/index.html"><img src="/design-system/assets/logos/pof-logo-teal-white.svg" alt="POF"></a>
  <span class="crumbs">{breadcrumb}</span>
  <span class="version">v3.4.0</span>
  <nav class="nav">
    <a href="/design-system/index.html">Overview</a>
    <a href="/design-system/charts.html">All charts</a>
    <a href="/design-system/maps.html">Maps</a>
    <a href="/design-system/icons.html">Icons</a>
    <a href="/design-system/architecture.html">Architecture</a>
    <a href="/design-system/workflows.html">Workflows</a>
  </nav>
</div>
"""
    
    count = 0
    for html_file in charts_dir.glob('*.html'):
        if html_file.name.startswith('_'):
            continue
        text = html_file.read_text()
        # Determine breadcrumb from filename
        stem = html_file.stem
        breadcrumb = f'Chart Bank / {stem}'
        topbar = DS_TOPBAR.format(breadcrumb=breadcrumb)
        # Inject after <body> tag
        if '<body>' in text and 'ds-topbar' not in text:
            text = text.replace('<body>', '<body>\n' + topbar, 1)
            html_file.write_text(text)
            count += 1
    return count

charts_rewrapped = rewrap_chart_pages()
print(f'[2b] Rewrapped {charts_rewrapped} chart pages with DS topbar')

# ---------- 3. Markdown -> HTML rendering ----------
import markdown
md = markdown.Markdown(extensions=['fenced_code', 'tables', 'codehilite', 'sane_lists', 'toc'])

# Shared HTML template for rendered md pages
MD_PAGE = '''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · POF Design System</title>
<link rel="stylesheet" href="{css_path}">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&family=Raleway:ital,wght@0,300;0,400;0,600;0,700&family=Roboto+Mono:wght@400;600&display=swap" rel="stylesheet">
<style>
:root {{
  --navy:#1C1F3B; --steel:#435D74; --steel-light:#5F7D95; --steel-pale:#CFD9E0;
  --teal:#80C7C2; --teal-dark:#2BA595; --coral:#E8546C;
  --gris-pof:#F9FCFF; --neutral-light:#F0F0F0; --neutral-mid:#EAEBED;
  --gray-400:#CED4DA; --gray-600:#6C757D; --body:#3C3C3C; --white:#FFFFFF;
}}
*{{box-sizing:border-box}}html,body{{margin:0;padding:0}}
body{{font-family:'Raleway',sans-serif;color:var(--body);background:#fff;-webkit-font-smoothing:antialiased;line-height:1.6}}
.topbar{{position:sticky;top:0;z-index:50;background:#fff;border-bottom:1px solid var(--neutral-mid);padding:14px 32px;display:flex;align-items:center;gap:16px}}
.topbar .brand img{{height:26px}}.topbar .crumbs{{font-family:Poppins;font-size:11px;font-weight:600;color:var(--gray-600);letter-spacing:1px;text-transform:uppercase}}
.topbar .version{{font-family:Poppins;font-size:9px;font-weight:600;letter-spacing:1.5px;text-transform:uppercase;color:var(--teal-dark);background:rgba(128,199,194,.12);padding:3px 8px;border-radius:3px}}
.topbar-nav{{margin-left:auto;display:flex;gap:8px;flex-wrap:wrap}}
.topbar-nav a{{font-family:Poppins;font-size:10px;font-weight:600;letter-spacing:.5px;color:var(--navy);text-decoration:none;padding:8px 14px;border:1px solid var(--neutral-mid);border-radius:5px;text-transform:uppercase}}
.topbar-nav a:hover,.topbar-nav a.active{{border-color:var(--teal);background:rgba(128,199,194,.07)}}
.page-header{{padding:48px 32px 24px;max-width:1080px;margin:0 auto;border-bottom:1px solid var(--neutral-mid)}}
.page-header .eyebrow{{font-family:Poppins;font-weight:700;font-size:11px;letter-spacing:2px;color:var(--steel-light);text-transform:uppercase}}
.page-header h1{{font-family:Poppins;font-weight:700;font-size:36px;color:var(--navy);margin:8px 0 12px;letter-spacing:-.5px}}
.page-header .meta{{font-family:Raleway;font-size:13px;color:var(--gray-600)}}
.page-header .actions{{margin-top:16px;display:flex;gap:12px;flex-wrap:wrap}}
.page-header .btn{{font-family:Poppins;font-size:10px;font-weight:600;letter-spacing:.5px;color:var(--navy);text-decoration:none;padding:8px 14px;border:1px solid var(--neutral-mid);border-radius:5px;text-transform:uppercase;background:#fff;transition:border-color .15s}}
.page-header .btn:hover{{border-color:var(--teal);background:rgba(128,199,194,.07)}}
.page-header .btn.primary{{background:var(--navy);color:#fff;border-color:var(--navy)}}
.page-header .btn.primary:hover{{background:var(--teal-dark);border-color:var(--teal-dark)}}
article.md-content{{max-width:880px;margin:0 auto;padding:48px 32px 96px;font-family:Raleway,sans-serif;font-size:16px;color:var(--body);line-height:1.7}}
article.md-content h1{{font-family:Poppins;font-weight:700;font-size:32px;color:var(--navy);margin:48px 0 16px;letter-spacing:-.5px;line-height:1.2}}
article.md-content h1:first-child{{margin-top:0}}
article.md-content h2{{font-family:Poppins;font-weight:700;font-size:22px;color:var(--navy);margin:40px 0 14px;padding-top:8px}}
article.md-content h3{{font-family:Poppins;font-weight:600;font-size:17px;color:var(--steel);margin:28px 0 10px;text-transform:uppercase;letter-spacing:.5px}}
article.md-content h4{{font-family:Poppins;font-weight:600;font-size:14px;color:var(--steel-light);margin:20px 0 8px}}
article.md-content p{{margin:0 0 16px}}
article.md-content a{{color:var(--teal-dark);text-decoration:underline;text-decoration-color:rgba(43,165,149,.3)}}
article.md-content a:hover{{text-decoration-color:var(--teal-dark)}}
article.md-content code{{font-family:'Roboto Mono',monospace;font-size:13px;background:var(--gris-pof);padding:2px 6px;border-radius:3px;color:var(--navy);border:1px solid var(--neutral-mid)}}
article.md-content pre{{background:var(--navy);color:#80C7C2;padding:18px 22px;border-radius:6px;overflow-x:auto;margin:20px 0;font-family:'Roboto Mono',monospace;font-size:13px;line-height:1.5}}
article.md-content pre code{{background:transparent;border:none;color:inherit;padding:0;font-size:inherit}}
article.md-content blockquote{{margin:20px 0;padding:14px 22px;border-left:3px solid var(--teal);background:rgba(128,199,194,.08);font-style:italic;color:var(--steel)}}
article.md-content table{{border-collapse:collapse;width:100%;margin:20px 0;font-family:Raleway;font-size:14px}}
article.md-content table th{{background:var(--navy);color:#fff;font-family:Poppins;font-weight:600;padding:12px 14px;text-align:left}}
article.md-content table td{{padding:10px 14px;border-bottom:1px solid var(--neutral-mid);vertical-align:top}}
article.md-content table tr:nth-child(even) td{{background:var(--gris-pof)}}
article.md-content ul,article.md-content ol{{margin:0 0 16px 22px;padding:0}}
article.md-content li{{margin:6px 0}}
article.md-content hr{{border:none;border-top:1px solid var(--neutral-mid);margin:32px 0}}
article.md-content img{{max-width:100%;height:auto;border-radius:4px}}
.codehilite{{background:var(--navy);border-radius:6px;margin:20px 0;overflow-x:auto}}
.codehilite pre{{margin:0}}
footer{{padding:40px 32px;text-align:center;color:var(--gray-600);font-family:Raleway;font-size:12px;border-top:1px solid var(--neutral-mid)}}
footer a{{color:var(--teal-dark);text-decoration:none}}
</style>
</head>
<body>
<div class="topbar">
  <a class="brand" href="{root_path}index.html"><img src="{assets_path}logos/pof-logo-teal-white.svg" alt="POF"></a>
  <span class="crumbs">{breadcrumb}</span>
  <span class="version">v3.4.0</span>
  <nav class="topbar-nav">
    <a href="{root_path}index.html">Overview</a>
    <a href="{root_path}architecture.html">Architecture</a>
    <a href="{root_path}charts.html">Charts</a>
    <a href="{root_path}maps.html">Maps</a>
    <a href="{root_path}icons.html">Icons</a>
    <a href="{root_path}workflows.html">Workflows</a>
    <a href="{root_path}databases.html">DBs</a>
    <a href="https://github.com/benoitpof/design-system">GitHub</a>
  </nav>
</div>
<header class="page-header">
  <div class="eyebrow">{breadcrumb}</div>
  <h1>{title}</h1>
  <div class="meta">{meta}</div>
  <div class="actions">
    <a class="btn primary" href="{github_url}">View on GitHub</a>
    <a class="btn" href="{root_path}index.html">Back to overview</a>
  </div>
</header>
<article class="md-content">
{content}
</article>
<footer>
  POF Design System v3.4.0 · Auto-rendered from {md_relative} · <a href="https://github.com/benoitpof/design-system">GitHub</a>
</footer>
</body>
</html>
'''

def render_md(md_path, out_path, title=None, breadcrumb=None, css_path='styles.css', root_path='', assets_path=''):
    text = md_path.read_text()
    # Strip first H1 if present (becomes title)
    first_h1 = re.match(r'^# (.+?)$', text, re.MULTILINE)
    if first_h1 and not title:
        title = first_h1.group(1).split('—')[0].strip().replace('`', '')
    if not title:
        title = md_path.stem
    if not breadcrumb:
        breadcrumb = md_path.stem
    # Render to HTML
    html_body = md.convert(text)
    md.reset()
    rel = md_path.relative_to(ROOT).as_posix()
    page = MD_PAGE.format(
        title=html.escape(title),
        breadcrumb=html.escape(breadcrumb),
        meta=f'Source : <code>{rel}</code> · POF DS v3.4.0',
        github_url=f'{GH_BLOB}/{rel}',
        content=html_body,
        css_path=css_path,
        root_path=root_path,
        assets_path=assets_path,
        md_relative=rel,
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(page)

# Render docs/rules/*.md
for f in sorted((ROOT / 'docs/Rules').glob('*.md')):
    render_md(f, BUILD / 'rules' / f"{f.stem}.html",
              breadcrumb=f"Rules / {f.stem}",
              css_path='../styles.css',
              root_path='../',
              assets_path='../assets/')
print(f'[3a] Rendered docs/rules/*.md -> _site/rules/*.html')

# Render docs/layouts/*.md
for f in sorted((ROOT / 'docs/Layout').glob('*.md')):
    render_md(f, BUILD / 'layouts' / f"{f.stem}.html",
              breadcrumb=f"Layouts / {f.stem}",
              css_path='../styles.css',
              root_path='../',
              assets_path='../assets/')
print(f'[3b] Rendered docs/layouts/*.md -> _site/layouts/*.html')

# Render memory/*.md (optional)
mem_dir = ROOT / 'docs/Memory'
if mem_dir.exists():
    for f in sorted(mem_dir.glob('*.md')):
        render_md(f, BUILD / 'memory' / f"{f.stem}.html",
                  breadcrumb=f"Memory / {f.stem}",
                  css_path='../styles.css',
                  root_path='../',
                  assets_path='../assets/')
    print(f'[3c] Rendered memory/*.md -> _site/memory/*.html')
else:
    print('[3c] memory/ folder absent, skip')

# Render root *.md (README, ITERATE, VISUALIZE, CHANGELOG)
for fname in ['README.md', 'ITERATE.md', 'VISUALIZE.md', 'CHANGELOG.md']:
    f = ROOT / fname
    if f.exists():
        render_md(f, BUILD / f'{f.stem.lower()}.html',
                  breadcrumb=f.stem, css_path='styles.css', root_path='', assets_path='assets/')
print(f'[3d] Rendered root md files')

# ---------- 4. Icons gallery (594 SVG) ----------
def build_icons_gallery():
    icons_dir = ROOT / 'assets/icons'
    cats = []
    # Root-level SVG (the active set) — filter out _archived
    root_svgs = sorted([f for f in icons_dir.glob('*.svg')])
    if root_svgs:
        cats.append(('environment · active', root_svgs))
    # Subdirectories — SKIP _archived
    for cat_dir in sorted([d for d in icons_dir.iterdir() if d.is_dir() and not d.name.startswith('_')]):
        svgs = sorted(cat_dir.glob('*.svg'))
        if svgs:
            cats.append((cat_dir.name, svgs))
        for sub in cat_dir.iterdir():
            if sub.is_dir() and not sub.name.startswith('_'):
                ssvgs = sorted(sub.glob('*.svg'))
                if ssvgs:
                    cats.append((f'{cat_dir.name}/{sub.name}', ssvgs))

    cards_html = []
    total = 0
    for cat_name, svgs in cats:
        cards_html.append(f'<h2>{cat_name} <span class="count">{len(svgs)}</span></h2><div class="icon-grid">')
        for svg in svgs:
            rel = svg.relative_to(ROOT).as_posix()
            name = svg.stem
            cards_html.append(f'''
<a class="icon-card" href="{rel}" title="{name}">
  <div class="icon-thumb"><img src="{rel}" alt="{name}" loading="lazy"></div>
  <div class="icon-name">{name}</div>
</a>''')
            total += 1
        cards_html.append('</div>')

    page = f'''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>POF · Icons · v3.4.0</title>
<link rel="stylesheet" href="styles.css">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&family=Raleway:wght@400;600&display=swap" rel="stylesheet">
<style>
.topbar{{position:sticky;top:0;z-index:50;background:#fff;border-bottom:1px solid var(--neutral-mid);padding:14px 32px;display:flex;align-items:center;gap:16px}}
.topbar .brand img{{height:26px}}.topbar .crumbs{{font-family:Poppins;font-size:11px;font-weight:600;color:var(--gray-600);letter-spacing:1px;text-transform:uppercase}}
.topbar .version{{font-family:Poppins;font-size:9px;font-weight:600;letter-spacing:1.5px;text-transform:uppercase;color:var(--teal-dark);background:rgba(128,199,194,.12);padding:3px 8px;border-radius:3px}}
.topbar-nav{{margin-left:auto;display:flex;gap:8px;flex-wrap:wrap}}
.topbar-nav a{{font-family:Poppins;font-size:10px;font-weight:600;letter-spacing:.5px;color:var(--navy);text-decoration:none;padding:8px 14px;border:1px solid var(--neutral-mid);border-radius:5px;text-transform:uppercase}}
.topbar-nav a:hover,.topbar-nav a.active{{border-color:var(--teal);background:rgba(128,199,194,.07)}}
.hero{{padding:48px 32px 32px;max-width:1280px;margin:0 auto}}
.hero h1{{font-family:Poppins;font-weight:700;font-size:36px;color:var(--navy);margin:0 0 8px}}
.hero p{{font-family:Raleway;font-size:14px;color:var(--gray-600);max-width:760px}}
.intro-stats{{display:grid;grid-template-columns:repeat(4,1fr);gap:0;margin:32px auto 0;max-width:1280px;padding:0 32px;border-top:1px solid var(--neutral-mid);border-bottom:1px solid var(--neutral-mid)}}
.intro-stat{{padding:20px 0}}.intro-stat:not(:last-child){{border-right:1px solid var(--neutral-mid);padding-right:20px}}.intro-stat:not(:first-child){{padding-left:20px}}
.intro-stat .num{{font-family:Poppins;font-weight:700;font-size:28px;color:var(--navy);line-height:1}}
.intro-stat .lab{{font-family:Raleway;font-size:10px;color:var(--gray-600);margin-top:6px;letter-spacing:.5px;text-transform:uppercase}}
.gallery{{max-width:1280px;margin:48px auto 0;padding:0 32px 96px}}
.gallery h2{{font-family:Poppins;font-weight:600;font-size:14px;letter-spacing:1.5px;color:var(--steel);text-transform:uppercase;margin:32px 0 16px;padding-left:14px;border-left:3px solid var(--steel-light)}}
.gallery h2 .count{{font-size:11px;color:var(--gray-600);margin-left:8px;font-weight:400}}
.icon-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(110px,1fr));gap:8px;margin-bottom:32px}}
.icon-card{{display:block;text-decoration:none;color:inherit;background:#fff;border:1px solid var(--neutral-mid);border-radius:6px;padding:14px 8px;text-align:center;transition:border-color 150ms,transform 150ms}}
.icon-card:hover{{border-color:var(--teal);transform:translateY(-1px);box-shadow:0 4px 12px rgba(28,31,59,.08)}}
.icon-thumb{{width:100%;aspect-ratio:1;display:flex;align-items:center;justify-content:center;padding:8px;background:var(--gris-pof);border-radius:4px;margin-bottom:6px}}
.icon-thumb img{{max-width:100%;max-height:100%;width:32px;height:32px}}
.icon-name{{font-family:Poppins;font-size:9px;color:var(--steel);font-weight:600;letter-spacing:.3px;word-break:break-word;line-height:1.2}}
.search{{margin:24px 0;display:flex;gap:8px;align-items:center}}
.search input{{flex:1;padding:10px 14px;border:1px solid var(--neutral-mid);border-radius:5px;font-family:Raleway;font-size:14px}}
.search input:focus{{outline:none;border-color:var(--teal)}}
</style>
</head>
<body>
<div class="topbar">
  <a class="brand" href="index.html"><img src="assets/logos/pof-logo-teal-white.svg" alt="POF"></a>
  <span class="crumbs">Design System · Icons</span>
  <span class="version">v3.4.0</span>
  <nav class="topbar-nav">
    <a href="index.html">Overview</a>
    <a href="architecture.html">Architecture</a>
    <a href="charts.html">Charts</a>
    <a href="maps.html">Maps</a>
    <a href="icons.html" class="active">Icons</a>
    <a href="images.html">Images</a>
    <a href="workflows.html">Workflows</a>
    <a href="databases.html">DBs</a>
    <a href="https://github.com/benoitpof/design-system">GitHub</a>
  </nav>
</div>
<header class="hero">
  <h1>Icons · {total} SVG</h1>
  <p>Tabler CDN reste source primaire. Voir <a href="rules/ICONS.html">rules/ICONS.md</a> pour le système complet et les patterns d'embed (HTML/PPTX/DOCX). Les icons archivées sont conservées pour référence et peuvent être réactivées si besoin.</p>
</header>
<section class="intro-stats">
  <div class="intro-stat"><div class="num">__TOTAL__</div><div class="lab">total SVG</div></div>
  <div class="intro-stat"><div class="num">__CAT_ACTIVE__</div><div class="lab">active categories</div></div>
  <div class="intro-stat"><div class="num">Tabler</div><div class="lab">primary source</div></div>
  <div class="intro-stat"><div class="num">currentColor</div><div class="lab">stroke pattern</div></div>
</section>
<div class="gallery">
<div class="search"><input type="text" id="q" placeholder="Filtrer par nom (ex: leaf, recycle, factory)..." oninput="filterIcons()"></div>
__CARDS__
</div>
<script>
function filterIcons(){{
  const q=document.getElementById('q').value.toLowerCase();
  document.querySelectorAll('.icon-card').forEach(c=>{{
    const n=c.querySelector('.icon-name').textContent.toLowerCase();
    c.style.display=n.includes(q)?'':'none';
  }});
}}
</script>
</body>
</html>'''
    cat_active = len([c for c in cats if not c[0].startswith('_archived')])
    cat_active_count = len([c for c in cats if not c[0].startswith('_archived')])
    page2 = page.replace('__TOTAL__', str(total)).replace('__CAT_ACTIVE__', str(cat_active_count)).replace('__CARDS__', '\n'.join(cards_html))
    (BUILD / 'icons.html').write_text(page2)
    return total

icons_total = build_icons_gallery()
print(f'[4] Built icons.html ({icons_total} SVG)')


# ---------- 4b. Images gallery ----------
def build_images_gallery():
    sections = []
    for sub, label, grid_cls in [
        ('logos', 'Logos · `/assets/logos/`', 'logo-grid'),
        ('monogramme', 'Monogramme · `/assets/monogramme/`', 'pictos-grid'),
        ('brand-elements', 'Brand elements · `/assets/brand-elements/`', 'pictos-grid'),
        ('backgrounds', 'Backgrounds · `/assets/backgrounds/`', 'bg-grid'),
    ]:
        d = ROOT / 'assets' / sub
        if not d.exists():
            continue
        files = sorted(d.glob('*.svg'))
        if not files:
            continue
        cards = []
        for f in files:
            rel = f.relative_to(ROOT).as_posix()
            cards.append(f'<a class="img-card" href="{rel}" title="{f.stem}"><div class="img-thumb {grid_cls.replace("-grid", "-thumb")}"><img src="{rel}" alt="{f.stem}"></div><div class="img-name">{f.stem}</div></a>')
        sections.append((label, cards, grid_cls, len(files)))

    sections_html = ''
    total = 0
    for title, cards, grid_cls, n in sections:
        sections_html += f'<h2>{title} <span style="color:var(--gray-600);font-weight:400;font-size:11px">{n} files</span></h2><div class="img-grid {grid_cls}">{"".join(cards)}</div>'
        total += n

    page = """<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>POF · Images · v3.4.0</title>
<link rel="stylesheet" href="styles.css">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&family=Raleway:wght@400;600&display=swap" rel="stylesheet">
<style>
.topbar{position:sticky;top:0;z-index:50;background:#fff;border-bottom:1px solid var(--neutral-mid);padding:14px 32px;display:flex;align-items:center;gap:16px}
.topbar .brand img{height:26px}.topbar .crumbs{font-family:Poppins;font-size:11px;font-weight:600;color:var(--gray-600);letter-spacing:1px;text-transform:uppercase}
.topbar .version{font-family:Poppins;font-size:9px;font-weight:600;letter-spacing:1.5px;text-transform:uppercase;color:var(--teal-dark);background:rgba(128,199,194,.12);padding:3px 8px;border-radius:3px}
.topbar-nav{margin-left:auto;display:flex;gap:8px;flex-wrap:wrap}
.topbar-nav a{font-family:Poppins;font-size:10px;font-weight:600;color:var(--navy);text-decoration:none;padding:8px 14px;border:1px solid var(--neutral-mid);border-radius:5px;text-transform:uppercase}
.topbar-nav a:hover,.topbar-nav a.active{border-color:var(--teal);background:rgba(128,199,194,.07)}
.hero{padding:48px 32px 24px;max-width:1280px;margin:0 auto}
.hero h1{font-family:Poppins;font-weight:700;font-size:36px;color:var(--navy);margin:0 0 8px}
.hero p{font-family:Raleway;font-size:14px;color:var(--gray-600);max-width:760px}
.key-resources{position:sticky;top:54px;z-index:40;padding:14px 32px;background:var(--gris-pof);border-bottom:1px solid var(--neutral-mid)}
.key-resources .inner{max-width:1280px;margin:0 auto;display:flex;align-items:center;gap:16px;flex-wrap:wrap}
.key-resources .label{font-family:Poppins;font-size:10px;font-weight:600;letter-spacing:1.5px;color:var(--steel);text-transform:uppercase}
.key-resources .links{display:flex;gap:8px;flex-wrap:wrap}
.key-resources a{font-family:Poppins;font-size:11px;font-weight:600;color:var(--navy);text-decoration:none;padding:6px 12px;background:#fff;border:1px solid var(--neutral-mid);border-radius:5px}
.key-resources a:hover{border-color:var(--teal);background:rgba(128,199,194,.07)}
.gallery{max-width:1280px;margin:32px auto;padding:0 32px 96px}
.gallery h2{font-family:Poppins;font-weight:600;font-size:14px;letter-spacing:1px;color:var(--steel);text-transform:uppercase;margin:32px 0 16px;padding-left:14px;border-left:3px solid var(--steel-light)}
.img-grid{display:grid;gap:14px;margin-bottom:32px}
.logo-grid{grid-template-columns:repeat(auto-fill,minmax(220px,1fr))}
.pictos-grid{grid-template-columns:repeat(auto-fill,minmax(150px,1fr))}
.bg-grid{grid-template-columns:repeat(auto-fill,minmax(320px,1fr))}
.img-card{display:block;text-decoration:none;color:inherit;background:#fff;border:1px solid var(--neutral-mid);border-radius:6px;padding:14px;transition:border-color 150ms,transform 150ms}
.img-card:hover{border-color:var(--teal);transform:translateY(-1px);box-shadow:0 4px 12px rgba(28,31,59,.08)}
.img-thumb{aspect-ratio:16/9;display:flex;align-items:center;justify-content:center;padding:12px;background:var(--gris-pof);border-radius:4px;margin-bottom:10px}
.img-thumb img{max-width:100%;max-height:100%}
.logo-thumb{aspect-ratio:5/2;background:#1C1F3B}
.logo-thumb img{max-height:50px}
.bg-thumb{aspect-ratio:32/9;padding:0;overflow:hidden}
.bg-thumb img{width:100%;height:100%;object-fit:cover}
.img-name{font-family:Poppins;font-size:11px;color:var(--steel);font-weight:600;word-break:break-word}
</style>
</head>
<body>
<div class="topbar">
<a class="brand" href="index.html"><img src="assets/logos/pof-logo-teal-white.svg" alt="POF"></a>
<span class="crumbs">Design System · Images</span>
<span class="version">v3.4.0</span>
<nav class="topbar-nav">
<a href="index.html">Overview</a>
<a href="architecture.html">Architecture</a>
<a href="charts.html">Charts</a>
<a href="maps.html">Maps</a>
<a href="icons.html">Icons</a>
<a href="images.html" class="active">Images</a>
<a href="workflows.html">Workflows</a>
<a href="databases.html">DBs</a>
<a href="https://github.com/benoitpof/design-system">GitHub</a>
</nav>
</div>
<header class="hero">
<h1>Images · brand visual assets</h1>
<p>Logos, monogramme, brand elements (waves, corner brackets), backgrounds. Photographies sourcees dans la <a href="databases/media-assets.html">Notion Media Assets DB</a>.</p>
</header>
<section class="key-resources">
<div class="inner">
<div class="label">Cadrage et regles</div>
<div class="links">
<a href="rules/PHOTOS.html">PHOTOS rules</a>
<a href="rules/DESIGN.html">DESIGN — overlay</a>
<a href="rules/ASSETS.html">ASSETS index</a>
<a href="https://github.com/benoitpof/design-system/tree/main/assets" target="_blank">→ /assets/ on GitHub</a>
</div>
</div>
</section>
<div class="gallery">
""" + sections_html + """
</div>
</body></html>"""
    (BUILD / 'images.html').write_text(page)
    return total

images_total = build_images_gallery()
print(f'[4b] Built images.html ({images_total} items)')

# ---------- 4d. Key resources sticky bar ----------
def inject_key_resources():
    """Add key-resources sticky bar to charts/maps/icons pages."""
    KEY_RES = {
        'charts.html': [
            ('rules/CHARTS.html', '📐 CHARTS rules'),
            ('rules/TABLES.html', '📐 TABLES rules'),
            ('https://github.com/benoitpof/design-system/tree/main/examples/charts', '🎯 Examples sur GitHub'),
        ],
        'maps.html': [
            ('rules/MAPS.html', '📐 MAPS rules'),
            ('assets/maps/map-charter.html', '🎯 Map Charter interactif'),
            ('assets/maps/pof-world-map-blank.svg', '🌍 World map base SVG'),
            ('https://github.com/benoitpof/design-system/tree/main/assets/maps', '→ /assets/maps/ on GitHub'),
        ],
        'icons.html': [
            ('rules/ICONS.html', '📐 ICONS rules'),
            ('https://tabler.io/icons', '🎯 Tabler CDN (source primaire)'),
            ('https://github.com/benoitpof/design-system/tree/main/assets/icons', '→ /assets/icons/ on GitHub'),
        ],
    }
    KEY_CSS = """<style>.kr-bar{position:sticky;top:54px;z-index:40;padding:12px 32px;background:#F9FCFF;border-bottom:1px solid #EAEBED}.kr-bar .kr-inner{max-width:1280px;margin:0 auto;display:flex;align-items:center;gap:14px;flex-wrap:wrap}.kr-bar .kr-label{font-family:Poppins;font-size:10px;font-weight:600;letter-spacing:1.5px;color:#435D74;text-transform:uppercase}.kr-bar a{font-family:Poppins;font-size:11px;font-weight:600;color:#1C1F3B;text-decoration:none;padding:6px 12px;background:#fff;border:1px solid #EAEBED;border-radius:5px}.kr-bar a:hover{border-color:#80C7C2;background:rgba(128,199,194,.07)}</style>"""

    for filename, links in KEY_RES.items():
        f = BUILD / filename
        if not f.exists():
            continue
        text = f.read_text()
        if 'class="kr-bar"' in text:
            continue
        target_attr = lambda h: ' target="_blank"' if h.startswith('http') else ''
        links_html = ''.join(f'<a href="{h}"{target_attr(h)}>{lbl}</a>' for h, lbl in links)
        bar = KEY_CSS + f'<section class="kr-bar"><div class="kr-inner"><div class="kr-label">Cadrage et examples</div>{links_html}</div></section>'
        # Insert right after closing of topbar div (before <header class="hero">)
        if '<header class="hero">' in text:
            text = text.replace('<header class="hero">', bar + '\n<header class="hero">', 1)
            f.write_text(text)

inject_key_resources()
print('[4d] Key resources sticky bar injected on charts/maps/icons')


# ---------- 5. Architecture page : full Git tree ----------
def build_architecture():
    # Walk the repo and list everything
    tree_lines = []
    skip_dirs = {'.git', '_site', '.archive', '__pycache__', 'node_modules'}
    def walk(p, prefix='', is_last=True):
        entries = sorted([e for e in p.iterdir() if e.name not in skip_dirs and not e.name.startswith('.')], 
                        key=lambda x: (x.is_file(), x.name))
        # Truncate at 5 entries per dir if all entries are files of same type
        if len(entries) > 5 and all(e.is_file() for e in entries):
            same_ext = len({e.suffix for e in entries}) == 1
            if same_ext:
                truncated = entries[:5]
                hidden = len(entries) - 5
                for i, e in enumerate(truncated):
                    last = i == len(truncated) - 1 and hidden == 0
                    connector = '└── ' if last else '├── '
                    display = e.name
                    size = ''
                    try:
                        s = e.stat().st_size
                        if s < 1024: size = f' ({s} B)'
                        elif s < 1024*1024: size = f' ({s//1024} KB)'
                        else: size = f' ({s//(1024*1024)} MB)'
                    except: pass
                    rel = e.relative_to(ROOT).as_posix()
                    link = f' <a href="{GH_BLOB}/{rel}" target="_blank">→ GitHub</a>'
                    tree_lines.append(f'<div class="tline">{prefix}{connector}<span class="f">{display}</span><span class="meta">{size}{link}</span></div>')
                # Show "..."
                rel_dir = p.relative_to(ROOT).as_posix()
                tree_lines.append(f'<div class="tline">{prefix}└── <span class="more">... {hidden} autres .{entries[0].suffix.lstrip(".")} (<a href="{GH_TREE}/{rel_dir}" target="_blank">voir tout sur GitHub</a>)</span></div>')
                return
        for i, e in enumerate(entries):
            last = i == len(entries) - 1
            connector = '└── ' if last else '├── '
            display = e.name + ('/' if e.is_dir() else '')
            size = ''
            if e.is_file():
                try:
                    s = e.stat().st_size
                    if s < 1024: size = f' ({s} B)'
                    elif s < 1024*1024: size = f' ({s//1024} KB)'
                    else: size = f' ({s//(1024*1024)} MB)'
                except: pass
            link = ''
            try:
                rel = e.relative_to(ROOT).as_posix()
                if e.is_file():
                    link = f' <a href="{GH_BLOB}/{rel}" target="_blank">→ GitHub</a>'
                else:
                    link = f' <a href="{GH_TREE}/{rel}" target="_blank">→ GitHub</a>'
            except: pass
            tree_lines.append(f'<div class="tline">{prefix}{connector}<span class="{"d" if e.is_dir() else "f"}">{display}</span><span class="meta">{size}{link}</span></div>')
            if e.is_dir():
                ext = '    ' if last else '│   '
                walk(e, prefix + ext, last)
    tree_lines.append(f'<div class="tline"><span class="d">benoitpof/design-system/</span> <a href="{GH_TREE}" target="_blank">→ GitHub root</a></div>')
    walk(ROOT)
    
    # Stats
    counts = {}
    for ext in ['svg','md','json','html','css','js','py','xlsx','pptx','docx','png']:
        c = len(list(ROOT.rglob(f'*.{ext}')))
        if c: counts[ext] = c
    stats_html = ''.join(f'<div class="intro-stat"><div class="num">{c}</div><div class="lab">.{e} files</div></div>' for e, c in list(counts.items())[:4])
    
    page = f'''<!DOCTYPE html>
<html lang="fr">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>POF · Architecture · v3.4.0</title>
<link rel="stylesheet" href="styles.css">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&family=Raleway:wght@400;600&family=Roboto+Mono:wght@400;600&display=swap" rel="stylesheet">
<style>
.topbar{{position:sticky;top:0;z-index:50;background:#fff;border-bottom:1px solid var(--neutral-mid);padding:14px 32px;display:flex;align-items:center;gap:16px}}
.topbar .brand img{{height:26px}}.topbar .crumbs{{font-family:Poppins;font-size:11px;font-weight:600;color:var(--gray-600);letter-spacing:1px;text-transform:uppercase}}
.topbar .version{{font-family:Poppins;font-size:9px;font-weight:600;letter-spacing:1.5px;text-transform:uppercase;color:var(--teal-dark);background:rgba(128,199,194,.12);padding:3px 8px;border-radius:3px}}
.topbar-nav{{margin-left:auto;display:flex;gap:8px;flex-wrap:wrap}}
.topbar-nav a{{font-family:Poppins;font-size:10px;font-weight:600;letter-spacing:.5px;color:var(--navy);text-decoration:none;padding:8px 14px;border:1px solid var(--neutral-mid);border-radius:5px;text-transform:uppercase}}
.topbar-nav a:hover,.topbar-nav a.active{{border-color:var(--teal);background:rgba(128,199,194,.07)}}
.hero{{padding:48px 32px 24px;max-width:1280px;margin:0 auto}}
.hero h1{{font-family:Poppins;font-weight:700;font-size:36px;color:var(--navy);margin:0 0 8px}}
.hero p{{font-family:Raleway;font-size:14px;color:var(--gray-600);max-width:760px}}
.intro-stats{{display:grid;grid-template-columns:repeat(4,1fr);gap:0;margin:24px auto 0;max-width:1280px;padding:0 32px;border-top:1px solid var(--neutral-mid);border-bottom:1px solid var(--neutral-mid)}}
.intro-stat{{padding:20px 0}}.intro-stat:not(:last-child){{border-right:1px solid var(--neutral-mid);padding-right:20px}}.intro-stat:not(:first-child){{padding-left:20px}}
.intro-stat .num{{font-family:Poppins;font-weight:700;font-size:28px;color:var(--navy)}}.intro-stat .lab{{font-family:Raleway;font-size:10px;color:var(--gray-600);margin-top:6px;letter-spacing:.5px;text-transform:uppercase}}
.tree{{max-width:1280px;margin:32px auto;padding:24px 32px 96px;font-family:'Roboto Mono',monospace;font-size:12px;line-height:1.7}}
.tree h2{{font-family:Poppins;font-weight:600;font-size:14px;letter-spacing:1.5px;color:var(--steel);text-transform:uppercase;margin:0 0 16px;padding-left:14px;border-left:3px solid var(--steel-light)}}
.tline{{white-space:pre;color:var(--steel);padding:1px 0}}
.tline .d{{color:var(--navy);font-weight:600}}
.tline .f{{color:var(--steel)}}
.tline .meta{{color:var(--gray-600);font-size:10px}}
.tline a{{color:var(--teal-dark);text-decoration:none;margin-left:6px;font-size:10px}}
.tline a:hover{{text-decoration:underline}}
.tline:hover{{background:var(--gris-pof)}}
</style>
</head>
<body>
<div class="topbar">
  <a class="brand" href="index.html"><img src="assets/logos/pof-logo-teal-white.svg" alt="POF"></a>
  <span class="crumbs">Design System · Architecture</span>
  <span class="version">v3.4.0</span>
  <nav class="topbar-nav">
    <a href="index.html">Overview</a>
    <a href="architecture.html" class="active">Architecture</a>
    <a href="charts.html">Charts</a>
    <a href="maps.html">Maps</a>
    <a href="icons.html">Icons</a>
    <a href="images.html">Images</a>
    <a href="workflows.html">Workflows</a>
    <a href="databases.html">DBs</a>
    <a href="https://github.com/benoitpof/design-system">GitHub</a>
  </nav>
</div>
<header class="hero">
  <h1>Architecture du repo</h1>
  <p>Arborescence complète du repo benoitpof/design-system. Chaque fichier et dossier est lié à GitHub. Ignore : .git, _site, .archive, fichiers cachés.</p>
</header>
<section class="intro-stats">{stats_html}</section>
<section class="tree">
<h2>Tree complet</h2>
{chr(10).join(tree_lines)}
</section>
</body>
</html>'''
    (BUILD / 'architecture.html').write_text(page)

build_architecture()
print(f'[5] Built architecture.html (full Git tree)')

# ---------- 6. Workflows page (replaces skills) + sub-pages ----------
WORKFLOW_DEFS = [
    {'slug': 'ds-dataviz-generator', 'num': 'S1', 'cat': 'ATOMIQUE', 'name': 'DS-Dataviz-generator',
     'notion': 'https://www.notion.so/34fc2ce245e881589325de3fc89e7154',
     'desc': 'Génère un asset visuel atomique : chart (16 templates), map (5 patterns), table. Mode quick (single-shot, QA auto) ou iterate (push Notion + boucle review Benoît).',
     'triggers': ['render chart', 'render map', 'build table', 'dataviz']},
    {'slug': 'ds-file-assembler', 'num': 'S2', 'cat': 'ORCHESTRATEUR', 'name': 'ds-file-assembler',
     'notion': 'https://www.notion.so/34fc2ce245e8811d9310cfe956ea089d',
     'desc': 'Assemble decks, reports A4, web pages, social posts depuis du contenu source. Lit les règles du repo, choisit les layouts, orchestre la création des assets via DS-Dataviz-generator.',
     'triggers': ['genere un deck', 'build report', 'page web', 'post LinkedIn']},
    {'slug': 'ds-iterate', 'num': 'S3', 'cat': 'CAPITALISATION', 'name': 'ds-iterate',
     'notion': 'https://www.notion.so/34fc2ce245e881709bfeec167d598115',
     'desc': 'Capitalise les Rex et propose des modifs sur memory/, rules/ ou layouts/ via PR GitHub. Mode manual ou scheduled (Monday 9h Paris). Niveaux risque A/B/C/D.',
     'triggers': ['capitalise les Rex', 'lance ds-iterate', 'retro DS', 'learning loop']},
    {'slug': 'ds-feedback', 'num': 'S4', 'cat': 'ATOMIQUE', 'name': 'ds-feedback',
     'notion': 'https://www.notion.so/34fc2ce245e88166bc23fa403fb75031',
     'desc': 'Log brut des Rex et feedbacks dans la DB Notion DS Feedback. Appelée par DS-Dataviz-generator et ds-file-assembler en phase 7, ou directement par Benoît.',
     'triggers': ['log feedback', 'note ce Rex', 'capture learning']}
]

DB_DEFS = [
    {'slug': 'media-assets', 'num': 'DB1', 'name': 'Media Assets',
     'notion': 'https://www.notion.so/25bd7cc0e7454f0f9cb8607870f59738',
     'collection': '8ca51a75-2413-4f72-8f2a-c44d445fa1d0',
     'desc': 'Working memory Notion pour les illustrations en cours, photos, partner logos, charts/maps en review. Lue par DS-Dataviz-generator (search similar) et ds-file-assembler (fetch media).',
     'props': ['Title', 'Type (chart/map/photo/picto)', 'Usage', 'Layout préféré', 'État', 'URL fichier', 'Tags']},
    {'slug': 'ds-feedback-db', 'num': 'DB2', 'name': 'DS Feedback',
     'notion': 'https://www.notion.so/d100a1de858f4d7d9391dbcd5c8cd7e0',
     'collection': 'd100a1de-858f-4d7d-9391-dbcd5c8cd7e0',
     'desc': 'Log brut des Rex écrit par ds-feedback. Lu par ds-iterate hebdo (Monday 9h Paris) pour cluster + diagnostic + PR.',
     'props': ['Title', 'Description', 'Livrable', 'Type', 'Severity', 'Source skill', 'Iterations', 'Blockers', 'Learnings', 'Rule to add', 'Tag']}
]

def workflow_card_svg(slug):
    # Simple SVG diagram per skill
    if slug == 'ds-dataviz-generator':
        return '''<svg viewBox="0 0 480 180" xmlns="http://www.w3.org/2000/svg"><rect x="20" y="55" width="80" height="80" rx="6" fill="#1C1F3B"/><text x="60" y="92" font-family="Poppins" font-weight="700" font-size="11" fill="#80C7C2" text-anchor="middle">DATA</text><text x="60" y="112" font-family="Raleway" font-size="9" fill="#FFF" text-anchor="middle" opacity="0.7">json</text><path d="M110 95 L 145 95" stroke="#435D74" stroke-width="2"/><polygon points="145,90 155,95 145,100" fill="#435D74"/><rect x="160" y="40" width="160" height="110" rx="6" fill="#FFF" stroke="#1C1F3B" stroke-width="2"/><line x1="180" y1="135" x2="300" y2="135" stroke="#1C1F3B" stroke-width="0.5"/><rect x="190" y="105" width="14" height="30" fill="#1C1F3B"/><rect x="210" y="85" width="14" height="50" fill="#1C1F3B"/><rect x="230" y="65" width="14" height="70" fill="#1C1F3B"/><rect x="250" y="80" width="14" height="55" fill="#435D74"/><rect x="270" y="100" width="14" height="35" fill="#435D74"/><rect x="290" y="75" width="14" height="60" fill="#80C7C2"/><text x="240" y="58" font-family="Poppins" font-weight="600" font-size="9" fill="#1C1F3B" text-anchor="middle">CHART · MAP · TABLE</text><path d="M330 95 L 365 95" stroke="#435D74" stroke-width="2"/><polygon points="365,90 375,95 365,100" fill="#435D74"/><rect x="380" y="55" width="80" height="80" rx="6" fill="#80C7C2"/><text x="420" y="92" font-family="Poppins" font-weight="700" font-size="11" fill="#1C1F3B" text-anchor="middle">.PNG</text><text x="420" y="112" font-family="Raleway" font-size="9" fill="#1C1F3B" text-anchor="middle">.svg .json</text></svg>'''
    elif slug == 'ds-file-assembler':
        return '''<svg viewBox="0 0 480 180" xmlns="http://www.w3.org/2000/svg"><rect x="20" y="50" width="90" height="90" rx="6" fill="#FFF" stroke="#1C1F3B" stroke-width="1.5"/><text x="65" y="78" font-family="Poppins" font-weight="700" font-size="10" fill="#1C1F3B" text-anchor="middle">CONTENU</text><text x="65" y="95" font-family="Raleway" font-size="8" fill="#435D74" text-anchor="middle">Notion source</text><text x="65" y="112" font-family="Poppins" font-weight="600" font-size="8" fill="#80C7C2" text-anchor="middle">📐 Layout</text><text x="65" y="125" font-family="Poppins" font-weight="600" font-size="8" fill="#80C7C2" text-anchor="middle">🖼️ Illustration</text><path d="M115 95 L 150 95" stroke="#435D74" stroke-width="2"/><polygon points="150,90 160,95 150,100" fill="#435D74"/><rect x="165" y="40" width="165" height="110" rx="6" fill="#1C1F3B"/><text x="247" y="68" font-family="Poppins" font-weight="700" font-size="11" fill="#80C7C2" text-anchor="middle">ds-file-assembler</text><text x="247" y="88" font-family="Raleway" font-size="8" fill="#FFF" text-anchor="middle" opacity="0.85">git pull · read rules</text><text x="247" y="103" font-family="Raleway" font-size="8" fill="#FFF" text-anchor="middle" opacity="0.7">duplicate template layout</text><text x="247" y="118" font-family="Raleway" font-size="8" fill="#FFF" text-anchor="middle" opacity="0.7">composition QA gate</text><text x="247" y="138" font-family="Poppins" font-weight="600" font-size="8" fill="#80C7C2" text-anchor="middle">1 question : validate?</text><path d="M335 95 L 370 95" stroke="#435D74" stroke-width="2"/><polygon points="370,90 380,95 370,100" fill="#435D74"/><rect x="385" y="50" width="80" height="90" rx="6" fill="#80C7C2"/><text x="425" y="80" font-family="Poppins" font-weight="700" font-size="10" fill="#1C1F3B" text-anchor="middle">LIVRABLE</text><text x="425" y="98" font-family="Raleway" font-size="8" fill="#1C1F3B" text-anchor="middle">.pptx</text><text x="425" y="112" font-family="Raleway" font-size="8" fill="#1C1F3B" text-anchor="middle">.docx</text><text x="425" y="126" font-family="Raleway" font-size="8" fill="#1C1F3B" text-anchor="middle">.html</text></svg>'''
    elif slug == 'ds-iterate':
        return '''<svg viewBox="0 0 480 180" xmlns="http://www.w3.org/2000/svg"><rect x="20" y="50" width="90" height="90" rx="6" fill="#FFF" stroke="#1C1F3B" stroke-width="1.5"/><text x="65" y="78" font-family="Poppins" font-weight="700" font-size="10" fill="#1C1F3B" text-anchor="middle">DS FEEDBACK</text><text x="65" y="95" font-family="Raleway" font-size="8" fill="#435D74" text-anchor="middle">DB Notion</text><rect x="35" y="105" width="60" height="6" rx="2" fill="#F9FCFF" stroke="#EAEBED"/><rect x="35" y="115" width="60" height="6" rx="2" fill="#F9FCFF" stroke="#EAEBED"/><rect x="35" y="125" width="60" height="6" rx="2" fill="#F9FCFF" stroke="#EAEBED"/><path d="M115 95 L 150 95" stroke="#435D74" stroke-width="2"/><polygon points="150,90 160,95 150,100" fill="#435D74"/><rect x="165" y="40" width="120" height="110" rx="6" fill="#1C1F3B"/><text x="225" y="68" font-family="Poppins" font-weight="700" font-size="11" fill="#80C7C2" text-anchor="middle">ds-iterate</text><text x="225" y="86" font-family="Raleway" font-size="8" fill="#FFF" text-anchor="middle" opacity="0.85">cluster · diagnostic</text><rect x="180" y="100" width="40" height="14" rx="3" fill="#80C7C2"/><text x="200" y="110" font-family="Poppins" font-weight="700" font-size="8" fill="#1C1F3B" text-anchor="middle">A</text><rect x="225" y="100" width="40" height="14" rx="3" fill="#80C7C2" opacity="0.7"/><text x="245" y="110" font-family="Poppins" font-weight="700" font-size="8" fill="#1C1F3B" text-anchor="middle">B</text><rect x="180" y="118" width="40" height="14" rx="3" fill="#E8546C" opacity="0.6"/><text x="200" y="128" font-family="Poppins" font-weight="700" font-size="8" fill="#FFF" text-anchor="middle">C</text><rect x="225" y="118" width="40" height="14" rx="3" fill="#E8546C" opacity="0.6"/><text x="245" y="128" font-family="Poppins" font-weight="700" font-size="8" fill="#FFF" text-anchor="middle">D</text><path d="M290 95 L 325 95" stroke="#435D74" stroke-width="2"/><polygon points="325,90 335,95 325,100" fill="#435D74"/><rect x="340" y="50" width="120" height="90" rx="6" fill="#FFF" stroke="#80C7C2" stroke-width="2"/><text x="400" y="78" font-family="Poppins" font-weight="700" font-size="10" fill="#1C1F3B" text-anchor="middle">PR GitHub</text><text x="400" y="98" font-family="Raleway" font-size="8" fill="#1C1F3B" text-anchor="middle">memory/*.md</text><text x="400" y="112" font-family="Raleway" font-size="8" fill="#1C1F3B" text-anchor="middle">docs/rules/*.md</text><text x="400" y="126" font-family="Raleway" font-size="8" fill="#1C1F3B" text-anchor="middle">docs/layouts/*.md</text></svg>'''
    elif slug == 'ds-feedback':
        return '''<svg viewBox="0 0 480 180" xmlns="http://www.w3.org/2000/svg"><rect x="20" y="50" width="120" height="40" rx="6" fill="#FFF" stroke="#1C1F3B" stroke-width="1.5"/><text x="80" y="68" font-family="Poppins" font-weight="700" font-size="9" fill="#1C1F3B" text-anchor="middle">DS-Dataviz</text><text x="80" y="82" font-family="Raleway" font-size="8" fill="#435D74" text-anchor="middle">phase 7</text><rect x="20" y="100" width="120" height="40" rx="6" fill="#FFF" stroke="#1C1F3B" stroke-width="1.5"/><text x="80" y="118" font-family="Poppins" font-weight="700" font-size="9" fill="#1C1F3B" text-anchor="middle">file-assembler</text><text x="80" y="132" font-family="Raleway" font-size="8" fill="#435D74" text-anchor="middle">phase 7</text><path d="M145 70 L 180 90" stroke="#435D74" stroke-width="2" stroke-dasharray="3,3"/><path d="M145 120 L 180 100" stroke="#435D74" stroke-width="2" stroke-dasharray="3,3"/><rect x="185" y="55" width="110" height="80" rx="6" fill="#1C1F3B"/><text x="240" y="85" font-family="Poppins" font-weight="700" font-size="12" fill="#80C7C2" text-anchor="middle">ds-feedback</text><text x="240" y="103" font-family="Raleway" font-size="8" fill="#FFF" text-anchor="middle" opacity="0.85">log atomique</text><text x="240" y="118" font-family="Raleway" font-size="8" fill="#FFF" text-anchor="middle" opacity="0.6">cluster mode</text><path d="M300 95 L 335 95" stroke="#435D74" stroke-width="2"/><polygon points="335,90 345,95 335,100" fill="#435D74"/><rect x="350" y="55" width="110" height="80" rx="6" fill="#FFF" stroke="#80C7C2" stroke-width="2"/><text x="405" y="80" font-family="Poppins" font-weight="700" font-size="10" fill="#1C1F3B" text-anchor="middle">DS FEEDBACK</text><text x="405" y="95" font-family="Poppins" font-weight="700" font-size="10" fill="#1C1F3B" text-anchor="middle">DB</text><text x="405" y="115" font-family="Raleway" font-size="8" fill="#435D74" text-anchor="middle">DB Notion</text></svg>'''
    return ''

def build_workflows():
    cards = []
    db_cards = []
    for w in WORKFLOW_DEFS:
        triggers_html = ' '.join(f'<code>{t}</code>' for t in w['triggers'])
        cards.append(f'''
<a class="card" href="workflows/{w['slug']}.html">
  <div class="thumb">{workflow_card_svg(w['slug'])}</div>
  <div class="meta">
    <div class="num">{w['num']} · {w['cat']}</div>
    <div class="name">{w['name']}</div>
    <div class="desc">{w['desc']}</div>
    <div class="triggers">{triggers_html}</div>
  </div>
</a>''')
    
    for db in DB_DEFS:
        props_html = ' · '.join(f"<code>{p}</code>" for p in db['props'][:5])
        if len(db['props']) > 5:
            props_html += '...'
        db_cards.append(f'''
<a class="card db-card" href="databases/{db['slug']}.html">
  <div class="meta">
    <div class="num">{db['num']} · NOTION DB</div>
    <div class="name">{db['name']}</div>
    <div class="desc">{db['desc']}</div>
    <div class="props">{props_html}</div>
  </div>
</a>''')
    page = f'''<!DOCTYPE html>
<html lang="fr">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>POF · Workflows et DBs · v3.4.0</title>
<link rel="stylesheet" href="styles.css">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&family=Raleway:wght@400;600&display=swap" rel="stylesheet">
<style>
.topbar{{position:sticky;top:0;z-index:50;background:#fff;border-bottom:1px solid var(--neutral-mid);padding:14px 32px;display:flex;align-items:center;gap:16px}}
.topbar .brand img{{height:26px}}.topbar .crumbs{{font-family:Poppins;font-size:11px;font-weight:600;color:var(--gray-600);letter-spacing:1px;text-transform:uppercase}}
.topbar .version{{font-family:Poppins;font-size:9px;font-weight:600;letter-spacing:1.5px;text-transform:uppercase;color:var(--teal-dark);background:rgba(128,199,194,.12);padding:3px 8px;border-radius:3px}}
.topbar-nav{{margin-left:auto;display:flex;gap:8px;flex-wrap:wrap}}
.topbar-nav a{{font-family:Poppins;font-size:10px;font-weight:600;letter-spacing:.5px;color:var(--navy);text-decoration:none;padding:8px 14px;border:1px solid var(--neutral-mid);border-radius:5px;text-transform:uppercase}}
.topbar-nav a:hover,.topbar-nav a.active{{border-color:var(--teal);background:rgba(128,199,194,.07)}}
.hero{{padding:48px 32px 24px;max-width:1280px;margin:0 auto}}
.hero h1{{font-family:Poppins;font-weight:700;font-size:36px;color:var(--navy);margin:0 0 8px}}
.hero p{{font-family:Raleway;font-size:14px;color:var(--gray-600);max-width:760px}}
.gallery{{max-width:1280px;margin:32px auto;padding:0 32px 96px}}
.gallery h2{{font-family:Poppins;font-weight:600;font-size:14px;letter-spacing:1.5px;color:var(--steel);text-transform:uppercase;margin:32px 0 16px;padding-left:14px;border-left:3px solid var(--steel-light)}}
.grid{{display:grid;grid-template-columns:repeat(2,1fr);gap:20px;margin-bottom:32px}}
.card{{display:block;text-decoration:none;color:inherit;background:#fff;border:1px solid var(--neutral-mid);border-radius:8px;overflow:hidden;transition:box-shadow 200ms,border-color 200ms}}
.card:hover{{border-color:var(--steel-light);box-shadow:0 12px 32px rgba(29,31,59,.08)}}
.thumb{{aspect-ratio:16/6;background:var(--gris-pof);border-bottom:1px solid var(--neutral-mid);display:flex;align-items:center;justify-content:center;padding:14px}}
.thumb svg{{width:100%;height:100%}}
.meta{{padding:18px 22px}}
.num{{font-family:Poppins;font-weight:700;font-size:11px;letter-spacing:2px;color:var(--steel-light)}}
.name{{font-family:Poppins;font-weight:600;font-size:18px;color:var(--navy);margin:4px 0 8px}}
.desc{{font-family:Raleway;font-size:13px;color:var(--gray-600);line-height:1.5;margin-bottom:10px}}
.triggers{{font-family:Poppins;font-size:9px;font-weight:600;letter-spacing:1px;color:var(--teal-dark);border-top:1px solid var(--neutral-mid);padding-top:10px;margin-top:8px}}
.triggers code{{background:rgba(128,199,194,.12);padding:2px 6px;border-radius:3px;color:var(--teal-dark);margin-right:4px;display:inline-block;margin-bottom:3px;font-family:Poppins;font-size:9px}}
.db-card .meta{{padding:24px}}
.db-card .props{{border-top:1px solid var(--neutral-mid);padding-top:12px;margin-top:14px;font-family:Raleway;font-size:11px;color:var(--steel)}}
.db-card .props code{{font-family:'Roboto Mono',monospace;font-size:10px;background:rgba(128,199,194,.1);padding:1px 5px;border-radius:3px;color:var(--teal-dark);margin:0 2px}}
@media(max-width:960px){{.grid{{grid-template-columns:1fr}}}}
</style>
</head>
<body>
<div class="topbar">
  <a class="brand" href="index.html"><img src="assets/logos/pof-logo-teal-white.svg" alt="POF"></a>
  <span class="crumbs">Design System · Workflows</span>
  <span class="version">v3.4.0</span>
  <nav class="topbar-nav">
    <a href="index.html">Overview</a>
    <a href="architecture.html">Architecture</a>
    <a href="charts.html">Charts</a>
    <a href="maps.html">Maps</a>
    <a href="icons.html">Icons</a>
    <a href="images.html">Images</a>
    <a href="workflows.html">Workflows</a>
    <a href="databases.html">DBs</a>
    <a href="https://github.com/benoitpof/design-system">GitHub</a>
  </nav>
</div>
<header class="hero">
  <h1>Workflows et bases de données</h1>
  <p>Skills Cowork qui pilotent la génération, l'assemblage, la capitalisation et le log + bases Notion (working memory). Chaque skill a sa page dédiée + sa spec Notion self-contained. Chaque DB pointe vers son schéma et ses utilisateurs.</p>
</header>
<div class="gallery">
<h2>Skills · 4 + 1 scheduled task</h2>
<div class="grid">
{''.join(cards)}
</div>
<h2 style="margin-top:64px">Bases de données · 2 Notion DBs · working memory</h2>
<div class="grid grid-db">
{''.join(db_cards)}
</div>
</div>
</body>
</html>'''
    (BUILD / 'workflows.html').write_text(page)

    # Sub-page per skill
    (BUILD / 'workflows').mkdir(exist_ok=True)
    for w in WORKFLOW_DEFS:
        sub = f'''<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{w['name']} · POF Workflows</title>
<link rel="stylesheet" href="../styles.css">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&family=Raleway:wght@400;600&display=swap" rel="stylesheet">
<style>
.topbar{{position:sticky;top:0;z-index:50;background:#fff;border-bottom:1px solid var(--neutral-mid);padding:14px 32px;display:flex;align-items:center;gap:16px}}
.topbar .brand img{{height:26px}}.topbar .crumbs{{font-family:Poppins;font-size:11px;font-weight:600;color:var(--gray-600);letter-spacing:1px;text-transform:uppercase}}
.topbar-nav{{margin-left:auto;display:flex;gap:8px;flex-wrap:wrap}}.topbar-nav a{{font-family:Poppins;font-size:10px;font-weight:600;color:var(--navy);text-decoration:none;padding:8px 14px;border:1px solid var(--neutral-mid);border-radius:5px;text-transform:uppercase}}.topbar-nav a:hover{{border-color:var(--teal)}}
.page-header{{padding:48px 32px 24px;max-width:1080px;margin:0 auto;border-bottom:1px solid var(--neutral-mid)}}
.page-header .eyebrow{{font-family:Poppins;font-weight:700;font-size:11px;letter-spacing:2px;color:var(--steel-light);text-transform:uppercase}}
.page-header h1{{font-family:Poppins;font-weight:700;font-size:36px;color:var(--navy);margin:8px 0 12px}}
.page-header .desc{{font-family:Raleway;font-size:15px;color:var(--steel);max-width:760px;line-height:1.6}}
.actions{{margin-top:24px;display:flex;gap:12px;flex-wrap:wrap}}
.btn{{font-family:Poppins;font-size:10px;font-weight:600;color:var(--navy);text-decoration:none;padding:10px 18px;border:1px solid var(--neutral-mid);border-radius:5px;text-transform:uppercase;background:#fff}}
.btn:hover{{border-color:var(--teal);background:rgba(128,199,194,.07)}}
.btn.primary{{background:var(--navy);color:#fff;border-color:var(--navy)}}
.btn.primary:hover{{background:var(--teal-dark);border-color:var(--teal-dark)}}
.diagram{{max-width:880px;margin:32px auto;padding:24px 32px;background:var(--gris-pof);border-radius:8px;border:1px solid var(--neutral-mid)}}
.diagram svg{{width:100%;height:auto}}
section.body{{max-width:880px;margin:0 auto;padding:32px;font-family:Raleway;font-size:15px;line-height:1.7;color:var(--body)}}
section.body h2{{font-family:Poppins;font-weight:700;font-size:20px;color:var(--navy);margin:32px 0 12px}}
section.body code{{font-family:'Roboto Mono',monospace;font-size:13px;background:#fff;padding:2px 6px;border-radius:3px;border:1px solid var(--neutral-mid)}}
section.body ul{{margin:0 0 16px 22px}}
.triggers-list code{{display:inline-block;background:rgba(128,199,194,.12);color:var(--teal-dark);padding:4px 10px;border-radius:3px;margin:0 6px 6px 0;font-family:Poppins;font-weight:600;font-size:11px;border:none}}
</style>
</head>
<body>
<div class="topbar">
<a class="brand" href="../index.html"><img src="../assets/logos/pof-logo-teal-white.svg" alt="POF"></a>
<span class="crumbs">Workflows / {w['name']}</span>
<nav class="topbar-nav">
<a href="../index.html">Overview</a>
<a href="../architecture.html">Architecture</a>
<a href="../workflows.html">← All workflows</a>
<a href="https://github.com/benoitpof/design-system">GitHub</a>
</nav>
</div>
<header class="page-header">
<div class="eyebrow">{w['num']} · {w['cat']}</div>
<h1>{w['name']}</h1>
<div class="desc">{w['desc']}</div>
<div class="actions">
<a class="btn primary" href="{w['notion']}" target="_blank">Spec complète Notion (self-contained)</a>
<a class="btn" href="../workflows.html">← Tous les workflows</a>
</div>
</header>
<div class="diagram">{workflow_card_svg(w['slug'])}</div>
<section class="body">
<h2>Trigger phrases</h2>
<div class="triggers-list">{' '.join(f'<code>{t}</code>' for t in w['triggers'])}</div>
<h2>Spec complète</h2>
<p>La spec détaillée (API, pipeline, inputs/outputs, dépendances, SKILL.md attendu, forbidden, exemples de lancement, effort de build) est dans la <a href="{w['notion']}" target="_blank">page Notion dédiée</a>. Cette page est <strong>self-contained</strong> : copy-paste son contenu dans un nouveau chat Cowork pour lancer le build via <code>/build-lead</code> Fast Track.</p>
<h2>Statut</h2>
<p>À builder via <code>/build-lead</code> Fast Track (effort 0.5 à 3 jours selon skill).</p>
</section>
</body></html>'''
        (BUILD / 'workflows' / f"{w['slug']}.html").write_text(sub)

build_workflows()
print('[6] Built workflows.html + 4 sub-pages')

# ---------- 7. Databases page + sub-pages ----------
def build_databases():
    cards = []
    for db in DB_DEFS:
        cards.append(f'''
<a class="card" href="databases/{db['slug']}.html">
  <div class="meta">
    <div class="num">{db['num']} · NOTION DB</div>
    <div class="name">{db['name']}</div>
    <div class="desc">{db['desc']}</div>
    <div class="props">{' · '.join(f'<code>{p}</code>' for p in db['props'][:5])}{'...' if len(db['props']) > 5 else ''}</div>
  </div>
</a>''')
    page = f'''<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>POF · Databases · v3.4.0</title>
<link rel="stylesheet" href="styles.css">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&family=Raleway:wght@400;600&display=swap" rel="stylesheet">
<style>
.topbar{{position:sticky;top:0;z-index:50;background:#fff;border-bottom:1px solid var(--neutral-mid);padding:14px 32px;display:flex;align-items:center;gap:16px}}
.topbar .brand img{{height:26px}}.topbar .crumbs{{font-family:Poppins;font-size:11px;font-weight:600;color:var(--gray-600);letter-spacing:1px;text-transform:uppercase}}
.topbar-nav{{margin-left:auto;display:flex;gap:8px;flex-wrap:wrap}}.topbar-nav a{{font-family:Poppins;font-size:10px;font-weight:600;color:var(--navy);text-decoration:none;padding:8px 14px;border:1px solid var(--neutral-mid);border-radius:5px;text-transform:uppercase}}.topbar-nav a:hover,.topbar-nav a.active{{border-color:var(--teal)}}
.hero{{padding:48px 32px 24px;max-width:1280px;margin:0 auto}}
.hero h1{{font-family:Poppins;font-weight:700;font-size:36px;color:var(--navy);margin:0 0 8px}}
.hero p{{font-family:Raleway;font-size:14px;color:var(--gray-600);max-width:760px}}
.gallery{{max-width:1280px;margin:32px auto;padding:0 32px 96px}}
.gallery h2{{font-family:Poppins;font-weight:600;font-size:14px;letter-spacing:1.5px;color:var(--steel);text-transform:uppercase;margin:32px 0 16px;padding-left:14px;border-left:3px solid var(--steel-light)}}
.grid{{display:grid;grid-template-columns:repeat(2,1fr);gap:20px}}
.card{{display:block;text-decoration:none;color:inherit;background:#fff;border:1px solid var(--neutral-mid);border-radius:8px;padding:24px;transition:box-shadow 200ms,border-color 200ms}}
.card:hover{{border-color:var(--steel-light);box-shadow:0 12px 32px rgba(29,31,59,.08)}}
.num{{font-family:Poppins;font-weight:700;font-size:11px;letter-spacing:2px;color:var(--steel-light)}}
.name{{font-family:Poppins;font-weight:600;font-size:20px;color:var(--navy);margin:4px 0 10px}}
.desc{{font-family:Raleway;font-size:13px;color:var(--gray-600);line-height:1.6;margin-bottom:14px}}
.props{{border-top:1px solid var(--neutral-mid);padding-top:12px;font-family:Raleway;font-size:11px;color:var(--steel)}}
.props code{{font-family:'Roboto Mono',monospace;font-size:11px;background:rgba(128,199,194,.1);padding:1px 5px;border-radius:3px;color:var(--teal-dark);margin:0 2px}}
@media(max-width:960px){{.grid{{grid-template-columns:1fr}}}}
</style>
</head>
<body>
<div class="topbar">
<a class="brand" href="index.html"><img src="assets/logos/pof-logo-teal-white.svg" alt="POF"></a>
<span class="crumbs">Design System · Databases</span>
<nav class="topbar-nav">
<a href="index.html">Overview</a>
<a href="architecture.html">Architecture</a>
<a href="charts.html">Charts</a>
<a href="maps.html">Maps</a>
<a href="icons.html">Icons</a>
<a href="images.html">Images</a>
<a href="workflows.html">Workflows</a>
<a href="databases.html" class="active">DBs</a>
<a href="https://github.com/benoitpof/design-system">GitHub</a>
</nav>
</div>
<header class="hero">
<h1>Databases · Notion working memory</h1>
<p>Notion est la working memory du DS. GitHub porte les règles, Notion porte les assets en cours et les feedbacks bruts. Lecture par les skills, écriture en pull-only depuis git-ops.</p>
</header>
<div class="gallery">
<h2>{len(DB_DEFS)} databases</h2>
<div class="grid">
{''.join(cards)}
</div>
</div>
</body></html>'''
    # Standalone databases.html removed (merged into workflows.html)
    (BUILD / 'databases.html').write_text(page)
    (BUILD / 'databases').mkdir(exist_ok=True)
    for db in DB_DEFS:
        sub = f'''<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{db['name']} · POF Databases</title>
<link rel="stylesheet" href="../styles.css">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&family=Raleway:wght@400;600&display=swap" rel="stylesheet">
<style>
.topbar{{position:sticky;top:0;z-index:50;background:#fff;border-bottom:1px solid var(--neutral-mid);padding:14px 32px;display:flex;align-items:center;gap:16px}}
.topbar .brand img{{height:26px}}.topbar-nav{{margin-left:auto;display:flex;gap:8px;flex-wrap:wrap}}.topbar-nav a{{font-family:Poppins;font-size:10px;font-weight:600;color:var(--navy);text-decoration:none;padding:8px 14px;border:1px solid var(--neutral-mid);border-radius:5px;text-transform:uppercase}}.topbar-nav a:hover{{border-color:var(--teal)}}
.page-header{{padding:48px 32px 24px;max-width:1080px;margin:0 auto;border-bottom:1px solid var(--neutral-mid)}}
.page-header .eyebrow{{font-family:Poppins;font-weight:700;font-size:11px;letter-spacing:2px;color:var(--steel-light);text-transform:uppercase}}
.page-header h1{{font-family:Poppins;font-weight:700;font-size:36px;color:var(--navy);margin:8px 0 12px}}
.page-header .desc{{font-family:Raleway;font-size:15px;color:var(--steel);max-width:760px;line-height:1.6}}
.actions{{margin-top:24px;display:flex;gap:12px;flex-wrap:wrap}}
.btn{{font-family:Poppins;font-size:10px;font-weight:600;color:var(--navy);text-decoration:none;padding:10px 18px;border:1px solid var(--neutral-mid);border-radius:5px;text-transform:uppercase;background:#fff}}
.btn:hover{{border-color:var(--teal);background:rgba(128,199,194,.07)}}
.btn.primary{{background:var(--navy);color:#fff;border-color:var(--navy)}}
section.body{{max-width:880px;margin:0 auto;padding:32px;font-family:Raleway;font-size:15px;line-height:1.7;color:var(--body)}}
section.body h2{{font-family:Poppins;font-weight:700;font-size:20px;color:var(--navy);margin:32px 0 12px}}
section.body code{{font-family:'Roboto Mono',monospace;font-size:13px;background:var(--gris-pof);padding:2px 6px;border-radius:3px;border:1px solid var(--neutral-mid)}}
section.body ul{{margin:0 0 16px 22px}}
section.body li{{margin:6px 0}}
</style>
</head>
<body>
<div class="topbar">
<a class="brand" href="../index.html"><img src="../assets/logos/pof-logo-teal-white.svg" alt="POF"></a>
<span class="crumbs">Databases / {db['name']}</span>
<nav class="topbar-nav">
<a href="../index.html">Overview</a>
<a href="../databases.html">← All DBs</a>
<a href="https://github.com/benoitpof/design-system">GitHub</a>
</nav>
</div>
<header class="page-header">
<div class="eyebrow">{db['num']} · NOTION DB</div>
<h1>{db['name']}</h1>
<div class="desc">{db['desc']}</div>
<div class="actions">
<a class="btn primary" href="{db['notion']}" target="_blank">Ouvrir dans Notion</a>
<a class="btn" href="../databases.html">← Toutes les DBs</a>
</div>
</header>
<section class="body">
<h2>Identifiants</h2>
<ul>
<li>Notion page : <a href="{db['notion']}" target="_blank">{db['notion']}</a></li>
<li>Collection ID : <code>{db['collection']}</code></li>
</ul>
<h2>Propriétés</h2>
<ul>
{chr(10).join(f'<li><code>{p}</code></li>' for p in db['props'])}
</ul>
<h2>Utilisée par</h2>
<ul>
<li>{('DS-Dataviz-generator (search similar) et ds-file-assembler (fetch media)') if 'media' in db['slug'] else ('ds-feedback (write log) et ds-iterate hebdo (read + cluster + PR)')}</li>
</ul>
</section>
</body></html>'''
        (BUILD / 'databases' / f"{db['slug']}.html").write_text(sub)

build_databases()
print('[7] Built databases.html + sub-pages')

# ---------- 8. Final stats ----------
total_files = sum(1 for _ in BUILD.rglob('*') if _.is_file())
print(f'\n=== BUILD COMPLETE ===')
print(f'Total files in _site/: {total_files}')
print(f'Generated at {datetime.now().isoformat()}')
