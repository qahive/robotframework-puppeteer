'use strict';
const puppeteer = require('puppeteer');

var lib = module.exports;

lib.OpenBrowser = async function () {
  lib.browser = await puppeteer.launch({headless: false});
  return lib.browser;
};

lib.Goto = async function () {
  const page = await lib.browser.newPage();
  await page.goto('https://example.com');
};

(async () => {
  await lib.OpenBrowser();
  await lib.Goto();
})();