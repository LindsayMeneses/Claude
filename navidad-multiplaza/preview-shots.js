// Capturas de preview/index.html en escritorio y celular: node preview-shots.js
const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const url = 'file://' + path.resolve(__dirname, 'preview/index.html');
  for (const [name, width, height] of [['escritorio', 1440, 900], ['celular', 390, 844]]) {
    const page = await browser.newPage({ viewport: { width, height }, deviceScaleFactor: 1 });
    await page.goto(url, { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    await page.screenshot({ path: path.join(__dirname, `preview/${name}.png`), fullPage: true });
    await page.close();
  }
  await browser.close();
  console.log('ok capturas');
})();
