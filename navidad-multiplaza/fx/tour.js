/* Recorrido guiado: cada clic (o →, espacio, Enter) avanza a la siguiente diapositiva con su animación. */
(function () {
  var root = document.documentElement;
  if (document.body && document.body.classList.contains('elementor-editor-active')) return;
  root.classList.add('nm-js');
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;

  function init() {
    var slides = [].slice.call(document.querySelectorAll('.nm-slide'));
    if (!slides.length) return;

    // Elementos que aparecen en cascada dentro de cada diapositiva.
    slides.forEach(function (s) {
      var items = [].slice.call(s.querySelectorAll('.elementor-widget, .nm-card')).filter(function (el) {
        if (el.classList.contains('nm-fx')) return false;
        var p = el.parentElement.closest('.nm-card');
        return !p || !s.contains(p);
      });
      items.forEach(function (el, i) { el.classList.add('nm-rv'); el.style.transitionDelay = Math.min(i * 90, 900) + 'ms'; });
    });

    // Interfaz: barra de progreso, marca, puntos, contador y botón siguiente.
    var ui = document.createElement('div');
    ui.className = 'nm-tour';
    ui.innerHTML = '<div class="nm-bar"><i></i></div><div class="nm-brand"><b>Multiplaza</b>Navidad 2026</div><nav class="nm-dots" aria-label="Diapositivas"></nav>' +
      '<div class="nm-hint">Haz clic para comenzar el recorrido</div>' +
      '<div class="nm-foot"><div class="nm-count" aria-live="polite"></div><button class="nm-next" type="button"><span>Siguiente</span><i aria-hidden="true">→</i></button></div>';
    document.body.appendChild(ui);
    var bar = ui.querySelector('.nm-bar i'), dots = ui.querySelector('.nm-dots'), count = ui.querySelector('.nm-count'),
      next = ui.querySelector('.nm-next'), label = next.querySelector('span'), hint = ui.querySelector('.nm-hint');
    slides.forEach(function (s, i) {
      var b = document.createElement('button'), t = titleOf(i);
      b.type = 'button'; b.setAttribute('aria-label', t); b.innerHTML = '<span>' + t + '</span>';
      b.addEventListener('click', function (e) { e.stopPropagation(); go(i); });
      dots.appendChild(b);
    });
    var cur = 0, started = false;

    function titleOf(i) {
      var s = slides[i]; if (!s) return '';
      var e = s.querySelector('.nm-eyebrow .elementor-heading-title') || s.querySelector('.elementor-heading-title');
      return s.getAttribute('data-nm-title') || (e ? e.textContent.replace(/^[\d\s\u00a0]+/, '').trim() : 'Diapositiva ' + (i + 1));
    }
    function pad(n) { return (n < 10 ? '0' : '') + n; }
    function paint(i) {
      cur = i;
      [].forEach.call(dots.children, function (d, k) { d.classList.toggle('on', k === i); });
      bar.style.width = ((i + 1) / slides.length * 100) + '%';
      count.innerHTML = '<b>' + pad(i + 1) + '</b>/ ' + pad(slides.length);
      var last = i >= slides.length - 1;
      label.textContent = last ? 'Volver al inicio' : (i === 0 ? 'Iniciar recorrido' : titleOf(i + 1));
      next.classList.toggle('back', last);
      next.style.visibility = i === 0 ? 'hidden' : '';
    }
    function go(i) {
      i = Math.max(0, Math.min(slides.length - 1, i));
      if (i > 0 && !started) { started = true; hint.classList.add('off'); }
      var top = slides[i].getBoundingClientRect().top + window.pageYOffset;
      window.scrollTo({ top: top, behavior: reduce ? 'auto' : 'smooth' });
      paint(i);
    }
    function forward() { go(cur >= slides.length - 1 ? 0 : cur + 1); }

    // Diapositiva activa según lo que se ve en pantalla.
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (e.isIntersecting) e.target.classList.add('is-on');
        if (e.isIntersecting && e.intersectionRatio >= .5) paint(slides.indexOf(e.target));
      });
    }, { threshold: [.15, .5] });
    slides.forEach(function (s) { io.observe(s); });
    slides[0].classList.add('is-on');
    addEventListener('scroll', function () { if (window.pageYOffset > 80 && !started) { started = true; hint.classList.add('off'); } }, { passive: true });

    next.addEventListener('click', function (e) { e.stopPropagation(); forward(); });
    document.addEventListener('click', function (e) {
      if (e.defaultPrevented || e.button !== 0) return;
      if (e.target.closest('a,button,input,textarea,select,label,video,[contenteditable],.nm-tour')) return;
      if (String(window.getSelection && window.getSelection()).length) return;
      forward();
    });
    document.addEventListener('keydown', function (e) {
      if (e.target.closest && e.target.closest('input,textarea,select,[contenteditable]')) return;
      var k = e.key;
      if (k === 'ArrowRight' || k === 'ArrowDown' || k === 'PageDown' || k === ' ' || k === 'Enter') { if (k === 'Enter' && e.target.closest('a,button')) return; e.preventDefault(); forward(); }
      else if (k === 'ArrowLeft' || k === 'ArrowUp' || k === 'PageUp') { e.preventDefault(); go(cur - 1); }
      else if (k === 'Home') { e.preventDefault(); go(0); }
      else if (k === 'End') { e.preventDefault(); go(slides.length - 1); }
    });
    paint(0);
  }

  // Nieve y destellos dorados en la portada.
  function snow() {
    if (reduce) return;
    var c = document.querySelector('.nm-snow'); if (!c) return;
    var x = c.getContext('2d'), w, h, d = Math.min(window.devicePixelRatio || 1, 2), f = [];
    function size() { w = c.clientWidth; h = c.clientHeight; c.width = w * d; c.height = h * d; x.setTransform(d, 0, 0, d, 0, 0); }
    size(); addEventListener('resize', size);
    var n = Math.round(Math.min(120, w / 11));
    for (var i = 0; i < n; i++) f.push({ x: Math.random() * w, y: Math.random() * h, r: Math.random() * 2.2 + .6, s: Math.random() * .5 + .25,
      o: Math.random() * 6.28, g: Math.random() < .25 });
    var on = true;
    new IntersectionObserver(function (es) { on = es[0].isIntersecting; if (on) requestAnimationFrame(tick); }).observe(c);
    function tick(t) {
      if (!on || document.hidden) return;
      x.clearRect(0, 0, w, h);
      for (var i = 0; i < f.length; i++) { var p = f[i];
        p.y += p.s; p.x += Math.sin(t / 1800 + p.o) * .35; if (p.y > h + 5) { p.y = -5; p.x = Math.random() * w; }
        var a = p.g ? .55 + .45 * Math.sin(t / 400 + p.o) : .75;
        x.beginPath(); x.arc(p.x, p.y, p.g ? p.r * .9 : p.r, 0, 6.283);
        x.fillStyle = p.g ? 'rgba(235,217,174,' + a + ')' : 'rgba(255,255,255,' + a * .8 + ')';
        x.shadowBlur = p.g ? 8 : 0; x.shadowColor = 'rgba(235,217,174,.9)'; x.fill(); }
      requestAnimationFrame(tick);
    }
    document.addEventListener('visibilitychange', function () { if (!document.hidden) requestAnimationFrame(tick); });
  }

  function start() { init(); snow(); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start); else start();
})();
