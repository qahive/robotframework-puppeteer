from robot.libraries.BuiltIn import BuiltIn
from PuppeteerLibrary.ikeywords.ielement_async import iElementAsync


class PlaywrightElement(iElementAsync):

    def __init__(self, library_ctx):
        super().__init__(library_ctx)

    ##############################
    # Click
    ##############################
    async def click_element(self, locator: str):
        return await self.library_ctx.get_current_page().click_with_selenium_locator(locator)

    async def upload_file(self, locator: str, file_path: str):
        element = await self.library_ctx.get_current_page().querySelector_with_selenium_locator(locator)
        await element.setInputFiles(file_path)

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

    async def element_should_be_visible(self, locator:str):
        try:
            return await self.library_ctx.get_current_page().waitForSelector_with_selenium_locator(locator, 0.1, visible=True, hidden=False)
        except:
            raise AssertionError("Element '%s' is not be visible. " % locator)

    async def element_should_not_be_visible(self, locator:str):
        try:
            return await self.library_ctx.get_current_page().waitForSelector_with_selenium_locator(locator, 0.1, visible=False, hidden=True)
        except:
            raise AssertionError("Element '%s' is visible. " % locator)

    ##############################
    # Property
    ##############################
    async def element_should_contain(self, locator: str, expected: str, ignore_case=False):
        text = await self.get_text(locator)
        return BuiltIn().should_contain(text, expected, ignore_case=ignore_case)

    async def element_should_not_contain(self, locator: str, expected: str, ignore_case=False):
        text = await self.get_text(locator)
        return BuiltIn().should_not_contain(text, expected, ignore_case=ignore_case)

    async def get_text(self, locator: str):
        element = await self.library_ctx.get_current_page().querySelector_with_selenium_locator(locator)
        return (await (await element.getProperty('textContent')).jsonValue())

    async def element_text_should_be(self, locator: str, expected: str, ignore_case=False):
        text = await self.get_text(locator)
        return BuiltIn().should_be_equal_as_strings(text, expected, ignore_case=ignore_case)

    async def element_text_should_not_be(self, locator: str, expected: str, ignore_case=False):
        text = await self.get_text(locator)
        return BuiltIn().should_not_be_equal_as_strings(text, expected, ignore_case=ignore_case)
