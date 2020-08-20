from robot.libraries.BuiltIn import BuiltIn

from PuppeteerLibrary.base.robotlibcore import keyword
from PuppeteerLibrary.base.librarycomponent import LibraryComponent


class ElementKeywordsAsync(LibraryComponent):

    @keyword
    async def click_element_async(self, selenium_locator):
        return await self.ctx.get_current_page().click_with_selenium_locator(selenium_locator)

    @keyword
    async def click_link_async(self, selenium_locator):
        elements = await self.ctx.get_current_page().querySelectorAll_with_selenium_locator(selenium_locator)
        for element in elements:
            tag_name = (await (await element.getProperty('tagName')).jsonValue()).lower()
            if tag_name == 'a':
                return await element.click()
        raise Exception('Not found link with specific locator ' + selenium_locator)

    @keyword
    async def click_button_async(self, selenium_locator):
        elements = await self.ctx.get_current_page().querySelectorAll_with_selenium_locator(selenium_locator)
        for element in elements:
            tag_name = (await (await element.getProperty('tagName')).jsonValue()).lower()
            if tag_name == 'button':
                return await element.click()
        raise Exception('Not found button with specific locator ' + selenium_locator)

    @keyword
    async def click_image_async(self, selenium_locator):
        elements = await self.ctx.get_current_page().querySelectorAll_with_selenium_locator(selenium_locator)
        for element in elements:
            tag_name = (await (await element.getProperty('tagName')).jsonValue()).lower()
            if tag_name == 'img':
                return element.click()
        raise Exception('Not found button with specific locator ' + selenium_locator)

    @keyword
    async def get_text_async(self, selenium_locator):
        element = await self.ctx.get_current_page().querySelector_with_selenium_locator(selenium_locator)
        return (await (await element.getProperty('textContent')).jsonValue())

    @keyword
    async def get_value_async(self, selenium_locator):
        element = await self.ctx.get_current_page().querySelector_with_selenium_locator(selenium_locator)
        return (await (await element.getProperty('value')).jsonValue())

    @keyword
    async def element_should_be_disabled_async(self, selenium_locator):
        element = await self.ctx.get_current_page().querySelector_with_selenium_locator(selenium_locator)
        is_disabled = await (await element.getProperty('disabled')).jsonValue()
        if not is_disabled:
            raise AssertionError("Element '%s' is enabled. " % selenium_locator)
        return element

    @keyword
    async def element_should_be_enabled_async(self, selenium_locator):
        element = await self.ctx.get_current_page().querySelector_with_selenium_locator(selenium_locator)
        is_disabled = await (await element.getProperty('disabled')).jsonValue()
        if is_disabled:
            raise AssertionError("Element '%s' is disabled. " % selenium_locator)
        return element

    @keyword
    async def element_should_be_visible_async(self, selenium_locator):
        try:
            return await self.ctx.get_current_page().waitForSelector_with_selenium_locator(selenium_locator, 0.1, visible=True, hidden=False)
        except:
            raise AssertionError("Element '%s' is not be visible. " % selenium_locator)

    @keyword
    async def element_should_not_be_visible_async(self, selenium_locator):
        try:
            return await self.ctx.get_current_page().waitForSelector_with_selenium_locator(selenium_locator, 0.1, visible=False, hidden=True)
        except:
            raise AssertionError("Element '%s' is visible. " % selenium_locator)

    @keyword
    async def element_should_contain_async(self, selenium_locator, expected, ignore_case=False):
        text = await self.get_text_async(selenium_locator)
        return BuiltIn().should_contain(text, expected, ignore_case=ignore_case)

    @keyword
    async def element_should_not_contain_async(self, selenium_locator, expected, ignore_case=False):
        text = await self.get_text_async(selenium_locator)
        return BuiltIn().should_not_contain(text, expected, ignore_case=ignore_case)

    @keyword
    async def element_text_should_be_async(self, selenium_locator, expected, ignore_case=False):
        text = await self.get_text_async(selenium_locator)
        return BuiltIn().should_be_equal_as_strings(text, expected, ignore_case=ignore_case)

    @keyword
    async def element_text_should_not_be_async(self, selenium_locator, expected, ignore_case=False):
        text = await self.get_text_async(selenium_locator)
        return BuiltIn().should_not_be_equal_as_strings(text, expected, ignore_case=ignore_case)

    @keyword
    async def upload_file_async(self, selenium_locator, file_path):
        element = await self.ctx.get_current_page().querySelector_with_selenium_locator(selenium_locator)
        await element.uploadFile(file_path)
