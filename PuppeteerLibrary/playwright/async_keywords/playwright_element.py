from PuppeteerLibrary.keywords.ielement_async import iElementAsync


class PlaywrightElement(iElementAsync):

    def __init__(self, library_ctx):
        super().__init__(library_ctx)

    ##############################
    # Click
    ##############################
    async def click_element(self, locator: str):
        return await self.library_ctx.get_current_page().click_with_selenium_locator(locator)

    ##############################
    # Status
    ##############################
    async def element_should_be_enabled(self, locator: str):
        pass

    async def element_should_be_disabled(self, locator: str):
        pass
