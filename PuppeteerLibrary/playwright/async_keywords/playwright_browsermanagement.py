from PuppeteerLibrary.iasync_keywords import iBrowserManagementAsync
try:
    from playwright import async_playwright
except ImportError:
    print('import playwright error')

class PlaywrightBrowserManagement(iBrowserManagementAsync):

  async def start_server_async(self, browser, options: dict=None, **kwargs: any):
    playwright = await async_playwright().start()
    self.browser = await playwright.webkit.launch(headless=False)
    return self.browser

  async def open_browser_async(self, url, browser, alias=None, options=None):
    page = await self.browser.newPage()
    await page.goto(url)

    """
    iphone_11 = p.devices['iPhone 11 Pro']
    browser = p.webkit.launch(headless=False)
    context = browser.newContext(
        **iphone_11,
        locale='en-US',
        geolocation={ 'longitude': 12.492507, 'latitude': 41.889938 },
        permissions=['geolocation']
    )
    page = context.newPage()
    page.goto('https://maps.google.com')
    page.click('text="Your location"')
    page.screenshot(path='colosseum-iphone.png')
    browser.close()
    ---------------------------------------------------------------------
    playwright = await async_playwright().start()
    web_browser = await playwright.webkit.launch(headless=False)
    page = await web_browser.newPage()
    await page.goto("http://whatsmyuseragent.org/")
    """
    

  async def close_browser_async(self, alias=None):
    pass

  async def close_all_browser_async(self):
    pass
