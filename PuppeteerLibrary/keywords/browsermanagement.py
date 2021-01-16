from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.base.robotlibcore import keyword
from PuppeteerLibrary.ikeywords.ibrowsermanagement_async import iBrowserManagementAsync


class BrowserManagementKeywords(LibraryComponent):

    def __init__(self, ctx):
        super().__init__(ctx)

    def get_async_keyword_group(self) -> iBrowserManagementAsync:
        return self.ctx.get_current_library_context().get_async_keyword_group(type(self).__name__)

    @keyword
    def open_browser(self, url, browser="chrome", alias=None, options=None):
        """Opens a new browser instance to the specific ``url``.

        The ``browser`` argument specifies which browser to use.

        |    = Browser =         |    = Name(s) =   |
        | Google Chrome          | chrome           |
        | Webkit (Safari engine) | webkit           |
        | Firefox                | firefox          |

        The ``options`` argument as a dictionary

        |    = Property =    |        = Value =       |
        | headless           | default True           |
        | width              | default 1366           |
        | height             | default 768            |
        | emulate            | iPhone 11              |

        Example:

        | &{options} =   | create dictionary                             | headless=${False}  |
        | `Open browser` | https://www.w3schools.com/html/html_forms.asp | options=${options} |

        """
        self.info(url)
        library_context = self.ctx.create_library_context(alias, browser)
        self.loop.run_until_complete(library_context.start_server(options))
        self.loop.run_until_complete(library_context.create_new_page(options))
        self.loop.run_until_complete(self.get_async_keyword_group().go_to(url))

    @keyword
    def close_window(self):
        """ Close current browser tab/page
        """
        self.loop.run_until_complete(self.ctx.get_current_library_context().close_window())

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
        library_contexts_dict =  self.ctx.get_all_library_context_dict()
        for key in list(library_contexts_dict.keys()):
            self.loop.run_until_complete(library_contexts_dict[key].stop_server())
            self.ctx.remove_library_context(key)

    @keyword
    def maximize_browser_window(self, width=1366, height=768):
        """Maximize view port not actual browser and set default size to 1366 x 768
        """
        self.info(('width: ' + str(width) + '\n' +
                   'height: ' + str(height)))
        self.loop.run_until_complete(self.get_async_keyword_group().maximize_browser_window(width, height))

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
        self.info(url)
        self.loop.run_until_complete(self.get_async_keyword_group().go_to(url))

    @keyword
    def reload_page(self):
        """Reload the current page"""
        self.loop.run_until_complete(self.get_async_keyword_group().reload_page())

    @keyword
    def get_window_count(self):
        """ Get windows count
        """
        return  self.loop.run_until_complete(self.get_async_keyword_group().get_window_count())

    @keyword
    def wait_for_new_window_open(self, timeout=None):
        """
        Waits until new page or tab opens.

        Example:

        | Run Async Keywords | Click Element              | id:view_conditions          | AND  |
        | ...                | `Wait For New Window Open` |                             |      |
        """
        self.loop.run_until_complete(self.get_async_keyword_group().wait_for_new_window_open(timeout))

    @keyword
    def switch_window(self, locator='MAIN'):
        """Switches to tabs matching locator
        locator support options NEW, MAIN and query using name, title and url
            - NEW: latest opened window
            - MAIN: main window
            - title="QAHive": window title. Page title will have have error if new tab have auto redirection
            - url="https://qahive.com": url support regex Example: url=.*qahive.com
        """
        self.loop.run_until_complete(self.get_async_keyword_group().switch_window(locator))

    @keyword
    def switch_browser(self, alias):
        """Switch browser context based on alias name
        """
        return self.loop.run_until_complete(self.ctx.set_current_library_context(alias))

    @keyword
    def enable_emulate_mode(self, emulate_name):
        """Emulate specific mobile or tablet

        The ``emulate_name`` argument specifies which emulator to use.
        Only support for chrome (Puppeteer)

        | = Example Options = |
        | iPhone X            |
        | Pixel 2             |

        More emulate_name please visit [device_descriptors.py](https://github.com/qahive/robotframework-puppeteer/tree/master/PuppeteerLibrary/utils/device_descriptors.py)

        """
        return self.loop.run_until_complete(self.get_async_keyword_group().enable_emulate_mode_async(emulate_name))

    ##############################
    # iFrame
    ##############################
    @keyword
    def select_frame(self, locator):
        return self.loop.run_until_complete(self.get_async_keyword_group().select_frame(locator))

    @keyword
    def unselect_frame(self):
        self.get_async_keyword_group().unselect_iframe()

    ##############################
    # Cookies
    ##############################
    @keyword
    def get_cookie(self, name):
        """ Get cookie by name

            Returns Cookie value
        """
        return self.loop.run_until_complete(self.get_async_keyword_group().get_cookie(name))

    @keyword
    def get_cookies(self):
        """ Get all cookies

            Returns Dictionary for all cookies of the current page.
        """
        return self.loop.run_until_complete(self.get_async_keyword_group().get_cookies())

    @keyword
    def add_cookie(self, name, value):
        """ Add cookie
        """
        return self.loop.run_until_complete(self.get_async_keyword_group().add_cookie(name, value))

    @keyword
    def delete_all_cookies(self):
        """ Deletes all cookies.
        """
        return self.loop.run_until_complete(self.get_async_keyword_group().delete_all_cookies())
