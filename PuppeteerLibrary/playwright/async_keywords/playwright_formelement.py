import asyncio
from PuppeteerLibrary.ikeywords.iformelement_async import iFormElementAsync
from PuppeteerLibrary.locators.SelectorAbstraction import SelectorAbstraction
from PuppeteerLibrary.utils.coverter import str2bool, str2str


class PlaywrightFormElement(iFormElementAsync):

    def __init__(self, library_ctx):
        super().__init__(library_ctx)

    async def input_text(self, locator: str, text: str, clear=True):
        text = str2str(text)
        clear = str2bool(clear)
        if clear:
            await self._clear_input_text(locator)
        await self.library_ctx.get_current_page().type_with_selenium_locator(locator, text)
    
    async def input_password(self, locator: str, text: str, clear=True):
        text = str2str(text)
        clear = str2bool(clear)
        await self.input_text(locator, text, clear)

    async def clear_element_text(self, locator: str):
        await self._clear_input_text(locator)
    
    async def download_file(self, locator: str, timeout=None):
        timeout = self.timestr_to_secs_for_default_timeout(timeout)* 1000
        page = self.library_ctx.get_current_page().get_page()
        tasks = self.library_ctx.get_current_page().click_with_selenium_locator(locator), page.wait_for_event('download', timeout=timeout)
        _, b = await asyncio.gather(*tasks)
        path = str(await b.path())
        return path.replace('\\', '\\\\')

    async def upload_file(self, locator: str, file_path: str):
        file_path = str2str(file_path)
        handle = await self.library_ctx.get_current_page().querySelector_with_selenium_locator(locator)
        await handle.set_input_files(file_path)

    async def _clear_input_text(self, selenium_locator):
        await self.library_ctx.get_current_page().click_with_selenium_locator(selenium_locator, {'click_count': 3})
        await self.library_ctx.get_current_page().get_page().keyboard.press('Backspace')
