from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.base.robotlibcore import keyword


class ElementKeywords(LibraryComponent):

    @keyword
    def click_element(self, selenium_locator):
        async def click_element_async():
            return await self.ctx.get_current_page().click_with_selenium_locator(selenium_locator)
        self.loop.run_until_complete(click_element_async())

    @keyword
    def click_link(self, selenium_locator):
        async def click_link_async():
            elements = await self.ctx.get_current_page().querySelectorAll_with_selenium_locator(selenium_locator)
            for element in elements:
                tag_name = (await (await element.getProperty('tagName')).jsonValue()).lower()
                if tag_name == 'a':
                    return await element.click()
            raise Exception('Not found link with specific locator '+selenium_locator)
        self.loop.run_until_complete(click_link_async())

    @keyword
    def click_button(self, selenium_locator):
        async def click_button_async():
            elements = await self.ctx.get_current_page().querySelectorAll_with_selenium_locator(selenium_locator)
            for element in elements:
                tag_name = (await (await element.getProperty('tagName')).jsonValue()).lower()
                if tag_name == 'button':
                    return await element.click()
            raise Exception('Not found button with specific locator ' + selenium_locator)
        self.loop.run_until_complete(click_button_async())

    @keyword
    def click_image(self, selenium_locator):
        async def click_image_async():
            elements = await self.ctx.get_current_page().querySelectorAll_with_selenium_locator(selenium_locator)
            for element in elements:
                tag_name = (await (await element.getProperty('tagName')).jsonValue()).lower()
                if tag_name == 'img':
                    return element.click()
            raise Exception('Not found button with specific locator ' + selenium_locator)
        self.loop.run_until_complete(click_image_async())

    @keyword
    def get_text(self, selenium_locator):
        async def get_text_async():
            element = await self.ctx.get_current_page().querySelector_with_selenium_locator(selenium_locator)
            return (await (await element.getProperty('textContent')).jsonValue())
        return self.loop.run_until_complete(get_text_async())

    @keyword
    def get_value(self, selenium_locator):
        async def get_text_async():
            element = await self.ctx.get_current_page().querySelector_with_selenium_locator(selenium_locator)
            return (await (await element.getProperty('value')).jsonValue())
        return self.loop.run_until_complete(get_text_async())
