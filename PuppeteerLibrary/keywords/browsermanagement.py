from pyppeteer import launch
from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.base.robotlibcore import keyword


class BrowserManagementKeywords(LibraryComponent):

    @keyword
    def open_browser(self, url, browser="chrome", alias=None, options=None):
        """Opens a new browser instance to the specific ``url``.

        The ``browser`` argument specifies which browser to use.

        |    = Browser =    |        = Name(s) =     |
        | Google Chrome     | chrome                 |


        The ``options`` argument as a dictionary

        |    = Property =    |        = Value =       |
        | headless           | default True           |
        | width              | default 1366           |
        | height             | default 768            |


        Example:

        | &{options} = | create dictionary                             | headless=${False}  |
        | Open browser | https://www.w3schools.com/html/html_forms.asp | options=${options} |

        """
        async def open_browser_async():
            default_options = {
                'headless': True,
                'width': 1366,
                'height': 768
            }
            merged_options = None
            if options is None:
                merged_options = default_options
            else:
                merged_options = {**default_options, **options}
            self.ctx.browser = await launch(headless=merged_options['headless'], defaultViewport={
                'width': merged_options['width'],
                'height': merged_options['height']
            })
            self.ctx.current_page = await self.ctx.browser.newPage()
            await self.ctx.current_page.goto(url)
            await self.ctx.current_page.screenshot({'path': 'example.png'})
        self.loop.run_until_complete(open_browser_async())

    @keyword
    def close_browser(self):
        """Closes the current browser
        """
        async def close_browser_async():
            await self.ctx.browser.close()
        self.loop.run_until_complete(close_browser_async())

    @keyword
    def maximize_browser_window(self, width=1366, height=768):
        """Maximize view port not actual browser and set default size to 1366 x 768
        """
        async def maximize_browser_window_async():
            await self.ctx.get_current_page().setViewport({
                'width': width,
                'height': height
            })
        self.loop.run_until_complete(maximize_browser_window_async())

    @keyword
    def get_source(self):
        print('')

    @keyword
    def get_title(self):
        """Get page title"""
        async def get_title_async():
            return await self.ctx.get_current_page().title()
        return self.loop.run_until_complete(get_title_async())

    @keyword
    def get_location(self):
        print('')

    @keyword
    def go_back(self):
        """Simulate browser go back"""
        async def go_back_async():
            await self.ctx.get_current_page().goBack()
        self.loop.run_until_complete(go_back_async())

    @keyword
    def go_to(self, url):
        """Navigates the current page to the ``url``"""
        async def go_to_async():
            await self.ctx.get_current_page().goto(url)
        self.loop.run_until_complete(go_to_async())

    @keyword
    def reload_page(self):
        """Reload the current page"""
        async def reload_page_async():
            await self.ctx.get_current_page().reload()
        self.loop.run_until_complete(reload_page_async())
