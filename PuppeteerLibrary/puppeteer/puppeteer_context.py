from PuppeteerLibrary.utils.coverter import str2bool, str2int
import sys
from pyppeteer import launch
from pyppeteer.browser import Browser
from PuppeteerLibrary.custom_elements.base_page import BasePage
from PuppeteerLibrary.library_context.ilibrary_context import iLibraryContext
from PuppeteerLibrary.puppeteer.async_keywords.puppeteer_alert import PuppeteerAlert
from PuppeteerLibrary.puppeteer.async_keywords.puppeteer_checkbox import PuppeteerCheckbox
from PuppeteerLibrary.puppeteer.async_keywords.puppeteer_screenshot import PuppeteerScreenshot
from PuppeteerLibrary.puppeteer.async_keywords.puppeteer_waiting import PuppeteerWaiting
from PuppeteerLibrary.puppeteer.async_keywords.puppeteer_browsermanagement import PuppeteerBrowserManagement
from PuppeteerLibrary.puppeteer.async_keywords.puppeteer_dropdown import PuppeteerDropdown
from PuppeteerLibrary.puppeteer.async_keywords.puppeteer_element import PuppeteerElement
from PuppeteerLibrary.puppeteer.async_keywords.puppeteer_formelement import PuppeteerFormElement
from PuppeteerLibrary.puppeteer.async_keywords.puppeteer_mouseevent import PuppeteerMouseEvent
from PuppeteerLibrary.puppeteer.custom_elements.puppeteer_page import PuppeteerPage
from PuppeteerLibrary.puppeteer.async_keywords.puppeteer_pdf import PuppeteerPDF
from PuppeteerLibrary.puppeteer.async_keywords.puppeteer_javascript import PuppeteerJavascript
from PuppeteerLibrary.puppeteer.async_keywords.puppeteer_mockresponse import PuppeteerMockResponse
from PuppeteerLibrary.utils.device_descriptors import DEVICE_DESCRIPTORS


class PuppeteerContext(iLibraryContext):

    browser: Browser = None
    contexts = {}
    current_page = None
    current_iframe = None

    debug_mode: bool = False
    debug_mode_options: dict = {
        'slowMo': 200,
        'devtools': False
    }

    page_support_options = ['ignoreHTTPSErrors', 'headless', 'executablePath', 'slowMo', 'defaultViewport', 'handleSIGINT', 'handleSIGTERM', 'handleSIGHUP', 'userDataDir', 'env', 'devtools']

    def __init__(self, browser_type: str):
        super().__init__(browser_type)

    async def start_server(self, options: dict={}):
        default_args = []
        merged_options = {
            'slowMo': 0,
            'headless': True,
            'devtools': False,
            'defaultViewport': {
                'width': 1366,
                'height': 768
            }
        }
        merged_options = {**merged_options, **options}
        for key in merged_options.keys():
            if key in ['headless', 'devtools', 'ignoreHTTPSErrors']:
                merged_options[key] = str2bool(merged_options[key])
            elif key in ['slowMo']:
                merged_options[key] = str2int(merged_options[key])
            elif key == 'defaultViewport':
                merged_options[key] = {
                    'width': str2int(merged_options[key]['width']),
                    'height': str2int(merged_options[key]['height'])
                }

        if self.debug_mode is True:
            merged_options = {**merged_options, **self.debug_mode_options}

        if 'win' not in sys.platform.lower():
            default_args = ['--no-sandbox', '--disable-setuid-sandbox']
            
        for support_key in self.page_support_options:
            if support_key in options:
               merged_options[support_key] = options[support_key]

        self.browser = await launch(
            **merged_options,
            args=default_args)

    async def stop_server(self):
        await self.browser.close()
        self._reset_context()
    
    def is_server_started(self) -> bool:
        if self.browser is not None:
            return True
        return False

    def set_default_timeout(self, timeout):
        self.timeout = timeout

    async def create_new_page(self, options: dict={}) -> BasePage:
        new_page = await self.browser.newPage()
        self.current_page = PuppeteerPage(new_page)
        if 'emulate' in options:
            await self.current_page.get_page().emulate(DEVICE_DESCRIPTORS[options['emulate']])
        return self.current_page

    def get_current_page(self) -> BasePage:
        return self.current_page

    def set_current_page(self, page: any) -> BasePage:
        self.current_page = PuppeteerPage(page)
        return self.current_page

    async def get_all_pages(self):
        return await self.browser.pages()

    def get_browser_context(self):
        return self.browser

    async def close_browser_context(self):
        await self.browser.close()
    
    async def close_window(self):
        await self.get_current_page().get_page().close()
        pages = await self.get_all_pages()
        self.set_current_page(pages[-1])

    def get_async_keyword_group(self, keyword_group_name: str):
        switcher = {
            "AlertKeywords": PuppeteerAlert(self),
            "BrowserManagementKeywords": PuppeteerBrowserManagement(self),
            "CheckboxKeywords": PuppeteerCheckbox(self),
            "DropdownKeywords": PuppeteerDropdown(self),
            "ElementKeywords": PuppeteerElement(self),
            "FormElementKeywords": PuppeteerFormElement(self),
            "JavascriptKeywords": PuppeteerJavascript(self),
            "MockResponseKeywords": PuppeteerMockResponse(self),
            "MouseEventKeywords": PuppeteerMouseEvent(self),
            "PDFKeywords": PuppeteerPDF(self),
            "ScreenshotKeywords": PuppeteerScreenshot(self),
            "WaitingKeywords": PuppeteerWaiting(self)
        }
        return switcher.get(keyword_group_name)

    def _reset_context(self):
        browser = None
        contexts = {}
        current_page = None
        current_iframe = None
        debug_mode = False
        debug_mode_options = {
            'slowMo': 200,
            'devtools': False
        }
