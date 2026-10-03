// Recorre la presentación con el botón «Siguiente» (como un visitante) y captura cada diapositiva.
// Uso: NODE_PATH=$(npm root -g) node preview-tour.js [ancho alto prefijo]
const { chromium } = require('playwright');
const path = require('path');
const [w, h, pre] = [+(process.argv[2] || 1440), +(process.argv[3] || 900), process.argv[4] || 'slide'];
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const p = await b.newPage({ viewport: { width: w, height: h } });
  await p.goto('file://' + path.resolve(__dirname, 'preview/index.html'), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(1800);
  const n = await p.evaluate(() => document.querySelectorAll('.nm-slide').length);
  for (let i = 0; i < n; i++) {
    const label = await p.textContent('.nm-next span');
    await p.screenshot({ path: path.join(__dirname, `preview/${pre}-${i + 1}.png`) });
    console.log(i + 1, '→ botón:', label);
    if (i < n - 1) { if (i === 0) await p.mouse.click(Math.round(w * .1), Math.round(h * .55)); else await p.click('.nm-next'); await p.waitForTimeout(2200); }
  }
  await b.close();
})();
