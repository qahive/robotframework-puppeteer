import os
from robot.utils import get_link_path
from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.base.robotlibcore import keyword
from PuppeteerLibrary.ikeywords.iscreenshot_async import DEFAULT_FILENAME_PAGE, iScreenshotAsync


class ScreenshotKeywords(LibraryComponent):

    def __init__(self, ctx):
        super().__init__(ctx)

    def get_async_keyword_group(self) -> iScreenshotAsync:
        return self.ctx.get_current_library_context().get_async_keyword_group(type(self).__name__)

    @keyword
    def set_screenshot_directory(self, path):
        self.ctx.get_current_library_context().set_screenshot_path(path)

    @keyword
    def get_screenshot_directory(self):
        return self.ctx.get_current_library_context().get_screenshot_path()

    @keyword
    def capture_page_screenshot(self, filename=DEFAULT_FILENAME_PAGE, fullPage=False):
        """
        Capture current web page as image png file.

        The ``filename`` argument specifies filename and path to save the file.
        Default valid is 'puppeteer-screenshot-{index}.png'.
        
        The ``fullPage`` argument specifieds capture screenshot as full page.

        Example:

        | Capture page screenshot   |                    |
        | Capture page screenshot   | custom-{index}.png |

        """
        path = self._get_screenshot_path(filename)
        self.loop.run_until_complete(self.get_async_keyword_group().capture_page_screenshot(path, bool(fullPage)))
        self._embed_to_log_as_file(path, 800)
    
    def _get_screenshot_path(self, filename):
        directory = self.ctx.get_current_library_context().get_screenshot_path()
        filename = filename.replace('/', os.sep)
        index = 0
        while True:
            index += 1
            formatted = self._format_path(filename, index)
            path = os.path.join(directory, formatted)
            if formatted == filename or not os.path.exists(path):
                return path

    def _format_path(self, file_path, index):
        return file_path.format_map(_SafeFormatter(index=index))

    def _embed_to_log_as_file(self, path, width):
        """
        Image is shown on its own row and thus previous row is closed on purpose.
        Depending on Robot's log structure is a bit risky.
        
        """
        self.info('</td></tr><tr><td colspan="3">'
                  '<a href="{src}"><img src="{src}" width="{width}px"></a>'
                  .format(src=get_link_path(path, os.curdir), width=width), html=True)

class _SafeFormatter(dict):

    def __missing__(self, key):
        return '{%s}' % key
