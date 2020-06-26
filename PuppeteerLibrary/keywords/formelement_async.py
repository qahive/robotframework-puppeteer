from robot.api.deco import not_keyword
from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.base.robotlibcore import keyword


class FormElementKeywordsAsync(LibraryComponent):

    @keyword
    async def input_text_async(self, selenium_locator, text, clear=True):
        if clear:
            await self._clear_input_text(selenium_locator)
        await self.ctx.get_current_page().type_with_selenium_locator(selenium_locator, text)

    @keyword
    async def clear_element_text_async(self, selenium_locator):
        await self._clear_input_text(selenium_locator)

    @not_keyword
    async def _clear_input_text(self, selenium_locator):
        await self.ctx.get_current_page().click_with_selenium_locator(selenium_locator, {'clickCount': 3})
        await self.ctx.get_current_page().keyboard.press('Backspace')
