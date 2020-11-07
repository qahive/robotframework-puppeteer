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

    def __init__(self, browser_type: str):
        super().__init__(browser_type)

    async def start_server(self, options: dict=None):
        default_args = []
        default_options = {
            'slowMo': 0,
            'headless': True,
            'devtools': False,
            'width': 1366,
            'height': 768
        }
        merged_options = default_options

        if options is not None:
            merged_options = {**merged_options, **options}

        if self.debug_mode is True:
            merged_options = {**merged_options, **self.debug_mode_options}

        if 'win' not in sys.platform.lower():
            default_args = ['--no-sandbox', '--disable-setuid-sandbox']

        self.browser = await launch(
            headless=merged_options['headless'],
            slowMo=merged_options['slowMo'],
            devtools=merged_options['devtools'],
            defaultViewport={
                'width': merged_options['width'],
                'height': merged_options['height']
            },
            args=default_args)

    async def stop_server(self):
        await self.browser.close()
        self._reset_context()
    
    def is_server_started(self) -> bool:
        if self.browser is not None:
            return True
        return False

    async def create_new_page(self, options: dict=None) -> BasePage:
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
