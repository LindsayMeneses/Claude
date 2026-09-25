/* Recorrido guiado: botón «Siguiente», puntos laterales y teclado (→ ← espacio). Entradas suaves al aparecer cada elemento. */
(function () {
  var root = document.documentElement;
  if (document.body && document.body.classList.contains('elementor-editor-active')) return;
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!('IntersectionObserver' in window)) return;
  if (!reduce) root.classList.add('nm-js');

  function init() {
    var slides = [].slice.call(document.querySelectorAll('.nm-slide'));
    if (!slides.length) return;

    // Entradas: cada elemento aparece cuando entra en pantalla (nunca queda oculto en diapositivas largas).
    if (!reduce) {
      var items = [];
      slides.forEach(function (s) {
        var k = 0;
        [].slice.call(s.querySelectorAll('.elementor-widget, .nm-card')).forEach(function (el) {
          if (el.classList.contains('nm-fx')) return;
          var p = el.parentElement.closest('.nm-card');
          if (p && s.contains(p)) return;
          el.classList.add('nm-rv'); el.style.transitionDelay = Math.min(k++ % 6 * 70, 350) + 'ms'; items.push(el);
        });
      });
      var rv = new IntersectionObserver(function (es) {
        es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('is-in'); rv.unobserve(e.target); } });
      }, { rootMargin: '0px 0px -6% 0px', threshold: 0 });
      items.forEach(function (el) { rv.observe(el); });
      setTimeout(function () { items.forEach(function (el) { if (el.getBoundingClientRect().top < innerHeight) el.classList.add('is-in'); }); }, 60);
    }

    // Interfaz: barra de progreso, marca, puntos, contador y botón siguiente.
    var ui = document.createElement('div');
    ui.className = 'nm-tour';
    ui.innerHTML = '<div class="nm-bar"><i></i></div><div class="nm-brand"><b>Multiplaza</b><i></i>Navidad 2026</div><nav class="nm-dots" aria-label="Secciones"></nav>' +
      '<div class="nm-foot"><div class="nm-count" aria-live="polite"></div><button class="nm-next" type="button"><span>Siguiente</span><i aria-hidden="true">→</i></button></div>';
    document.body.appendChild(ui);
    var bar = ui.querySelector('.nm-bar i'), dots = ui.querySelector('.nm-dots'), count = ui.querySelector('.nm-count'),
      next = ui.querySelector('.nm-next'), label = next.querySelector('span');
    slides.forEach(function (s, i) {
      var b = document.createElement('button'), t = titleOf(i);
      b.type = 'button'; b.setAttribute('aria-label', t); b.innerHTML = '<span>' + t + '</span>';
      b.addEventListener('click', function () { go(i); });
      dots.appendChild(b);
    });
    var cur = -1;

    function titleOf(i) {
      var s = slides[i]; if (!s) return '';
      var e = s.querySelector('.nm-eyebrow .elementor-heading-title') || s.querySelector('.elementor-heading-title');
      return s.getAttribute('data-nm-title') || (e ? e.textContent.replace(/^[\d\s]+/, '').trim() : 'Sección ' + (i + 1));
    }
    function pad(n) { return (n < 10 ? '0' : '') + n; }
    function paint(i) {
      if (i === cur) return;
      cur = i;
      [].forEach.call(dots.children, function (d, k) { d.classList.toggle('on', k === i); });
      bar.style.width = ((i + 1) / slides.length * 100) + '%';
      count.innerHTML = '<b>' + pad(i + 1) + '</b>/ ' + pad(slides.length);
      var last = i >= slides.length - 1;
      label.textContent = last ? 'Volver al inicio' : (i === 0 ? 'Iniciar recorrido' : titleOf(i + 1));
      next.classList.toggle('back', last);
    }
    function go(i) {
      i = Math.max(0, Math.min(slides.length - 1, i));
      var top = slides[i].getBoundingClientRect().top + window.pageYOffset;
      window.scrollTo({ top: top, behavior: reduce ? 'auto' : 'smooth' });
      paint(i);
    }
    // Sección activa: la que ocupa el centro de la pantalla.
    function sync() {
      var mid = innerHeight / 2, best = 0;
      for (var i = 0; i < slides.length; i++) if (slides[i].getBoundingClientRect().top <= mid) best = i;
      paint(best);
    }
    var ticking = false;
    addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(function () { ticking = false; sync(); }); } }, { passive: true });
    addEventListener('resize', sync);

    next.addEventListener('click', function () { go(cur >= slides.length - 1 ? 0 : cur + 1); });
    document.addEventListener('keydown', function (e) {
      if (e.altKey || e.ctrlKey || e.metaKey) return;
      if (e.target.closest && e.target.closest('input,textarea,select,[contenteditable],a,button')) return;
      var k = e.key;
      if (k === 'ArrowRight' || k === 'PageDown' || k === ' ') { e.preventDefault(); go(cur + 1); }
      else if (k === 'ArrowLeft' || k === 'PageUp') { e.preventDefault(); go(cur - 1); }
    });
    sync();
  }

  // Nieve suave en la portada (se detiene fuera de pantalla).
  function snow() {
    if (reduce) return;
    var c = document.querySelector('.nm-snow'); if (!c) return;
    var x = c.getContext('2d'), w, h, d = Math.min(window.devicePixelRatio || 1, 2), f = [];
    function size() { w = c.clientWidth; h = c.clientHeight; c.width = w * d; c.height = h * d; x.setTransform(d, 0, 0, d, 0, 0); }
    size(); addEventListener('resize', size);
    var n = Math.round(Math.min(70, w / 18));
    for (var i = 0; i < n; i++) f.push({ x: Math.random() * w, y: Math.random() * h, r: Math.random() * 1.6 + .5, s: Math.random() * .3 + .15,
      o: Math.random() * 6.28, g: Math.random() < .3 });
    var on = true;
    new IntersectionObserver(function (es) { on = es[0].isIntersecting; if (on) requestAnimationFrame(tick); }).observe(c);
    function tick(t) {
      if (!on || document.hidden) return;
      x.clearRect(0, 0, w, h);
      for (var i = 0; i < f.length; i++) { var p = f[i];
        p.y += p.s; p.x += Math.sin(t / 2600 + p.o) * .2; if (p.y > h + 5) { p.y = -5; p.x = Math.random() * w; }
        x.beginPath(); x.arc(p.x, p.y, p.r, 0, 6.283);
        x.fillStyle = p.g ? 'rgba(235,217,174,.55)' : 'rgba(255,255,255,.5)'; x.fill(); }
      requestAnimationFrame(tick);
    }
    document.addEventListener('visibilitychange', function () { if (!document.hidden) requestAnimationFrame(tick); });
  }

  // Destellos desenfocados (bokeh) que flotan muy despacio en la portada.
  function bokeh() {
    var b = document.querySelector('.nm-bokeh'); if (!b || reduce) return;
    var h = '';
    for (var i = 0; i < 14; i++) { var s = Math.round(40 + Math.random() * 130);
      h += '<span style="width:' + s + 'px;height:' + s + 'px;left:' + (Math.random() * 100).toFixed(1) + '%;top:' + (Math.random() * 100).toFixed(1) +
        '%;--o:' + (.18 + Math.random() * .32).toFixed(2) + ';--d:' + (14 + Math.random() * 16).toFixed(1) + 's;--dl:-' + (Math.random() * 20).toFixed(1) + 's"></span>'; }
    b.innerHTML = h;
  }

  function start() { init(); snow(); bokeh(); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start); else start();
})();
