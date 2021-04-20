from PuppeteerLibrary.utils.coverter import str2bool, str2str
from PuppeteerLibrary.ikeywords.iscreenshot_async import iScreenshotAsync


class PuppeteerScreenshot(iScreenshotAsync):

    def __init__(self, library_ctx):
        super().__init__(library_ctx)

    async def capture_page_screenshot(self, path: str, fullPage: bool):
        path = str2str(path)
        fullPage = str2bool(fullPage)
        return await self.library_ctx.get_current_page().get_page().screenshot(
            {
                'path': path,
                'fullPage': fullPage
            }
        )
