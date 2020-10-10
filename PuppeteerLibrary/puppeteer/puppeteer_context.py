import sys
from pyppeteer import launch
from pyppeteer.browser import Browser
from PuppeteerLibrary.library_context.ilibrary_context import iLibraryContext

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
