/* charts/_trio.js — render light / dark / highlight trio per chart */
(function(){

// Compact SVG templates per chart. Element marked data-hl="1" is the highlight target.
// Colors used: navy #1C1F3B, steel #435D74, steelLight #5F7D95, pale #CFD9E0, teal #80C7C2, coral #E8546C
const T = {
'01': `<svg viewBox="0 0 220 130" xmlns="http://www.w3.org/2000/svg">
<text x="20" y="34" font-family="Poppins" font-weight="600" font-size="9" letter-spacing="2" fill="#5F7D95">2025 IMPACT</text>
<line x1="20" y1="44" x2="44" y2="44" stroke="#5F7D95" stroke-width="2"/>
<text x="20" y="86" font-family="Poppins" font-weight="700" font-size="42" fill="#1C1F3B" data-hl="1">200</text>
<text x="20" y="106" font-family="Raleway" font-size="10" fill="#6C757D">factories by 2030</text>
<text x="20" y="120" font-family="Poppins" font-weight="600" font-size="9" fill="#5F7D95">▲ from 4 today</text>
</svg>`,
'02': `<svg viewBox="0 0 220 130" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="110" x2="200" y2="110" stroke="#1C1F3B" stroke-width="0.8"/>
<rect x="32" y="74" width="22" height="36" fill="#1C1F3B" rx="2"/>
<rect x="62" y="56" width="22" height="54" fill="#1C1F3B" rx="2"/>
<rect x="92" y="34" width="22" height="76" fill="#1C1F3B" rx="2" data-hl="1"/>
<rect x="122" y="50" width="22" height="60" fill="#5F7D95" rx="2"/>
<rect x="152" y="64" width="22" height="46" fill="#5F7D95" rx="2"/>
<rect x="182" y="48" width="22" height="62" fill="#5F7D95" rx="2"/>
</svg>`,
'03': `<svg viewBox="0 0 220 130" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="110" x2="200" y2="110" stroke="#1C1F3B" stroke-width="0.8"/>
<g><path d="M32,80 L60,80 L60,110 L32,110 Z" fill="#1C1F3B"/><path d="M32,58 L60,58 L60,80 L32,80 Z" fill="#5F7D95"/><path d="M32,42 A2,2 0 0,1 34,40 L58,40 A2,2 0 0,1 60,42 L60,58 L32,58 Z" fill="#CFD9E0"/></g>
<g><path d="M68,74 L96,74 L96,110 L68,110 Z" fill="#1C1F3B"/><path d="M68,50 L96,50 L96,74 L68,74 Z" fill="#5F7D95"/><path d="M68,32 A2,2 0 0,1 70,30 L94,30 A2,2 0 0,1 96,32 L96,50 L68,50 Z" fill="#CFD9E0"/></g>
<g><path d="M104,68 L132,68 L132,110 L104,110 Z" fill="#1C1F3B"/><path d="M104,42 L132,42 L132,68 L104,68 Z" fill="#5F7D95"/><path d="M104,24 A2,2 0 0,1 106,22 L130,22 A2,2 0 0,1 132,24 L132,42 L104,42 Z" fill="#CFD9E0"/></g>
<g><path d="M140,60 L168,60 L168,110 L140,110 Z" fill="#1C1F3B" data-hl="1"/><path d="M140,34 L168,34 L168,60 L140,60 Z" fill="#5F7D95"/><path d="M140,16 A2,2 0 0,1 142,14 L166,14 A2,2 0 0,1 168,16 L168,34 L140,34 Z" fill="#CFD9E0"/></g>
</svg>`,
'04': `<svg viewBox="0 0 220 130" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="110" x2="200" y2="110" stroke="#1C1F3B" stroke-width="0.8"/>
<rect x="32" y="56" width="14" height="54" fill="#5F7D95" rx="2"/><rect x="48" y="46" width="14" height="64" fill="#1C1F3B" rx="2"/>
<rect x="78" y="64" width="14" height="46" fill="#5F7D95" rx="2"/><rect x="94" y="50" width="14" height="60" fill="#1C1F3B" rx="2"/>
<rect x="124" y="42" width="14" height="68" fill="#5F7D95" rx="2"/><rect x="140" y="30" width="14" height="80" fill="#1C1F3B" rx="2" data-hl="1"/>
<rect x="170" y="36" width="14" height="74" fill="#5F7D95" rx="2"/><rect x="186" y="22" width="14" height="88" fill="#1C1F3B" rx="2"/>
</svg>`,
'05': `<svg viewBox="0 0 220 130" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="110" x2="200" y2="110" stroke="#1C1F3B" stroke-width="0.8"/>
<polyline points="28,98 64,86 100,72 136,52 172,30 200,20" fill="none" stroke="#1C1F3B" stroke-width="2"/>
<polyline points="28,104 64,98 100,88 136,76 172,58 200,46" fill="none" stroke="#5F7D95" stroke-width="1.5" stroke-dasharray="4,3"/>
<circle cx="172" cy="30" r="4" fill="#1C1F3B" data-hl="1"/>
</svg>`,
'06': `<svg viewBox="0 0 220 130" xmlns="http://www.w3.org/2000/svg">
<g transform="translate(110,68)">
<path d="M 0,-40 A 40,40 0 1,1 -22.4,33.2 L -13.4,19.9 A 24,24 0 1,0 0,-24 Z" fill="#1C1F3B" data-hl="1"/>
<path d="M -22.4,33.2 A 40,40 0 0,1 -38.0,-12.4 L -22.8,-7.4 A 24,24 0 0,0 -13.4,19.9 Z" fill="#5F7D95"/>
<path d="M -38.0,-12.4 A 40,40 0 0,1 0,-40 L 0,-24 A 24,24 0 0,0 -22.8,-7.4 Z" fill="#CFD9E0"/>
</g>
</svg>`,
'07': `<svg viewBox="0 0 220 130" xmlns="http://www.w3.org/2000/svg">
<rect x="20" y="34" width="180" height="10" rx="5" fill="#EAEBED"/><rect x="20" y="34" width="120" height="10" rx="5" fill="#1C1F3B"/>
<rect x="20" y="60" width="180" height="10" rx="5" fill="#EAEBED"/><rect x="20" y="60" width="160" height="10" rx="5" fill="#1C1F3B" data-hl="1"/>
<rect x="20" y="86" width="180" height="10" rx="5" fill="#EAEBED"/><rect x="20" y="86" width="80" height="10" rx="5" fill="#5F7D95"/>
</svg>`,
'08': `<svg viewBox="0 0 220 130" xmlns="http://www.w3.org/2000/svg">
<polygon points="40,20 180,20 162,42 58,42" fill="#1C1F3B"/>
<polygon points="60,46 160,46 144,68 76,68" fill="#1C1F3B" opacity="0.85"/>
<polygon points="78,72 142,72 128,94 92,94" fill="#435D74"/>
<polygon points="94,98 126,98 116,116 104,116" fill="#1C1F3B" data-hl="1"/>
</svg>`,
'09': `<svg viewBox="0 0 220 130" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="68" x2="200" y2="68" stroke="#CFD9E0" stroke-width="2"/>
<line x1="20" y1="68" x2="140" y2="68" stroke="#1C1F3B" stroke-width="2"/>
<circle cx="20" cy="68" r="5" fill="#1C1F3B"/>
<circle cx="60" cy="68" r="5" fill="#1C1F3B"/>
<circle cx="100" cy="68" r="5" fill="#1C1F3B"/>
<circle cx="140" cy="68" r="7" fill="#1C1F3B" data-hl="1"/>
<circle cx="180" cy="68" r="5" fill="none" stroke="#5F7D95" stroke-width="2"/>
</svg>`,
'10': `<svg viewBox="0 0 220 130" xmlns="http://www.w3.org/2000/svg">
<rect x="40" y="22" width="60" height="14" fill="#1C1F3B" rx="2"/>
<rect x="70" y="42" width="80" height="14" fill="#435D74" rx="2"/>
<rect x="100" y="62" width="70" height="14" fill="#5F7D95" rx="2" data-hl="1"/>
<rect x="130" y="82" width="60" height="14" fill="#CFD9E0" rx="2"/>
<line x1="130" y1="14" x2="130" y2="108" stroke="#1C1F3B" stroke-dasharray="3,3" stroke-width="1"/>
</svg>`,
'11': `<svg viewBox="0 0 220 130" xmlns="http://www.w3.org/2000/svg">
<rect x="20" y="34" width="6" height="36" fill="#1C1F3B"/>
<rect x="20" y="78" width="6" height="20" fill="#435D74"/>
<rect x="105" y="38" width="6" height="56" fill="#1C1F3B"/>
<rect x="194" y="34" width="6" height="40" fill="#1C1F3B" data-hl="1"/>
<rect x="194" y="82" width="6" height="20" fill="#5F7D95"/>
<path d="M 26,52 C 65,52 65,60 111,60" stroke="#1C1F3B" stroke-width="36" fill="none" opacity="0.45"/>
<path d="M 26,88 C 65,88 65,82 111,82" stroke="#435D74" stroke-width="20" fill="none" opacity="0.45"/>
<path d="M 111,54 C 152,54 152,54 200,54" stroke="#1C1F3B" stroke-width="40" fill="none" opacity="0.45"/>
<path d="M 111,88 C 152,88 152,92 200,92" stroke="#5F7D95" stroke-width="20" fill="none" opacity="0.4"/>
</svg>`,
'12': `<svg viewBox="0 0 220 130" xmlns="http://www.w3.org/2000/svg">
<rect x="14" y="50" width="32" height="30" fill="#1C1F3B" rx="2"/>
<rect x="54" y="50" width="32" height="30" fill="#1C1F3B" opacity="0.85" rx="2"/>
<rect x="94" y="50" width="32" height="30" fill="#435D74" rx="2"/>
<rect x="134" y="50" width="32" height="30" fill="#5F7D95" rx="2" data-hl="1"/>
<rect x="174" y="50" width="32" height="30" fill="#CFD9E0" rx="2"/>
<g stroke="#1C1F3B" stroke-width="1" fill="none">
<path d="M 46,65 L 54,65"/><path d="M 86,65 L 94,65"/><path d="M 126,65 L 134,65"/><path d="M 166,65 L 174,65"/>
</g>
</svg>`,
'13': `<svg viewBox="0 0 220 130" xmlns="http://www.w3.org/2000/svg">
<rect x="90" y="14" width="40" height="20" fill="#1C1F3B" rx="2" data-hl="1"/>
<line x1="110" y1="34" x2="110" y2="50" stroke="#1C1F3B"/>
<line x1="40" y1="50" x2="180" y2="50" stroke="#1C1F3B"/>
<line x1="40" y1="50" x2="40" y2="64" stroke="#1C1F3B"/>
<line x1="110" y1="50" x2="110" y2="64" stroke="#1C1F3B"/>
<line x1="180" y1="50" x2="180" y2="64" stroke="#1C1F3B"/>
<rect x="20" y="64" width="40" height="20" fill="#435D74" rx="2"/>
<rect x="90" y="64" width="40" height="20" fill="#435D74" rx="2"/>
<rect x="160" y="64" width="40" height="20" fill="#435D74" rx="2"/>
<rect x="0" y="98" width="40" height="16" fill="#5F7D95" rx="2"/>
<rect x="50" y="98" width="40" height="16" fill="#5F7D95" rx="2"/>
<rect x="120" y="98" width="40" height="16" fill="#5F7D95" rx="2"/>
<rect x="180" y="98" width="40" height="16" fill="#5F7D95" rx="2"/>
</svg>`,
'14': `<svg viewBox="0 0 220 130" xmlns="http://www.w3.org/2000/svg">
<rect x="20" y="20" width="180" height="14" fill="#1C1F3B"/>
<rect x="20" y="34" width="180" height="14" fill="#FFFFFF" stroke="#EAEBED" stroke-width="0.5"/>
<rect x="20" y="48" width="180" height="14" fill="#F9FCFF" stroke="#EAEBED" stroke-width="0.5"/>
<rect x="20" y="62" width="180" height="14" fill="#FFFFFF" stroke="#EAEBED" stroke-width="0.5"/>
<rect x="20" y="76" width="180" height="14" fill="#F9FCFF" stroke="#EAEBED" stroke-width="0.5"/>
<rect x="20" y="90" width="180" height="14" fill="#FFFFFF" stroke="#EAEBED" stroke-width="0.5"/>
<rect x="90" y="20" width="56" height="84" fill="#E8546C" opacity="0.10" data-hl="1"/>
<rect x="90" y="20" width="56" height="2" fill="#1C1F3B"/>
</svg>`,
'15': `<svg viewBox="0 0 220 130" xmlns="http://www.w3.org/2000/svg">
<g transform="translate(110,68)">
<polygon points="0,-50 43,-25 43,25 0,50 -43,25 -43,-25" fill="none" stroke="#EAEBED"/>
<polygon points="0,-34 30,-17 30,17 0,34 -30,17 -30,-17" fill="none" stroke="#EAEBED"/>
<polygon points="0,-46 38,-15 36,28 -4,42 -38,18 -32,-22" fill="#1C1F3B" fill-opacity="0.3" stroke="#1C1F3B" stroke-width="1.5" data-hl="1"/>
<polygon points="0,-30 28,-12 26,20 -2,28 -26,16 -22,-14" fill="#5F7D95" fill-opacity="0.18" stroke="#5F7D95" stroke-width="1" stroke-dasharray="3,2"/>
</g>
</svg>`,
'16': `<svg viewBox="0 0 220 130" xmlns="http://www.w3.org/2000/svg">
<!-- Stylized world: a few schematic continent blobs + bubbles -->
<g fill="#EAEBED" stroke="#FFFFFF" stroke-width="0.6">
<path d="M22,38 Q34,28 50,30 L74,28 Q90,32 92,46 L88,58 L70,56 L54,62 L36,58 Q24,52 22,38 Z"/>
<path d="M44,72 Q58,68 72,72 L82,90 L74,108 L60,110 L52,96 Q44,86 44,72 Z"/>
<path d="M104,40 Q120,32 138,34 L160,30 Q180,32 196,42 L200,58 L182,62 L160,60 L140,64 L120,62 Q108,54 104,40 Z"/>
<path d="M132,72 Q150,68 166,74 L160,90 L150,98 Q140,90 132,72 Z"/>
<path d="M178,76 Q190,72 200,80 L196,92 L184,90 Q176,84 178,76 Z" data-hl="1"/>
</g>
<!-- Bubbles -->
<circle cx="62" cy="76" r="6" fill="#80C7C2" fill-opacity="0.6" stroke="#2BA595" stroke-width="1"/>
<circle cx="146" cy="80" r="9" fill="#80C7C2" fill-opacity="0.6" stroke="#2BA595" stroke-width="1"/>
<circle cx="186" cy="82" r="5" fill="#1C1F3B" fill-opacity="0.85" data-hl="1"/>
<text x="146" y="84" font-family="Poppins" font-weight="700" font-size="9" fill="#FFFFFF" text-anchor="middle">7</text>
</svg>`
};

// Color swap for dark cell. Keep teal/coral as-is (they pop on dark).
function darkSwap(svg){
  return svg
    .replace(/fill="#1C1F3B"/g, 'fill="#FFFFFF"')
    .replace(/fill="#435D74"/g, 'fill="#80C7C2"')
    .replace(/fill="#5F7D95"/g, 'fill="#9DB1C2"')
    .replace(/fill="#CFD9E0"/g, 'fill="#5F7D95"')
    .replace(/fill="#EAEBED"/g, 'fill="#3A4A66"')
    .replace(/fill="#F9FCFF"/g, 'fill="#252845"')
    .replace(/fill="#FFFFFF" stroke="#EAEBED"/g, 'fill="#252845" stroke="#3A4A66"')
    .replace(/stroke="#1C1F3B"/g, 'stroke="#FFFFFF"')
    .replace(/stroke="#EAEBED"/g, 'stroke="#3A4A66"')
    .replace(/stroke="#CFD9E0"/g, 'stroke="#5F7D95"')
    .replace(/fill="#6C757D"/g, 'fill="#9DB1C2"')
    .replace(/fill="#2BA595"/g, 'fill="#80C7C2"');
}

// Highlight: change all data-hl="1" element fills/strokes to coral
function highlightSwap(svg){
  return svg.replace(/(<[^>]*data-hl="1"[^>]*>)/g, function(tag){
    let t = tag;
    if(/fill="[^"]+"/.test(t)) t = t.replace(/fill="[^"]+"/, 'fill="#E8546C"');
    if(/stroke="#1C1F3B"/.test(t)) t = t.replace(/stroke="#1C1F3B"/, 'stroke="#E8546C"');
    return t;
  });
}

function render(){
  document.querySelectorAll('[data-trio]').forEach(host => {
    const key = host.getAttribute('data-trio');
    const tpl = T[key];
    if(!tpl){ host.textContent = '(missing trio template '+key+')'; return; }
    host.innerHTML = `
      <div class="trio-cell light"><div class="trio-tag">LIGHT · NEUTRAL</div>${tpl}</div>
      <div class="trio-cell dark"><div class="trio-tag">DARK · NAVY</div>${darkSwap(tpl)}</div>
      <div class="trio-cell gris"><div class="trio-tag">HIGHLIGHT · CORAL</div>${highlightSwap(tpl)}</div>
    `;
  });
}

if(document.readyState !== 'loading') render();
else document.addEventListener('DOMContentLoaded', render);
})();
