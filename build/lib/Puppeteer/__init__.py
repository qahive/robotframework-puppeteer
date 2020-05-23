from pyppeteer import launch
from Puppeteer.base.robotlibcore import keyword


__version__ = '0.0.1'


class Puppeteer:

    ROBOT_LISTENER_API_VERSION = 3

    # loop = asyncio.get_event_loop()
    browser = None
    current_page = None

    # @keyword
    def open_browser(self):
        # self.loop.run_until_complete(self.open_browser_async())
        print('open')

    # @keyword
    def close_browser(self):
        # self.loop.run_until_complete(self.close_browser_async())
        print('close')

    # async def open_browser_async(self):
    #     global browser, current_page
    #     browser = await launch(headless=False)
    #     current_page = await browser.newPage()
    #     await current_page.goto('http://example.com')
    #     await current_page.screenshot({'path': 'example.png'})
    #
    # async def close_browser_async(self):
    #     global browser
    #     await browser.close()
