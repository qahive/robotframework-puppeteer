from PuppeteerLibrary.utils.coverter import str2bool
from typing import Optional
from robot.libraries.BuiltIn import BuiltIn
from PuppeteerLibrary.ikeywords.ielement_async import iElementAsync


class PuppeteerElement(iElementAsync):

    def __init__(self, library_ctx):
        super().__init__(library_ctx)

    ##############################
    # Query Element
    ##############################
    async def find_elements(self, locator: str):
        return await self.library_ctx.get_current_page().querySelectorAll_with_selenium_locator(locator)

    ##############################
    # Click
    ##############################
    async def click_element(self, locator: str, noWaitAfter: str='False'):
        element = await self.library_ctx.get_current_page().querySelector_with_selenium_locator(locator)
        await element.click()

    async def click_link(self, locator: str):
        await self._click_with_specific_tag(locator,'a')

    async def click_button(self, locator: str):
        await self._click_with_specific_tag(locator,'button')

    async def click_image(self, locator: str):
        await self._click_with_specific_tag(locator,'img')

    async def _click_with_specific_tag(self, locator: str, expect_tag_name: str):
        elements = await self.library_ctx.get_current_page().querySelectorAll_with_selenium_locator(locator)
        for element in elements:
            tag_name = await (await element.getProperty('tagName')).jsonValue()
            if tag_name.lower() == expect_tag_name:
                return await element.click()
        raise Exception('Can\'t find the specific '+ expect_tag_name +' element for '+locator)

    async def click_element_at_coordinate(self, locator: str, xoffset: str, yoffset: str):
        element = await self.library_ctx.get_current_page().querySelector_with_selenium_locator(locator)
        bounding_box = await element.boundingBox()
        await self.library_ctx.get_current_page().get_page().mouse.move(
            bounding_box['x'] + int(xoffset),
            bounding_box['y'] + int(yoffset))
        await self.library_ctx.get_current_page().get_page().mouse.down()
        await self.library_ctx.get_current_page().get_page().mouse.up()

    async def upload_file(self, locator: str, file_path: str):
        element = await self.library_ctx.get_current_page().querySelector_with_selenium_locator(locator)
        await element.uploadFile(file_path)

    async def press_keys(self, locator: str, *keys: str):
        element = await self.library_ctx.get_current_page().querySelector_with_selenium_locator(locator)
        for key in keys:
            await element.press(key)

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
        return (await (await element.getProperty('innerText')).jsonValue())

    async def get_attribute(self, locator: str, attribute: str) -> str:
        element = await self.library_ctx.get_current_page().querySelector_with_selenium_locator(locator)
        return (await (await element.getProperty(attribute)).jsonValue())
        
    async def element_text_should_be(self, locator: str, expected: str, ignore_case=False):
        text = await self.get_text(locator)
        return BuiltIn().should_be_equal_as_strings(text, expected, ignore_case=ignore_case)

    async def element_text_should_not_be(self, locator: str, expected: str, ignore_case=False):
        text = await self.get_text(locator)
        return BuiltIn().should_not_be_equal_as_strings(text, expected, ignore_case=ignore_case)

    ##############################
    # Scrolling
    ##############################
    async def scroll_element_into_view(self, locator: str):
        element = await self.library_ctx.get_current_page().querySelector_with_selenium_locator(locator)        
        await element.focus()
