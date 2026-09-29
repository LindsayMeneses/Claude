/* lindsaymeneses.com — barra, menú hamburguesa (proyectos automáticos) y animaciones ligadas al scroll. */
(function () {
  var d = document, root = d.documentElement;
  if (d.body && d.body.classList.contains('elementor-editor-active')) return;
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  root.classList.add('lx-js'); if (reduce) root.classList.add('lx-reduce');
  var MAIL = 'contacto@lindsaymeneses.com', IN = 'https://www.linkedin.com/in/lindsay-meneses-cambronero-3b424420/';

  function esc(s) { var e = d.createElement('i'); e.textContent = s; return e.innerHTML; }

  // Barra y menú. La lista de proyectos se llena con las páginas hijas de «Proyectos» (data-hub).
  function shell() {
    var cfg = d.querySelector('.lx-shell'); if (!cfg || d.querySelector('.lx-bar')) return;
    var hub = cfg.getAttribute('data-hub'), home = cfg.getAttribute('data-home') || '/', hubUrl = cfg.getAttribute('data-hub-url') || '/proyectos/';
    var fallback = []; try { fallback = JSON.parse(cfg.getAttribute('data-projects') || '[]'); } catch (e) {}
    var bar = d.createElement('header'); bar.className = 'lx-bar';
    bar.innerHTML = '<a class="lx-logo" href="' + home + '">Lindsay <em>Meneses</em></a>' +
      '<button class="lx-burger" type="button" aria-expanded="false" aria-controls="lx-menu"><b class="lx-bt">Menú</b><span><i></i><i></i></span></button>';
    var nav = d.createElement('nav'); nav.id = 'lx-menu'; nav.className = 'lx-menu'; nav.setAttribute('aria-label', 'Menú principal');
    function item(p, i) { return '<li><a href="' + p.link + '" style="transition-delay:' + (120 + i * 60) + 'ms">' + p.title +
      (p.meta ? '<small>' + esc(p.meta) + '</small>' : '') + '</a></li>'; }
    function projects(list) { return list.map(function (p, i) { return item(p, i + 4); }).join('') +
      '<li><a href="' + hubUrl + '" style="transition-delay:' + (120 + (list.length + 4) * 60) + 'ms"><small>Ver todos los proyectos →</small></a></li>'; }
    nav.innerHTML = '<div class="lx-menu-in"><div><p class="lx-menu-k">Lindsay Meneses</p><ul class="lx-menu-main">' +
      [{ title: 'Inicio', link: home }, { title: 'Perfil', link: home + '#perfil' }, { title: 'Trayectoria', link: home + '#trayectoria' },
       { title: 'Contacto', link: home + '#contacto' }].map(item).join('') + '</ul></div>' +
      '<div><p class="lx-menu-k">Proyectos</p><ul class="lx-menu-proj">' + projects(fallback) + '</ul></div></div>' +
      '<div class="lx-menu-foot"><a href="mailto:' + MAIL + '">' + MAIL + '</a><a href="' + IN + '" target="_blank" rel="noopener">LinkedIn</a></div>';
    d.body.appendChild(nav); d.body.appendChild(bar);
    var btn = bar.querySelector('.lx-burger'), label = bar.querySelector('.lx-bt');
    function set(open) {
      root.classList.toggle('lx-open', open); root.classList.toggle('lx-lock', open);
      btn.setAttribute('aria-expanded', open); label.textContent = open ? 'Cerrar' : 'Menú';
      if (open) { var a = nav.querySelector('a'); if (a) setTimeout(function () { a.focus({ preventScroll: true }); }, 400); } else btn.focus({ preventScroll: true });
    }
    btn.addEventListener('click', function () { set(!root.classList.contains('lx-open')); });
    d.addEventListener('keydown', function (e) { if (e.key === 'Escape' && root.classList.contains('lx-open')) set(false); });
    nav.addEventListener('click', function (e) { if (e.target.closest('a')) set(false); });
    function mark() { var here = location.pathname.replace(/\/$/, ''); [].forEach.call(nav.querySelectorAll('a'), function (a) {
      if (a.pathname && a.pathname.replace(/\/$/, '') === here && !a.hash) a.setAttribute('aria-current', 'page'); }); }
    mark();
    if (hub && window.fetch) fetch('/wp-json/wp/v2/pages?parent=' + hub + '&per_page=30&orderby=menu_order&order=asc&_fields=title,link,excerpt')
      .then(function (r) { return r.ok ? r.json() : []; })
      .then(function (list) { if (!list.length) return;
        nav.querySelector('.lx-menu-proj').innerHTML = projects(list.map(function (p) { return { title: p.title.rendered, link: p.link }; })); mark(); })
      .catch(function () {});
    var solid = function () { bar.classList.toggle('solid', window.pageYOffset > 40); };
    addEventListener('scroll', solid, { passive: true }); solid();
  }

  // Texto que se ilumina palabra por palabra.
  function splitWords() {
    [].forEach.call(d.querySelectorAll('.lx-words'), function (w) {
      var el = w.querySelector('.elementor-heading-title') || w.querySelector('p') || w;
      if (el.getAttribute('data-split')) return;
      el.innerHTML = el.textContent.trim().split(/\s+/).map(function (t) { return '<span class="lx-w">' + esc(t) + '</span>'; }).join(' ');
      el.setAttribute('data-split', '1');
    });
  }

  // Motor: calcula el avance de cada sección fijada (--p), las palabras, el carrusel y la línea de tiempo.
  function engine() {
    var pins = [].slice.call(d.querySelectorAll('.lx-pin')), words = [].slice.call(d.querySelectorAll('.lx-words')),
      tls = [].slice.call(d.querySelectorAll('.lx-tl')), hp = [].slice.call(d.querySelectorAll('.lx-hpin'));
    var mobile = function () { return innerWidth < 768; };
    function sizeH() { hp.forEach(function (p) { var t = p.querySelector('.lx-track'); if (!t) return;
      if (mobile() || reduce) { p.style.height = ''; t.style.setProperty('--shift', '0px'); return; }
      var left = t.getBoundingClientRect().left + (+p.getAttribute('data-shift0') || 0), extra = Math.max(0, Math.round(t.scrollWidth + left * 2 - innerWidth)); p.setAttribute('data-extra', extra); p.style.height = (innerHeight + extra) + 'px'; }); }
    function upd() {
      var vh = innerHeight;
      pins.forEach(function (p) { var r = p.getBoundingClientRect(), tot = p.offsetHeight - vh;
        var v = tot > 0 ? Math.min(1, Math.max(0, -r.top / tot)) : 0; p.style.setProperty('--p', v.toFixed(4));
        if (p.classList.contains('lx-hpin')) { var t = p.querySelector('.lx-track'); if (t && !mobile()) { var sh = v * (+p.getAttribute('data-extra') || 0); p.setAttribute('data-shift0', sh.toFixed(1)); t.style.setProperty('--shift', sh.toFixed(1) + 'px'); } } });
      words.forEach(function (w) { var r = w.getBoundingClientRect(), s = w.querySelectorAll('.lx-w'), n = s.length;
        var v = (vh * .88 - r.top) / (vh * .55 + r.height * .5), k = Math.round(Math.min(1, Math.max(0, v)) * n);
        for (var i = 0; i < n; i++) s[i].classList.toggle('on', i < k); });
      tls.forEach(function (t) { var r = t.getBoundingClientRect(); var v = (vh * .8 - r.top) / (r.height || 1);
        t.style.setProperty('--tp', Math.min(1, Math.max(0, v)).toFixed(3)); });
    }
    var tick = false;
    function on() { if (!tick) { tick = true; requestAnimationFrame(function () { tick = false; upd(); }); } }
    if (!reduce) { addEventListener('scroll', on, { passive: true }); addEventListener('resize', function () { sizeH(); on(); }); }
    sizeH(); upd(); addEventListener('load', function () { sizeH(); upd(); });
  }

  // Entradas suaves de los elementos de secciones normales.
  function reveal() {
    if (reduce || !('IntersectionObserver' in window)) return;
    var els = [].slice.call(d.querySelectorAll('.lx-sec .elementor-widget, .lx-sec .lx-card'))
      .filter(function (el) { return !el.closest('.lx-pin') && !el.classList.contains('lx-shell-w') && !el.parentElement.closest('.lx-card'); });
    var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); } }); },
      { rootMargin: '0px 0px -8% 0px' });
    els.forEach(function (el, i) { el.classList.add('lx-rv'); el.style.transitionDelay = (i % 4) * 90 + 'ms'; io.observe(el); });
  }

  function start() { shell(); splitWords(); engine(); reveal(); }
  if (d.readyState === 'loading') d.addEventListener('DOMContentLoaded', start); else start();
})();
