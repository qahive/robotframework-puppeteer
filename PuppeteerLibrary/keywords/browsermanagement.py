import time
import sys
from robot.utils import timestr_to_secs
from pyppeteer import launch
from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.base.robotlibcore import keyword
from PuppeteerLibrary.keywords.browsermanagement_async import BrowserManagementKeywordsAsync


class BrowserManagementKeywords(LibraryComponent):

    def __init__(self, ctx):
        self.ctx = ctx
        self.async_func = BrowserManagementKeywordsAsync(self.ctx)

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
            if self.ctx.browser is None:
                default_args = []
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

                if 'win' not in sys.platform.lower():
                    default_args = ['--no-sandbox', '--disable-setuid-sandbox']

                self.info(('Open browser to ' + url + '\n' +
                            str(merged_options)))
                self.ctx.browser = await launch(
                    headless=merged_options['headless'],
                    defaultViewport={
                        'width': merged_options['width'],
                        'height': merged_options['height']
                    },
                    args=default_args)
            await self.ctx.create_context_async(alias)
            current_page = await self.ctx.create_page_async()
            await current_page.goto(url)
            await current_page.screenshot({'path': 'example.png'})
        self.loop.run_until_complete(open_browser_async())

    @keyword
    def close_browser(self, alias=None):
        """Closes the current browser
        """
        self.loop.run_until_complete(self.async_func.close_browser_async(alias))

    @keyword
    def close_all_browser(self):
        """Close all browser
        """
        self.loop.run_until_complete(self.async_func.close_all_browser_async())

    @keyword
    def close_puppeteer(self):
        self.loop.run_until_complete(self.async_func.close_puppeteer_async())

    @keyword
    def maximize_browser_window(self, width=1366, height=768):
        """Maximize view port not actual browser and set default size to 1366 x 768
        """
        self.info(('width: ' + str(width) + '\n' +
                   'height: ' + str(height)))
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
    def set_timeout(self, timeout):
        """Sets the timeout that is used by various keywords.
        The value can be given as a number that is considered to be seconds or as a human-readable string like 1 second.
        The previous value is returned and can be used to restore the original value later if needed.
        See the Timeout section above for more information.

        Example:

        | ${orig timeout} =	          | Set Timeout	     | 15 seconds |
        | Open page that loads slowly |	                 |            |
        | Set Timeout	              | ${orig timeout}	 |            |

        """
        orig_timeout = self.ctx.timeout
        self.ctx.timeout = timestr_to_secs(timeout)
        self.info('Original timeout is ' + str(orig_timeout) + ' seconds')
        return orig_timeout

    @keyword
    def wait_for_new_window_open(self, timeout=None):
        """
        Waits until new page or tab opens.

        Example:

        | Run Async Keywords | Click Element              | id:view_conditions          | AND  |
        | ...                | `Wait For New Window Open` |                             |      |
        """
        self.loop.run_until_complete(self.async_func.wait_for_new_window_open_async(timeout))

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

    @keyword
    def switch_browser(self, alias):
        """Switch browser context based on alias name
        """
        return self.loop.run_until_complete(self.ctx.set_current_context(alias))
