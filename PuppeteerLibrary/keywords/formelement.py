from PuppeteerLibrary.locators import SelectorAbstraction

from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.base.robotlibcore import keyword


class FormElementKeywords(LibraryComponent):

    @keyword
    def input_text(self, selenium_locator, text, clear=True):
        async def input_text_async():
            if clear:
                await self._clear_input_text(selenium_locator)
            await self.ctx.get_current_page().type_with_selenium_locator(selenium_locator, text)
        self.loop.run_until_complete(input_text_async())

    @keyword
    def clear_element_text(self, selenium_locator):
        async def clear_element_text_async():
            await self._clear_input_text(selenium_locator)
        self.loop.run_until_complete(clear_element_text_async())

    async def _clear_input_text(self, selenium_locator):
        await self.ctx.get_current_page().click_with_selenium_locator(selenium_locator, {'clickCount': 3})
        await self.ctx.get_current_page().keyboard.press('Backspace')
