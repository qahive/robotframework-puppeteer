from PuppeteerLibrary.keywords.ielement_async import iElementAsync


class PuppeteerElement(iElementAsync):

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
        element = await self.library_ctx.get_current_page().querySelector_with_selenium_locator(locator)
        is_disabled = await (await element.getProperty('disabled')).jsonValue()
        if is_disabled:
            raise AssertionError("Element '%s' is disabled. " % locator)
        return element

    async def element_should_be_disabled(self, locator: str):
        element = await self.library_ctx.get_current_page().querySelector_with_selenium_locator(locator)
        is_disabled = await (await element.getProperty('disabled')).jsonValue()
        if not is_disabled:
            raise AssertionError("Element '%s' is enabled. " % locator)
        return element
