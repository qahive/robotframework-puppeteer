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
