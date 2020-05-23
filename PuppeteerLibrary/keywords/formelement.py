from pyppeteer.page import Page

from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.base.robotlibcore import keyword


class FormElementKeywords(LibraryComponent):

    @keyword
    def input_text(self, locator, text, clear=True):
        self.info("Typing text '%s' into text field '%s'." % (text, locator))
        self.loop.run_until_complete(self.input_text_async(locator, text, clear))

    async def input_text_async(self, locator, text, clear):
        if clear:
            await self.clear(locator)
        await self.ctx.getCurrentPage().type('#fname', text)

    async def clear(self, locator):
        await self.ctx.getCurrentPage().click('#fname', {'clickCount': 3})
        await self.ctx.getCurrentPage().keyboard.press('Backspace')

    '''
    async function clear(page, selector)
    {
        await page.evaluate(selector= > {
            document.querySelector(selector).value = "";
    }, selector);
    }
    '''
