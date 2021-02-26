from PuppeteerLibrary.ikeywords.icheckbox_async import iCheckboxAsync


class PuppeteerCheckbox(iCheckboxAsync):

    def __init__(self, library_ctx):
        super().__init__(library_ctx)

    async def select_checkbox(self, locator):
        if (await self.is_checked(locator)) is False:
            element = await self.library_ctx.get_current_page().querySelector_with_selenium_locator(locator)
            await element.click()

    async def unselect_checkbox(self, locator):
        if (await self.is_checked(locator)) is True:
            element = await self.library_ctx.get_current_page().querySelector_with_selenium_locator(locator)
            await element.click()

    async def checkbox_should_be_selected(self, locator):
        is_checked = await self.is_checked(locator)
        if is_checked is False:
            raise Exception('Checkbox '+locator+' was not selected')

    async def checkbox_should_not_be_selected(self, locator):
        is_checked = await self.is_checked(locator)
        if is_checked is True:
            raise Exception('Checkbox '+locator+' was selected')
    
    async def is_checked(self, locator):
        element = await self.library_ctx.get_current_page().querySelector_with_selenium_locator(locator)
        return (await (await element.getProperty('checked')).jsonValue())
