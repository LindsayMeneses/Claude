// Capturas de preview/index.html (escritorio y celular) y un video corto de las animaciones.
// Uso: NODE_PATH=$(npm root -g) node preview-shots.js [--video]
const { chromium } = require('playwright');
const path = require('path');

const url = 'file://' + path.resolve(__dirname, 'preview/index.html');

async function scrollThrough(page, step = 500, pause = 120) {
  const total = await page.evaluate(() => document.body.scrollHeight);
  for (let y = 0; y <= total; y += step) {
    await page.evaluate((v) => window.scrollTo(0, v), y);
    await page.waitForTimeout(pause);
  }
}

(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  for (const [name, width, height] of [['escritorio', 1440, 900], ['celular', 390, 844]]) {
    const page = await browser.newPage({ viewport: { width, height } });
    await page.goto(url, { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    await scrollThrough(page);
    await page.waitForTimeout(1500); // que terminen las entradas
    await page.evaluate(() => window.scrollTo(0, 0));
    await page.screenshot({ path: path.join(__dirname, `preview/${name}.png`), fullPage: true });
    await page.close();
  }
  if (process.argv.includes('--video')) {
    const ctx = await browser.newContext({ viewport: { width: 1280, height: 720 },
      recordVideo: { dir: path.join(__dirname, 'preview/video'), size: { width: 1280, height: 720 } } });
    const page = await ctx.newPage();
    await page.goto(url, { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(4000); // portada: nieve y brillo
    await scrollThrough(page, 18, 25); // recorrido suave por la página
    await page.waitForTimeout(1000);
    await ctx.close();
  }
  await browser.close();
  console.log('ok capturas');
})();
