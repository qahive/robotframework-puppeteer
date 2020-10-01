from PuppeteerLibrary.ikeywords.ibrowsermanagement import iBrowserManagement
from playwright import sync_playwright

class PlaywrightBrowserManagement(iBrowserManagement):

  async def open_browser(self, url, browser="chrome", alias=None, options=None):
    playwright = sync_playwright().start()
    web_browser = playwright.webkit.launch()
    page = web_browser.newPage()
    await page.goto("http://whatsmyuseragent.org/")

