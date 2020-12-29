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
    
    async def clear_element_text(self, locator: str):
        await self._clear_input_text(locator)

    async def download_file(self, locator: str):
        path = os.getcwd()+'\\tmp-download'
        try:
            shutil.rmtree(path)
        except:
            print('')
        page = self.library_ctx.get_current_page().get_page()
        await page._client.send('Page.setDownloadBehavior', {
            'behavior': 'allow', 
            'downloadPath': path
        })
        await self.library_ctx.get_current_page().click_with_selenium_locator(locator)
        max_wait_time = 30 # 30 seconds
        retry = 0
        file = None
        while retry < max_wait_time:
            time.sleep(1)
            retry = retry + 1
            files = glob.glob(path+'\\*')
            if len(files) == 1: 
                file = files[0]
                break
        return file

    async def _clear_input_text(self, selenium_locator):
        await self.library_ctx.get_current_page().click_with_selenium_locator(selenium_locator, {'clickCount': 3})
        await self.library_ctx.get_current_page().get_page().keyboard.press('Backspace')
