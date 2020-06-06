from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.base.robotlibcore import keyword


class FormElementKeywords(LibraryComponent):

    @keyword
    def input_text(self, locator, text, clear=True):
        async def input_text_async():
            if clear:
                await self._clear_input_text(locator)
            await self.ctx.get_current_page().type(locator, text)
        self.loop.run_until_complete(input_text_async())

    async def _clear_input_text(self, locator):
        await self.ctx.get_current_page().click(locator, {'clickCount': 3})
        await self.ctx.get_current_page().keyboard.press('Backspace')
