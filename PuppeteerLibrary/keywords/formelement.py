from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.base.robotlibcore import keyword


class FormElementKeywords(LibraryComponent):

    @keyword
    def input_text(self, locator, text, clear=True):
        locator = locator.replace('id=', '#')
        async def input_text_async():
            if clear:
                await self._clear_input_text(locator)
            await self.ctx.getCurrentPage().type(locator, text)
        self.loop.run_until_complete(input_text_async())

    async def _clear_input_text(self, locator):
        await self.ctx.getCurrentPage().click(locator, {'clickCount': 3})
        await self.ctx.getCurrentPage().keyboard.press('Backspace')
