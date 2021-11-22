import os
import shutil
from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.base.robotlibcore import keyword
from PuppeteerLibrary.ikeywords.ibrowsermanagement_async import iBrowserManagementAsync
from robot.libraries.BuiltIn import BuiltIn


class BrowserManagementKeywords(LibraryComponent):

    def __init__(self, ctx):
        super().__init__(ctx)
        self.STATES_FOLDER = './states'

    def get_async_keyword_group(self) -> iBrowserManagementAsync:
        return self.ctx.get_current_library_context().get_async_keyword_group(type(self).__name__)

    @keyword
    def open_browser(self, url, browser="chrome", alias=None, options={}):
        """Opens a new browser instance to the specific ``url``.

        The ``browser`` argument specifies which browser to use.

        |    = Browser =           |    = Name(s) =   |    = Engine =   |
        | Google Chrome Default    | chrome           | Playwright      |
        | Google Chrome Playwright | pwchrome         | Playwright      |
        | Google Chrome Puppeteer  | ptchrome         | Puppeteer       |
        | Webkit (Safari engine)   | webkit           | Playwright      |
        | Firefox                  | firefox          | Playwright      |

        The ``options`` argument as a dictionary

        |    = Property =    |        = Value =       |
        | headless           | default True           |
        | width              | default 1366           |
        | height             | default 768            |
        | emulate            | iPhone 11              |
        | state_ref          | State Reference        |

        **Other options**
        pwchrome, webkit and firefox please visit: https://playwright.dev/python/docs/api/class-browser?_highlight=new_page#browsernew_pagekwargs
        chrome please visit: https://pptr.dev/#?product=Puppeteer&version=v8.0.0&show=api-puppeteerlaunchoptions

        Example:

        | &{options} =   | create dictionary                             | headless=${False}  |
        | `Open browser` | https://www.w3schools.com/html/html_forms.asp | options=${options} |

        """
        if options is None:
            options = {}
            
        self.info(url)
        library_context = self.ctx.get_library_context_by_name(alias)
        if library_context is None:
            library_context = self.ctx.create_library_context(alias, browser)
        self.loop.run_until_complete(self.ctx.set_current_library_context(alias))
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
        library_contexts_dict = self.ctx.get_all_library_context_dict()
        for key in list(library_contexts_dict.keys()):
            self.loop.run_until_complete(library_contexts_dict[key].stop_server())
            self.ctx.remove_library_context(key)

    @keyword
    def get_title(self):
        """Get page title"""
        return self.loop.run_until_complete(self.ctx.get_current_library_context().get_current_page().title())

    @keyword
    def get_location(self):
        """Get page location"""
        return self.ctx.get_current_library_context().get_current_page().get_page().url

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
    # Trace
    ##############################
    @keyword
    def start_tracing(self):
        """Create trace log file

        # View the trace by running following command

        playwright show-trace trace.zip
        """
        return self.loop.run_until_complete(self.get_async_keyword_group().start_tracing())

    @keyword
    def stop_tracing(self, path=None):
        """Stop trace and generate the trace file.

        Default will be ``traces/<testcasename>.zip``
        """
        if path is None:
            test_name = BuiltIn().get_variable_value("${TEST_NAME}")
            path = 'traces/'+test_name+'.zip'
        return self.loop.run_until_complete(self.get_async_keyword_group().stop_tracing(path))

    ##############################
    # Page
    ##############################
    @keyword
    def set_view_port_size(self, width, height):
        return self.loop.run_until_complete(self.get_async_keyword_group().set_view_port_size(width, height))

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

    ##############################
    # State
    ##############################
    @keyword
    def save_browser_storage_state(self, ref='user'):
        """ Save browser storage state that can resue Authentication state

            *ref* : reference state name

            *Limitation* only support Playwright browser
        """
        self.info('Save storate state for ' + ref)
        try:
            os.mkdir(self.STATES_FOLDER)
        except:
            self.info('states folder already exists.')
        return self.loop.run_until_complete(self.get_async_keyword_group().save_browser_storage_state(self.STATES_FOLDER, ref))

    @keyword
    def delete_browser_storage_state(self, ref):
        """ Delete browser storage state

            *ref* : reference state name

            *Limitation* only support Playwright browser
        """
        file_path = self.STATES_FOLDER +'/state-'+ ref + '.json'
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            self.warn('Can not delete the storate '+ref+' as it doesn\'t exists')

    @keyword
    def delete_all_browser_storage_states(self):
        """ Delete all browser storage state

            *Limitation* only support Playwright browser
        """
        try:
            shutil.rmtree(self.STATES_FOLDER)
        except OSError as e:
            self.warn("Error: %s - %s." % (e.filename, e.strerror))

