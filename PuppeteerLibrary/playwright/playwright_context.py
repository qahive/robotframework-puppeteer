import asyncio
from PuppeteerLibrary.custom_elements.base_page import BasePage
from PuppeteerLibrary.playwright.custom_elements.playwright_page import PlaywrightPage
from PuppeteerLibrary.playwright.async_keywords.playwright_checkbox import PlaywrightCheckbox
from PuppeteerLibrary.playwright.async_keywords.playwright_mockresponse import PlaywrightMockResponse
from PuppeteerLibrary.playwright.async_keywords.playwright_formelement import PlaywrightFormElement
from PuppeteerLibrary.playwright.async_keywords.playwright_dropdown import PlaywrightDropdown
from PuppeteerLibrary.playwright.async_keywords.playwright_alert import PlaywrightAlert
from PuppeteerLibrary.playwright.async_keywords.playwright_screenshot import PlaywrightScreenshot
from PuppeteerLibrary.playwright.async_keywords.playwright_waiting import PlaywrightWaiting
from PuppeteerLibrary.playwright.async_keywords.playwright_element import PlaywrightElement
from PuppeteerLibrary.playwright.async_keywords.playwright_dropdown import PlaywrightDropdown
from PuppeteerLibrary.playwright.async_keywords.playwright_mouseevent import PlaywrightMouseEvent
from PuppeteerLibrary.playwright.async_keywords.playwright_browsermanagement import PlaywrightBrowserManagement
from PuppeteerLibrary.playwright.async_keywords.playwright_pdf import PlaywrightPDF
from PuppeteerLibrary.playwright.async_keywords.playwright_javascript import PlaywrightJavascript
from PuppeteerLibrary.library_context.ilibrary_context import iLibraryContext
from PuppeteerLibrary.utils.coverter import str2bool, str2int
try:
    from playwright.async_api import async_playwright
    from playwright.playwright import Playwright as AsyncPlaywright
    from playwright.browser import Browser
except ImportError:
    print('import playwright error')


class PlaywrightContext(iLibraryContext):

    playwright: any = None
    browser: any = None
    current_context: any = None
    current_page: any = None
    current_iframe = None

    page_support_options = ['accept_downloads', 'bypass_csp', 'color_scheme', 'device_scale_factor', 'extra_http_headers', 'geolocation', 'has_touch', 'http_credentials', 'ignore_https_errors', 'is_mobile',
                            'java_script_enabled', 'locale', 'no_viewport', 'offline', 'permissions', 'proxy', 'record_har_omit_content', 'record_har_path', 'record_video_dir', 'record_video_size', 'timezone_id', 'user_agent', 'viewport']

    def __init__(self, browser_type: str):
        super().__init__(browser_type)

    async def start_server(self, options: dict = {}):
        default_options = {
            'slowMo': 0,
            'headless': True,
            'devtools': False,
            'viewport': {
                'width': 1366,
                'height': 768,
            },
            'accept_downloads': True
        }
        merged_options = default_options
        merged_options = {**merged_options, **options}
        for key in merged_options.keys():
            if key in ['headless', 'devtools', 'accept_downloads', 'is_mobile']:
                merged_options[key] = str2bool(merged_options[key])
            elif key == 'width':
                merged_options['viewport']['width'] = str2int(
                    merged_options[key])
            elif key == 'height':
                merged_options['viewport']['height'] = str2int(
                    merged_options[key])
            elif key in ['slowMo']:
                merged_options[key] = str2int(merged_options[key])

        # Only start new Playwright server. If server didn't start before
        if self.playwright is None:
            self.playwright = await async_playwright().start()

        if self.browser_type == "chrome" or self.browser_type == "pwchrome":
            proxy = None
            if 'proxy' in merged_options:
                proxy = merged_options['proxy']
                # Chromium can use proxy only via global launch
                del merged_options['proxy']
            self.browser = await self.playwright.chromium.launch(
                headless=merged_options['headless'], proxy=proxy)
            merged_options
        elif self.browser_type == "webkit":
            self.browser = await self.playwright.webkit.launch(
                headless=merged_options['headless'])
        elif self.browser_type == "firefox":
            self.browser = await self.playwright.firefox.launch(
                headless=merged_options['headless'])
        self.browser.accept_downloads = True

    async def stop_server(self):
        await self.playwright.stop()
        self._reset_server_context()

    def is_server_started(self) -> bool:
        if self.browser is not None:
            return True
        return False

    def set_default_timeout(self, timeout):
        self.timeout = timeout
        self.get_current_page().get_page().set_default_timeout(timeout * 1000)

    async def create_new_page(self, options: dict = {}) -> BasePage:
        device_options = {
            'accept_downloads': True,
            'viewport': {
                'width': 1366,
                'height': 768
            }
        }

        for support_key in self.page_support_options:
            if support_key in options:
                device_options[support_key] = options[support_key]
                if support_key in ['accept_downloads', 'ignore_https_errors']:
                    device_options[support_key] = str2bool(
                        device_options[support_key])

            # Force support viewport
            if support_key == 'viewport':
                if 'width' in options.keys():
                    device_options['viewport']['width'] = str2int(
                        options['width'])
                if 'height' in device_options.keys():
                    device_options['viewport']['height'] = str2int(
                        options['height'])

        if 'emulate' in options:
            device_options = self.playwright.devices[options['emulate']]

        if 'state_ref' in options:
            device_options['storage_state'] = './states/state-' + \
                options['state_ref'] + '.json'

        new_page = await self.browser.new_page(**device_options)
        self.current_page = PlaywrightPage(new_page)
        return self.current_page

    def get_current_page(self) -> BasePage:
        return self.current_page

    def set_current_page(self, page: any) -> BasePage:
        self.current_page = PlaywrightPage(page)
        return self.current_page

    async def get_all_pages(self):
        return self.browser.contexts[0].pages

    def get_browser_context(self):
        return self.browser

    async def close_browser_context(self):
        if self.browser is not None:
            try:
                await asyncio.wait_for(self.browser.close(), timeout=3)
            except asyncio.TimeoutError:
                None
        self._reset_context()

    async def close_window(self):
        await self.get_current_page().get_page().close()
        pages = await self.get_all_pages()
        self.set_current_page(pages[-1])

    def get_async_keyword_group(self, keyword_group_name: str):
        switcher = {
            "AlertKeywords": PlaywrightAlert(self),
            "BrowserManagementKeywords": PlaywrightBrowserManagement(self),
            "CheckboxKeywords": PlaywrightCheckbox(self),
            "DropdownKeywords": PlaywrightDropdown(self),
            "ElementKeywords": PlaywrightElement(self),
            "FormElementKeywords": PlaywrightFormElement(self),
            "JavascriptKeywords": PlaywrightJavascript(self),
            "MockResponseKeywords": PlaywrightMockResponse(self),
            "MouseEventKeywords": PlaywrightMouseEvent(self),
            "PDFKeywords": PlaywrightPDF(self),
            "ScreenshotKeywords": PlaywrightScreenshot(self),
            "WaitingKeywords": PlaywrightWaiting(self)
        }
        return switcher.get(keyword_group_name)

    async def start_tracing(self):
        if len(self.browser.contexts) > 0:
            await self.browser.contexts[0].tracing.start(screenshots=True, snapshots=True)

    async def stop_tracing(self, path):
        if len(self.browser.contexts) > 0:
            await self.browser.contexts[0].tracing.stop(path=path)

    def _reset_context(self):
        self.browser = None
        self.current_context = None
        self.current_page = None
        self.current_iframe = None

    def _reset_server_context(self):
        self._reset_context()
        self.playwright = None
