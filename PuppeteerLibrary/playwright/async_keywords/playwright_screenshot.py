from PuppeteerLibrary.playwright.async_keywords.playwright_waiting import PlaywrightWaiting
from PuppeteerLibrary.keywords.iscreenshot_async import iScreenshotAsync


class PlaywrightScreenshot(iScreenshotAsync):

    def __init__(self, library_ctx):
        super().__init__(library_ctx)

    async def capture_page_screenshot(self, path: str):
        return await self.library_ctx.get_current_page().get_page().screenshot(
            path=f''+path
        )
