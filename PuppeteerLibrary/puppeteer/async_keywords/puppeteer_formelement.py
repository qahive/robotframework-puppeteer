import os
import glob
import shutil
import time
from PuppeteerLibrary.ikeywords.iformelement_async import iFormElementAsync


class PuppeteerFormElement(iFormElementAsync):

    def __init__(self, library_ctx):
        super().__init__(library_ctx)

    async def input_text(self, locator: str, text: str, clear=True):
        if clear:
            await self._clear_input_text(locator)
        await self.library_ctx.get_current_page().type_with_selenium_locator(locator, text)
    
    async def input_password(self, locator: str, text: str, clear=True):
        await self.input_text(locator, text, clear)

    async def clear_element_text(self, locator: str):
        await self._clear_input_text(locator)

    async def download_file(self, locator: str, timeout=None):
        path = os.getcwd()+''+os.sep+'tmp-download'
        try:
            shutil.rmtree(path)
        except:
            self.info('Cannot cleanup the tmp download folder.')
        page = self.library_ctx.get_current_page().get_page()
        await page._client.send('Page.setDownloadBehavior', {
            'behavior': 'allow', 
            'downloadPath': path
        })
        await self.library_ctx.get_current_page().click_with_selenium_locator(locator)
        timeout = self.timestr_to_secs_for_default_timeout(timeout)
        max_time = time.time() + timeout
        file = None
        while time.time() < max_time:
            time.sleep(1)
            files = glob.glob(path+''+os.sep+'*')
            if len(files) == 1: 
                file = files[0]
                break
        return file

    async def upload_file(self, locator: str, file_path: str):
        element = await self.library_ctx.get_current_page().querySelector_with_selenium_locator(locator)
        return await element.uploadFile(file_path)
        
    async def _clear_input_text(self, selenium_locator):
        await self.library_ctx.get_current_page().click_with_selenium_locator(selenium_locator, {'clickCount': 3})
        await self.library_ctx.get_current_page().get_page().keyboard.press('Backspace')
