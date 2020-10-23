from robot.libraries.BuiltIn import BuiltIn
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

    async def element_should_be_visible(self, locator:str):
        pass

    async def element_should_not_be_visible(self, locator:str):
        pass

    ##############################
    # Property
    ##############################
    async def element_should_contain(self, locator: str, expected: str, ignore_case=False):
        pass

    async def element_should_not_contain(self, locator: str, expected: str, ignore_case=False):
        pass

    async def get_text(self, locator: str):
        pass

    async def element_text_should_be(self, locator: str, expected: str, ignore_case=False):
        pass

    async def element_text_should_not_be(self, locator: str, expected: str, ignore_case=False):
        pass
