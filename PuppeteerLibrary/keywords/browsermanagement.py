from PuppeteerLibrary.keywords.ibrowsermanagement_async import iBrowserManagementAsync
import re
import sys
from robot.utils import timestr_to_secs
from pyppeteer import launch
from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.base.robotlibcore import keyword
from PuppeteerLibrary.keywords.browsermanagement_async import BrowserManagementKeywordsAsync

class BrowserManagementKeywords(LibraryComponent):

    def __init__(self, ctx):
        super().__init__(ctx)
        self.async_func = BrowserManagementKeywordsAsync(self.ctx)

    def get_async_keyword_group(self) -> iBrowserManagementAsync:
        return self.ctx.get_current_library_context().get_async_keyword_group(type(self).__name__)

    @keyword
    def open_browser(self, url, browser="chrome", alias=None, options=None):
        """Opens a new browser instance to the specific ``url``.

        The ``browser`` argument specifies which browser to use.

        |    = Browser =         |    = Name(s) =   |
        | Google Chrome          | chrome           |
        | Webkit (Safari engine) | webkit           |


        The ``options`` argument as a dictionary

        |    = Property =    |        = Value =       |
        | headless           | default True           |
        | width              | default 1366           |
        | height             | default 768            |


        Example:

        | &{options} =   | create dictionary                             | headless=${False}  |
        | `Open browser` | https://www.w3schools.com/html/html_forms.asp | options=${options} |

        """
        library_context = self.ctx.create_library_context(alias, browser)
        self.loop.run_until_complete(library_context.start_server(options))
        self.loop.run_until_complete(library_context.create_new_page(options))
        self.loop.run_until_complete(self.get_async_keyword_group().go_to(url))

    @keyword
    def close_browser(self, alias=None):
        """Closes the current browser
        """
        library_context = self.ctx.get_current_library_context()
        if alias is not None:
            library_context = self.ctx.get_library_context_by_name(alias)
        self.loop.run_until_complete(library_context.close_browser_context())

    @keyword
    def close_all_browser(self):
        """Close all browser
        """
        library_contexts =  self.ctx.get_all_library_context()
        for library_context in library_contexts:
            self.loop.run_until_complete(library_context.close_browser_context())

    @keyword
    def close_puppeteer(self):
        library_contexts =  self.ctx.get_all_library_context()
        for library_context in library_contexts:
            self.loop.run_until_complete(library_context.stop_server())

    @keyword
    def maximize_browser_window(self, width=1366, height=768):
        """Maximize view port not actual browser and set default size to 1366 x 768
        """
        self.info(('width: ' + str(width) + '\n' +
                   'height: ' + str(height)))
        self.loop.run_until_complete(self.get_async_keyword_group().maximize_browser_window(width, height))
        '''
        async def maximize_browser_window_async():
            await self.ctx.get_current_page().setViewport({
                'width': width,
                'height': height
            })
        self.loop.run_until_complete(maximize_browser_window_async())
        '''

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
        self.loop.run_until_complete(self.get_async_keyword_group().go_back())

    @keyword
    def go_to(self, url):
        """Navigates the current page to the ``url``"""
        self.loop.run_until_complete(self.get_async_keyword_group().go_to(url))

    @keyword
    def reload_page(self):
        """Reload the current page"""
        self.loop.run_until_complete(self.get_async_keyword_group().reload_page())
        # async def reload_page_async():
        #     await self.ctx.get_current_page().reload()
        # self.loop.run_until_complete(reload_page_async())

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
    def get_window_count(self):
        """ Get windows count
        """
        pass
        # return  self.loop.run_until_complete(self.async_func.get_window_count_async())

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
            - title="QAHive": window title. Page title will have have error if new tab have auto redirection
            - url="https://qahive.com": url support regex Example: url=.*qahive.com
        """
        async def switch_window_async():
            pages = await self.ctx.get_browser().pages()
            if locator == 'MAIN':
                page = pages[0]
                await page.bringToFront()
                return self.ctx.set_current_page(page)

            elif locator == 'NEW':
                page = pages[-1]
                await page.bringToFront()
                return self.ctx.set_current_page(page)

            elif 'title=' in locator:
                title = locator.replace('title=', '')
                for page in pages:
                    page_title = await page.title()
                    if page_title == title:
                        await page.bringToFront()
                        return self.ctx.set_current_page(page)
                    self.info('Title mismatch: ' + page_title)

            elif 'url=' in locator:
                url = locator.replace('url=', '')
                for page in pages:
                    if re.match(url, page.url):
                        await page.bringToFront()
                        return self.ctx.set_current_page(page)
                    self.info('Url mismatch: ' + page.url)
            else:
                raise Exception('Sorry Switch window support only NEW, MAIN, title and url')
            raise Exception('Can\'t find specify page locator.')

        return self.loop.run_until_complete(switch_window_async())

    @keyword
    def switch_browser(self, alias):
        """Switch browser context based on alias name
        """
        return self.loop.run_until_complete(self.ctx.set_current_context(alias))

    @keyword
    def enable_emulate_mode(self, emulate_name):
        """Emulate specific mobile or tablet

        The ``emulate_name`` argument specifies which emulator to use.

        | = Example Options = |
        | iPhone X            |
        | Pixel 2             |

        More emulate_name please visit [device_descriptors.py](https://github.com/qahive/robotframework-puppeteer/tree/master/PuppeteerLibrary/utils/device_descriptors.py)

        """
        return self.loop.run_until_complete(self.async_func.enable_emulate_mode_async(emulate_name))

    @keyword
    def select_frame(self, selenium_locator):
        return self.loop.run_until_complete(self.async_func.select_frame_async(selenium_locator))

    @keyword
    def unselect_frame(self):
        self.ctx.clear_current_iframe()
