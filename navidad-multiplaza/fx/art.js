/* Ilustraciones vectoriales originales: <div class="nm-art" data-art="arbol"></div> se rellena con un SVG. */
(function () {
  var GOLD = '#C9A45C', GOLD_L = '#EBD9AE', NS = 'http://www.w3.org/2000/svg';
  function rng(seed) { return function () { seed |= 0; seed = seed + 0x6D2B79F5 | 0; var t = Math.imul(seed ^ seed >>> 15, 1 | seed);
    t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; }; }
  function u(r, a, b) { return a + r() * (b - a); }
  function f(n) { return Math.round(n * 10) / 10; }
  var DEFS = '<defs>' +
    '<radialGradient id="nmBg" cx="50%" cy="38%" r="75%"><stop offset="0" stop-color="#15523F"/><stop offset=".55" stop-color="#0F3B2E"/><stop offset="1" stop-color="#071A14"/></radialGradient>' +
    '<linearGradient id="nmGold" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F6E7BE"/><stop offset=".45" stop-color="#C9A45C"/><stop offset="1" stop-color="#8A6A2F"/></linearGradient>' +
    '<radialGradient id="nmOrb" cx="35%" cy="30%" r="70%"><stop offset="0" stop-color="#FFF6DC"/><stop offset=".25" stop-color="#E4C57E"/><stop offset=".7" stop-color="#B08A43"/><stop offset="1" stop-color="#6E5220"/></radialGradient>' +
    '<radialGradient id="nmOrbR" cx="35%" cy="30%" r="70%"><stop offset="0" stop-color="#FF8A9B"/><stop offset=".3" stop-color="#C21D3C"/><stop offset=".75" stop-color="#7A0C21"/><stop offset="1" stop-color="#3E0511"/></radialGradient>' +
    '<radialGradient id="nmOrbG" cx="35%" cy="30%" r="70%"><stop offset="0" stop-color="#7FC4A4"/><stop offset=".3" stop-color="#1F6B51"/><stop offset=".75" stop-color="#0F3B2E"/><stop offset="1" stop-color="#051510"/></radialGradient>' +
    '<radialGradient id="nmWarm" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#FFE9B0" stop-opacity=".95"/><stop offset="1" stop-color="#FFB950" stop-opacity="0"/></radialGradient>' +
    '<filter id="nmGlow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="2.2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>' +
    '<filter id="nmBlur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="6"/></filter></defs>';

  function bokeh(r, n, cols) { var s = ''; cols = cols || [GOLD_L, GOLD, '#fff'];
    for (var i = 0; i < n; i++) s += '<circle cx="' + f(u(r, 0, 400)) + '" cy="' + f(u(r, 0, 300)) + '" r="' + f(u(r, 6, 22)) +
      '" fill="' + cols[Math.floor(r() * cols.length)] + '" opacity="' + f(u(r, .06, .2) * 100) / 100 + '" filter="url(#nmBlur)"/>';
    return s; }
  function stars(r, n, ymax) { var s = ''; ymax = ymax || 300;
    for (var i = 0; i < n; i++) s += '<circle class="nm-tw" cx="' + f(u(r, 0, 400)) + '" cy="' + f(u(r, 0, ymax)) + '" r="' + f(u(r, .5, 1.4)) +
      '" fill="#fff" opacity="' + f(u(r, .3, .9)) + '" style="animation-delay:' + f(u(r, 0, 3)) + 's"/>';
    return s; }
  function star(cx, cy, R, p, inner) { var pts = []; p = p || 8; inner = inner || .42;
    for (var i = 0; i < p * 2; i++) { var a = Math.PI * i / p - Math.PI / 2, rr = i % 2 ? R * inner : R;
      pts.push(f(cx + rr * Math.cos(a)) + ',' + f(cy + rr * Math.sin(a))); }
    return pts.join(' '); }

  var ART = {
    arbol: function (r) {
      var s = bokeh(r, 14) + stars(r, 30), d = '', top = 58, bottom = 262, cx = 200, half = 92, n = 170;
      for (var i = 0; i < n; i++) { var t = i / n, y = top + t * (bottom - top), a = t * 14 * Math.PI, x = cx + t * half * Math.cos(a),
        dp = (Math.sin(a) + 1) / 2;
        d += '<circle class="nm-tw" cx="' + f(x) + '" cy="' + f(y) + '" r="' + f(.9 + dp * 1.8) + '" fill="' + (dp > .5 ? GOLD_L : GOLD) +
          '" opacity="' + f(.35 + dp * .65) + '" style="animation-delay:' + f((i % 17) * .18) + 's"/>'; }
      return s + '<g filter="url(#nmGlow)">' + d + '</g><ellipse cx="200" cy="268" rx="110" ry="9" fill="url(#nmWarm)" opacity=".35"/>' +
        '<circle cx="200" cy="50" r="30" fill="url(#nmWarm)" opacity=".5"/><g class="nm-spin" style="transform-origin:200px 50px" filter="url(#nmGlow)">' +
        '<polygon points="' + star(200, 50, 15) + '" fill="url(#nmGold)"/></g>';
    },
    villa: function (r) {
      var s = stars(r, 40, 170) + bokeh(r, 8) + '<path d="M0 238 Q100 222 200 232 T400 226 V300 H0Z" fill="#F6F1E6" opacity=".92"/>';
      [[40, 70, 88, '#0B2C22'], [112, 62, 104, '#123F31'], [178, 84, 120, '#0B2C22'], [262, 64, 98, '#123F31'], [326, 58, 84, '#0B2C22']].forEach(function (h) {
        var x = h[0], w = h[1], base = 236, top = base - h[2], roof = top - w * .45;
        s += '<path d="M' + x + ' ' + base + ' V' + top + ' L' + f(x + w / 2) + ' ' + f(roof) + ' L' + (x + w) + ' ' + top + ' V' + base + 'Z" fill="' + h[3] + '"/>' +
          '<path d="M' + (x - 4) + ' ' + (top + 2) + ' L' + f(x + w / 2) + ' ' + f(roof - 3) + ' L' + (x + w + 4) + ' ' + (top + 2) +
          '" fill="none" stroke="#F6F1E6" stroke-width="5" stroke-linecap="round" opacity=".9"/>';
        for (var wy = top + 14; wy < base - 20; wy += 28) [x + w * .22, x + w * .6].forEach(function (wx) {
          s += '<circle cx="' + f(wx + w * .09) + '" cy="' + (wy + 7) + '" r="14" fill="url(#nmWarm)" opacity=".45"/>' +
            '<rect class="nm-tw" x="' + f(wx) + '" y="' + wy + '" width="' + f(w * .18) + '" height="14" rx="2" fill="#FFD98A" style="animation-delay:' + f(u(r, 0, 3)) + 's"/>'; });
      });
      var line = '', lights = '';
      for (var i = 0; i < 16; i++) { var lx = 20 + i * 24, ly = f(150 + 8 * Math.sin(i * .9)); line += (i ? ' L' : 'M') + lx + ' ' + ly;
        lights += '<circle class="nm-tw" cx="' + lx + '" cy="' + ly + '" r="2.2" fill="' + (i % 2 ? GOLD_L : '#FF9AA8') + '" style="animation-delay:' + f(i * .2) + 's"/>'; }
      return s + '<path d="' + line + '" fill="none" stroke="#0B2C22" stroke-width=".8" opacity=".6"/><g filter="url(#nmGlow)">' + lights + '</g>';
    },
    musica: function (r) {
      var s = bokeh(r, 16) + stars(r, 20);
      for (var i = 0; i < 7; i++) { var y = 110 + i * 14, a = 40 - i * 3;
        s += '<path class="nm-flow" d="M-10 ' + y + ' C 90 ' + (y - a) + ' 150 ' + (y + a) + ' 210 ' + y + ' S 330 ' + (y - a) + ' 410 ' + (y + 6) +
          '" fill="none" stroke="url(#nmGold)" stroke-width="' + f(2.2 - i * .22) + '" opacity="' + f(.95 - i * .1) + '" style="animation-delay:' + f(i * .25) + 's"/>'; }
      [[120, 92, 1], [238, 150, .8], [300, 96, .9]].forEach(function (n) {
        s += '<g transform="translate(' + n[0] + ' ' + n[1] + ') scale(' + n[2] + ')" fill="url(#nmGold)" filter="url(#nmGlow)">' +
          '<ellipse cx="0" cy="22" rx="7" ry="5" transform="rotate(-20 0 22)"/><rect x="5" y="-12" width="2" height="34"/><path d="M7 -12 Q20 -6 16 6 Q14 -2 7 -2Z"/></g>'; });
      return s;
    },
    regalo: function (r) {
      var s = bokeh(r, 14) + stars(r, 24) + '<ellipse cx="200" cy="262" rx="120" ry="10" fill="#000" opacity=".25"/>' +
        '<rect x="130" y="140" width="140" height="118" rx="6" fill="url(#nmOrbR)"/><rect x="118" y="118" width="164" height="32" rx="6" fill="#9B1530"/>' +
        '<rect x="190" y="118" width="20" height="140" fill="url(#nmGold)"/><rect x="118" y="126" width="164" height="12" fill="url(#nmGold)" opacity=".95"/>' +
        '<path d="M200 120 C170 80 140 92 150 108 C158 122 184 122 200 120Z" fill="url(#nmGold)"/><path d="M200 120 C230 80 260 92 250 108 C242 122 216 122 200 120Z" fill="url(#nmGold)"/>' +
        '<circle cx="200" cy="119" r="8" fill="#F6E7BE"/>';
      [[110, 80, 7], [292, 70, 9], [320, 150, 5], [84, 170, 6]].forEach(function (p) {
        s += '<g class="nm-spin" style="transform-origin:' + p[0] + 'px ' + p[1] + 'px" filter="url(#nmGlow)"><polygon points="' + star(p[0], p[1], p[2], 4, .3) + '" fill="' + GOLD_L + '"/></g>'; });
      return s;
    },
    esferas: function (r) {
      var s = bokeh(r, 18);
      [[120, 170, 46, 'nmOrb', 0], [212, 128, 38, 'nmOrbR', .6], [292, 186, 42, 'nmOrbG', 1.2]].forEach(function (o) {
        var x = o[0], y = o[1], R = o[2], hx = f(x - R * .35), hy = f(y - R * .4);
        s += '<g class="nm-sway" style="transform-origin:' + x + 'px 0px;animation-delay:' + o[4] + 's"><line x1="' + x + '" y1="0" x2="' + x + '" y2="' + (y - R - 8) + '" stroke="' + GOLD + '" stroke-width="1"/>' +
          '<rect x="' + (x - 8) + '" y="' + (y - R - 10) + '" width="16" height="10" rx="2" fill="url(#nmGold)"/><circle cx="' + x + '" cy="' + y + '" r="' + R + '" fill="url(#' + o[3] + ')"/>' +
          '<path d="M' + f(x - R * .8) + ' ' + (y - 4) + ' Q' + x + ' ' + (y + 10) + ' ' + f(x + R * .8) + ' ' + (y - 4) + '" fill="none" stroke="' + GOLD_L + '" stroke-width="1.2" opacity=".7"/>' +
          '<ellipse cx="' + hx + '" cy="' + hy + '" rx="' + f(R * .22) + '" ry="' + f(R * .12) + '" fill="#fff" opacity=".55" transform="rotate(-30 ' + hx + ' ' + hy + ')"/></g>'; });
      return s;
    },
    copo: function (r) {
      var s = bokeh(r, 12) + stars(r, 30), arms = '';
      for (var k = 0; k < 6; k++) arms += '<g transform="rotate(' + k * 60 + ' 200 150)"><line x1="200" y1="150" x2="200" y2="62"/>' +
        '<polyline points="184,96 200,80 216,96" fill="none"/><polyline points="188,118 200,106 212,118" fill="none"/><circle cx="200" cy="58" r="4"/></g>';
      return s + '<g class="nm-spin-slow" style="transform-origin:200px 150px" stroke="#D9B970" stroke-width="2.2" stroke-linecap="round" fill="' + GOLD_L + '" filter="url(#nmGlow)">' +
        arms + '<polygon points="' + star(200, 150, 14, 6, .55) + '" fill="url(#nmGold)" stroke="none"/></g>';
    },
    guirnalda: function (r) {
      var s = bokeh(r, 20, [GOLD_L, '#FFB950', '#fff']) + stars(r, 18);
      [[70, 60], [150, 50], [225, 40]].forEach(function (row, ri) {
        var d = '', i = 0;
        for (var x = -10; x <= 410; x += 10, i++) { var y = f(row[0] + row[1] * Math.sin(Math.PI * x / 400)); d += (i ? ' L' : 'M') + x + ' ' + y;
          if (i % 3 === 1) s += '<circle cx="' + x + '" cy="' + f(+y + 6) + '" r="10" fill="url(#nmWarm)" opacity=".7"/><circle class="nm-tw" cx="' + x + '" cy="' + f(+y + 6) +
            '" r="3.2" fill="#FFE3A3" style="animation-delay:' + f(((i + ri) * .23) % 3) + 's"/>'; }
        s = '<path d="' + d + '" fill="none" stroke="#1F6B51" stroke-width="1.2" opacity=".8"/>' + s; });
      return s;
    },
    estrella: function (r) {
      var s = bokeh(r, 16) + stars(r, 40), rays = '';
      for (var a = 0; a < 360; a += 15) rays += '<line x1="200" y1="150" x2="' + f(200 + 150 * Math.cos(a * Math.PI / 180)) + '" y2="' + f(150 + 150 * Math.sin(a * Math.PI / 180)) + '"/>';
      return s + '<g stroke="' + GOLD_L + '" stroke-width=".6" opacity=".35">' + rays + '</g><circle cx="200" cy="150" r="70" fill="url(#nmWarm)" opacity=".45"/>' +
        '<g class="nm-spin-slow" style="transform-origin:200px 150px" filter="url(#nmGlow)"><polygon points="' + star(200, 150, 58, 8, .4) + '" fill="url(#nmGold)"/>' +
        '<polygon points="' + star(200, 150, 30, 8, .4) + '" fill="#F6E7BE" opacity=".7"/></g>';
    }
  };
  var SEEDS = { arbol: 7, villa: 11, musica: 5, regalo: 3, esferas: 21, copo: 9, guirnalda: 4, estrella: 13 };

  function paint() {
    if (!document.getElementById('nmArtDefs')) {
      var holder = document.createElementNS(NS, 'svg');
      holder.setAttribute('id', 'nmArtDefs'); holder.setAttribute('width', '0'); holder.setAttribute('height', '0');
      holder.setAttribute('aria-hidden', 'true'); holder.style.position = 'absolute';
      holder.innerHTML = DEFS; document.body.appendChild(holder);
    }
    document.querySelectorAll('.nm-art[data-art]:not([data-done])').forEach(function (el) {
      var k = el.getAttribute('data-art'); if (!ART[k]) return;
      el.innerHTML = '<svg viewBox="0 0 400 300" preserveAspectRatio="xMidYMid slice" role="img" aria-label="' +
        (el.getAttribute('data-label') || '') + '"><rect width="400" height="300" fill="url(#nmBg)"/>' + ART[k](rng(SEEDS[k])) + '</svg>';
      el.setAttribute('data-done', '1');
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', paint); else paint();
  window.nmPaintArt = paint;
})();
