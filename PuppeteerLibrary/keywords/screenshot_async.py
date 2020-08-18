import os
from robot.utils import get_link_path
from PuppeteerLibrary.base.robotlibcore import keyword
from PuppeteerLibrary.base.librarycomponent import LibraryComponent

DEFAULT_FILENAME_PAGE = 'puppeteer-screenshot-{index}.png'

class ScreenshotKeywordsAsync(LibraryComponent):

    def __init__(self, ctx):
        self.ctx = ctx
        self.log_dir = os.curdir

    @keyword
    async def capture_page_screenshot_async(self, filename=DEFAULT_FILENAME_PAGE):
        path = self._get_screenshot_path(filename)
        await self.ctx.current_page.screenshot({'path': path})
        self._embed_to_log_as_file(path, 800)

    def _get_screenshot_path(self, filename):
        directory = self.log_dir
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
        # Image is shown on its own row and thus previous row is closed on
        # purpose. Depending on Robot's log structure is a bit risky.
        self.info('</td></tr><tr><td colspan="3">'
                  '<a href="{src}"><img src="{src}" width="{width}px"></a>'
                  .format(src=get_link_path(path, self.log_dir), width=width), html=True)

class _SafeFormatter(dict):

    def __missing__(self, key):
        return '{%s}' % key
