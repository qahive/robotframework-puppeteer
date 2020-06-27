import time
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

        | &{options} =   | create dictionary                             | headless=${False}  |
        | `Open browser` | https://www.w3schools.com/html/html_forms.asp | options=${options} |

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
    def get_title(self):
        """Get page title"""
        async def get_title_async():
            return await self.ctx.get_current_page().title()
        return self.loop.run_until_complete(get_title_async())

    @keyword
    def get_location(self):
        """Get page location"""
        return self.ctx.get_current_page().url

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

    @keyword
    def wait_for_new_window_open(self, timeout=5):
        """
        Waits until new page or tab opens.

        Example:

        | Run Async Keywords | Click Element              | id:view_conditions          | AND  |
        | ...                | `Wait For New Window Open` |                             |      |
        """
        async def wait_for_new_page_open_async():
            pages = await self.ctx.get_browser().pages()
            await pages[-1].title() # workaround for force pages re-cache
            pre_page_len = len(pages)
            timer = 0
            while timer < timeout:
                pages = await self.ctx.get_browser().pages()
                await pages[-1].title()  # workaround for force pages re-cache
                page_len = len(pages)
                if page_len > pre_page_len:
                    return
                timer += 1
                time.sleep(1)
            raise Exception('No new page has been open. pre: '+str(pre_page_len)+' current: '+str(page_len))
        self.loop.run_until_complete(wait_for_new_page_open_async())

    @keyword
    def switch_window(self, locator='MAIN'):
        """Switches to tabs matching locator
        locator support options NEW, MAIN and query using name, title and url
            - NEW: latest opened window
            - MAIN: main window
            - title="QAHive": window title
            - url="https://qahive.com": url
        """
        async def switch_window_async():
            pages = await self.ctx.get_browser().pages()
            if locator == 'MAIN':
                return self.ctx.set_current_page(pages[0])
            elif locator == 'NEW':
                return self.ctx.set_current_page(pages[-1])
            elif 'title=' in locator:
                title = locator.replace('title=', '')
                for page in pages:
                    if page.title() == title:
                        return self.ctx.set_current_page(page)
            elif 'url=' in locator:
                url = locator.replace('url=', '')
                for page in pages:
                    if page.url() == url:
                        return self.ctx.set_current_page(page)
            else:
                raise Exception('Sorry Switch window support only NEW, MAIN, title and url')

            raise Exception('Can\'t find specify page locator.')
        self.loop.run_until_complete(switch_window_async())

