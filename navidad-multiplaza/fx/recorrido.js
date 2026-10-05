/* Banner de Navidad Multiplaza: recorrido en video con controles (escenas, pausa, sonido y pantalla completa).
   Reemplaza el reel de la portada. Las escenas de video se reproducen tal cual; las de render llevan un
   movimiento de cámara lento. Se pausa solo cuando el banner sale de la pantalla o la pestaña se oculta. */
(function () {
  var d = document, root = d.documentElement;
  if (d.body && d.body.classList.contains('elementor-editor-active')) return;
  var U = '/wp-content/uploads/2026/09/';
  // [tipo, archivo, escena, lugar, póster del video]
  var S = [
    ['v', 'nm26-fachada-esc-principal.mp4', 'Fachada principal', 'Escazú', 'nm26-fachada-esc-principal-1024x682.jpg'],
    ['i', 'nm26-tunel-arcos-render-1-1536x1346.jpg', 'Túnel de arcos', 'Escazú'],
    ['i', 'nm26-plaza-starbucks-render.jpg', 'Plaza Starbucks', 'Escazú'],
    ['v', 'nm26-fachada-esc-universal.mp4', 'Fachada Universal', 'Escazú', 'nm26-fachada-esc-universal-1024x768.jpg'],
    ['i', 'nm26-plaza-tukis-render-3.jpg', 'Plaza Tukis', 'Escazú'],
    ['i', 'nm26-plaza-brunos-render-1-1536x835.jpg', 'Plaza Brunos', 'Escazú'],
    ['i', 'nm26-vacio-esc-esferas.jpg', 'Vacíos', 'Escazú'],
    ['i', 'nm26-quinta-etapa-render-1536x864.jpg', 'Pasillo Quinta Etapa', 'Escazú'],
    ['i', 'nm26-plaza-siman-render-1-1536x862.jpg', 'Plaza Siman', 'Escazú'],
    ['v', 'nm26-fachada-esc-multiplaza.mp4', 'Fachada Multiplaza', 'Escazú', 'nm26-fachada-esc-multiplaza-1024x768.jpg'],
    ['i', 'nm26-plaza-honor-render-1536x1021.jpg', 'Plaza Honor', 'Escazú'],
    ['v', 'nm26-fachada-curri-principal.mp4', 'Fachada principal', 'Curridabat', 'nm26-fachada-curri-principal-1024x509.jpg'],
    ['i', 'nm26-santo-katrin-render.jpg', 'Plaza Santo Katrin', 'Curridabat'],
    ['i', 'nm26-equiz-vertigo-cascabeles-1536x864.jpg', 'Pasillo Equiz – Vértigo', 'Curridabat'],
    ['i', 'nm26-plaza-reebok-render-1536x1174.jpg', 'Plaza Reebok', 'Curridabat'],
    ['v', 'nm26-fachada-curri-entrada.mp4', 'Entrada techada', 'Curridabat', 'nm26-fachada-curri-entrada-1024x768.jpg']
  ];
  // Movimientos de cámara para los renders: acercar, alejar y desplazar
  var CAM = [[1.03, 1.16, '1.5%', '-1.5%', '0', '-1%'], [1.17, 1.04, '0', '0', '-2%', '1%'],
             [1.06, 1.17, '-2%', '2%', '0', '0'], [1.04, 1.18, '0', '0', '2%', '-2%']];
  var IMG = 6500, VMIN = 5000, VMAX = 12000, FIRST = 32000;
  var I = {
    play: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>',
    pause: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 5h3.5v14H7zM13.5 5H17v14h-3.5z"/></svg>',
    prev: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6h2v12H6zM9.5 12l8.5 6V6z"/></svg>',
    next: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M16 6h2v12h-2zM14.5 12L6 6v12z"/></svg>',
    on: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 9v6h4l5 4V5L8 9zm12.5 3A4.5 4.5 0 0 0 14 8v8a4.5 4.5 0 0 0 2.5-4zM14 3.2v2.1a7 7 0 0 1 0 13.4v2.1a9 9 0 0 0 0-17.6z"/></svg>',
    off: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 9v6h4l5 4V5L8 9zm16.6 3 2.1-2.1-1.4-1.4-2.1 2.1-2.1-2.1-1.4 1.4 2.1 2.1-2.1 2.1 1.4 1.4 2.1-2.1 2.1 2.1 1.4-1.4z"/></svg>',
    full: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 4h6v2H6v4H4zm10 0h6v6h-2V6h-4zM4 14h2v4h4v2H4zm14 0h2v6h-6v-2h4z"/></svg>',
    exit: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 4h2v6H4V8h4zm6 0h2v4h4v2h-6zM4 14h6v6H8v-4H4zm10 0h6v2h-4v4h-2z"/></svg>'
  };

  function go() {
    var reel = d.querySelector('.nm-reel'), cap = d.querySelector('.nm-reel-cap'), hero = d.querySelector('.nm-hero');
    if (!reel || !cap || !hero) return;
    var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;

    reel.innerHTML = S.map(function (s, k) {
      var c = s[0] === 'v' ? [1, 1.06, '0', '0', '0', '0'] : CAM[k % CAM.length];
      return '<div class="sc" style="--s0:' + c[0] + ';--s1:' + c[1] + ';--x0:' + c[2] + ';--x1:' + c[3] + ';--y0:' + c[4] + ';--y1:' + c[5] + '">' +
        (s[0] === 'v' ? '<video muted loop playsinline preload="none" data-src="' + U + s[1] + '" poster="' + U + s[4] + '"></video>'
                      : '<img alt="" decoding="async" data-src="' + U + s[1] + '">') + '</div>';
    }).join('') + '<div class="sheen"></div>';

    hero.appendChild(cap);   // fuera de la capa del fondo, para que quede sobre el contenido y reciba clics
    cap.removeAttribute('aria-hidden');
    cap.className = 'nm-reel-cap nm-player';
    cap.setAttribute('role', 'group');
    cap.setAttribute('aria-label', 'Recorrido en video por la Navidad de Multiplaza');
    cap.innerHTML = '<span class="k">Recorrido · <span class="n"></span></span><span class="t" aria-live="polite"></span>' +
      '<div class="nm-segs">' + S.map(function (s) {
        return '<button type="button" aria-label="' + s[2] + ' · ' + s[3] + '"><i><b></b></i></button>'; }).join('') + '</div>' +
      '<div class="nm-ctl"><button type="button" class="pv" aria-label="Escena anterior">' + I.prev + '</button>' +
      '<button type="button" class="pp" aria-label="Pausar">' + I.pause + '</button>' +
      '<button type="button" class="nx" aria-label="Escena siguiente">' + I.next + '</button>' +
      '<button type="button" class="snd" aria-label="Activar sonido">' + I.off + '</button>' +
      '<button type="button" class="fs" aria-label="Ver en pantalla completa">' + I.full + '<span>Pantalla completa</span></button></div>';

    var sc = [].slice.call(reel.querySelectorAll('.sc')), segs = [].slice.call(cap.querySelectorAll('.nm-segs button')),
      tEl = cap.querySelector('.t'), nEl = cap.querySelector('.n'), pp = cap.querySelector('.pp'),
      snd = cap.querySelector('.snd'), fs = cap.querySelector('.fs');
    var i = -1, t0 = 0, elapsed = 0, dur = IMG, paused = false, visible = true, muted = true;

    function pad(n) { return (n < 10 ? '0' : '') + n; }
    function vid(k) { return sc[k] ? sc[k].querySelector('video') : null; }
    function bar(k, f) { segs[k].querySelector('b').style.transform = 'scaleX(' + f + ')'; }
    function play(v) { var p = v.play(); if (p && p.catch) p.catch(function () {}); }
    function load(k) {
      var m = sc[k] && sc[k].querySelector('[data-src]');
      if (m) { m.src = m.getAttribute('data-src'); m.removeAttribute('data-src'); }
    }
    function show(k) {
      var prev = sc[i];
      i = (k + sc.length) % sc.length;
      var s = sc[i], v = vid(i), cap0 = i === 0 ? FIRST : VMAX;
      load(i); load((i + 1) % sc.length);
      dur = v ? cap0 : IMG;
      if (v) {
        v.muted = muted;
        try { v.currentTime = 0; } catch (e) {}
        var fit = function () { if (v.duration && isFinite(v.duration)) dur = Math.max(VMIN, Math.min(v.duration * 1000, cap0)); };
        if (v.readyState >= 1) fit(); else v.addEventListener('loadedmetadata', fit, { once: true });
        if (!paused && visible) play(v);
      }
      s.style.setProperty('--dur', (dur + 2000) / 1000 + 's');
      s.classList.remove('run'); void s.offsetWidth; s.classList.add('on');
      if (!reduce) s.classList.add('run');
      if (prev && prev !== s) {
        prev.classList.remove('on');
        setTimeout(function () {
          if (prev.classList.contains('on')) return;
          prev.classList.remove('run'); var pv = prev.querySelector('video'); if (pv) pv.pause();
        }, 1900);
      }
      tEl.style.opacity = 0;
      setTimeout(function () { tEl.innerHTML = S[i][2] + ' <i>· ' + S[i][3] + '</i>'; tEl.style.opacity = 1; }, 300);
      nEl.textContent = pad(i + 1) + ' / ' + pad(S.length);
      segs.forEach(function (b, j) {
        bar(j, j < i ? 1 : 0); b.classList.toggle('on', j === i);
        if (j === i) b.setAttribute('aria-current', 'step'); else b.removeAttribute('aria-current');
      });
      elapsed = 0; t0 = performance.now();
    }
    function tick(now) {
      requestAnimationFrame(tick);
      if (paused || !visible || d.hidden) { t0 = now - elapsed; return; }
      elapsed = now - t0;
      var f = Math.min(1, elapsed / dur);
      bar(i, f);
      if (f >= 1) show(i + 1);
    }
    function setPaused(p) {
      paused = p;
      var v = vid(i); if (v) { if (p) v.pause(); else if (visible) play(v); }
      reel.classList.toggle('paused', p);
      pp.innerHTML = p ? I.play : I.pause;
      pp.setAttribute('aria-label', p ? 'Reproducir' : 'Pausar');
    }
    function immersive(on) {
      root.classList.toggle('nm-imm', on);
      fs.innerHTML = (on ? I.exit : I.full) + '<span>' + (on ? 'Salir' : 'Pantalla completa') + '</span>';
      fs.setAttribute('aria-label', on ? 'Salir de pantalla completa' : 'Ver en pantalla completa');
      if (on && paused) setPaused(false);
    }

    pp.addEventListener('click', function () { setPaused(!paused); });
    cap.querySelector('.pv').addEventListener('click', function () { show(i - 1); });
    cap.querySelector('.nx').addEventListener('click', function () { show(i + 1); });
    segs.forEach(function (b, j) { b.addEventListener('click', function () { show(j); }); });
    snd.addEventListener('click', function () {
      muted = !muted; var v = vid(i); if (v) v.muted = muted;
      snd.innerHTML = muted ? I.off : I.on;
      snd.setAttribute('aria-label', muted ? 'Activar sonido' : 'Silenciar');
    });
    fs.addEventListener('click', function () {
      var on = !root.classList.contains('nm-imm');
      if (on) {
        if (hero.requestFullscreen) hero.requestFullscreen().catch(function () {});
        else window.scrollTo({ top: hero.getBoundingClientRect().top + window.pageYOffset });
        immersive(true);
      } else {
        if (d.fullscreenElement && d.exitFullscreen) d.exitFullscreen();
        immersive(false);
      }
    });
    d.addEventListener('fullscreenchange', function () {
      if (!d.fullscreenElement && root.classList.contains('nm-imm')) immersive(false);
    });
    d.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && root.classList.contains('nm-imm') && !d.fullscreenElement) immersive(false);
    });
    if ('IntersectionObserver' in window) new IntersectionObserver(function (es) {
      visible = es[0].isIntersecting;
      var v = vid(i); if (v) { if (visible && !paused) play(v); else v.pause(); }
    }).observe(hero);

    show(0);
    setPaused(!!reduce);
    requestAnimationFrame(tick);
  }
  if (d.readyState === 'loading') d.addEventListener('DOMContentLoaded', go); else go();
})();
