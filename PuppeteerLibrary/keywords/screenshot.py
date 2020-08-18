from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.base.robotlibcore import keyword
from PuppeteerLibrary.keywords.screenshot_async import ScreenshotKeywordsAsync, DEFAULT_FILENAME_PAGE


class ScreenshotKeywords(LibraryComponent):

    def __init__(self, ctx):
        super().__init__(ctx)
        self.async_func = ScreenshotKeywordsAsync(self.ctx)

    @keyword
    def capture_page_screenshot(self, filename=DEFAULT_FILENAME_PAGE):
        """
        Capture current web page as image png file.

        The ``filename`` argument specifies filename and path to save the file.
        Default valid is 'puppeteer-screenshot-{index}.png'.

        Example:

        | Capture page screenshot   |                    |
        | Capture page screenshot   | custom-{index}.png |

        """
        return self.loop.run_until_complete(self.async_func.capture_page_screenshot_async(filename))
