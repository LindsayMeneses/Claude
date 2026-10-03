(function () {
var root = document.documentElement;
if (document.body && document.body.classList.contains('elementor-editor-active')) return;
var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
if (!('IntersectionObserver' in window)) return;
if (!reduce) root.classList.add('nm-js');
function init() {
var slides = [].slice.call(document.querySelectorAll('.nm-slide'));
if (!slides.length) return;
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


function pad(n) { return (n < 10 ? '0' : '') + n; }


function media() {
var vs = [].slice.call(document.querySelectorAll('.elementor-widget-video video, .nm-vid video'));
if (!vs.length || !('IntersectionObserver' in window)) return;
vs.forEach(function (v) { v.removeAttribute('autoplay'); v.preload = 'metadata'; v.muted = true; v.loop = true; v.setAttribute('playsinline', ''); try { v.pause(); } catch (e) {} });
var io = new IntersectionObserver(function (es) {
es.forEach(function (e) { var v = e.target;
if (e.isIntersecting) { if (!reduce) { var p = v.play(); if (p && p.catch) p.catch(function () {}); } }
else v.pause(); });
}, { rootMargin: '160px 0px', threshold: .15 });
vs.forEach(function (v) { io.observe(v); });
}
function compare() {
[].forEach.call(document.querySelectorAll('.nm-cmp'), function (c) {
var inp = c.querySelector('input'); if (!inp) return;
function set(v) { c.style.setProperty('--p', v + '%'); }
inp.addEventListener('input', function () { c.setAttribute('data-touched', '1'); set(inp.value); });
inp.addEventListener('keydown', function (e) { e.stopPropagation(); });
set(inp.value);
if (reduce) return;
var io = new IntersectionObserver(function (es) {
if (!es[0].isIntersecting) return; io.disconnect();
var t0 = null;
function step(t) {
if (c.getAttribute('data-touched')) return;
if (!t0) t0 = t; var k = (t - t0) / 2400;
if (k >= 1) { set(50); inp.value = 50; return; }
var v = 50 + Math.sin(k * Math.PI * 2) * 24; set(v.toFixed(1)); inp.value = v; requestAnimationFrame(step);
}
setTimeout(function () { requestAnimationFrame(step); }, 700);
}, { threshold: .55 });
io.observe(c);
});
}

function start() { init(); media(); compare(); }
if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start); else start();
})();