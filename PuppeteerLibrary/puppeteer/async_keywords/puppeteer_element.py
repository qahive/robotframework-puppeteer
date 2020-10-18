from PuppeteerLibrary.keywords.ielement_async import iElementAsync


class PuppeteerElement(iElementAsync):

    def __init__(self, library_ctx):
        super().__init__(library_ctx)

    async def click_element(self, locator: str):
        return await self.library_ctx.get_current_page().click_with_selenium_locator(locator)

