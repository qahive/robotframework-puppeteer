import asyncio
import re
import time
from PuppeteerLibrary.ikeywords.ibrowsermanagement_async import iBrowserManagementAsync


class PuppeteerBrowserManagement(iBrowserManagementAsync):

    def __init__(self, library_ctx):
        super().__init__(library_ctx)

    async def maximize_browser_window(self, width=1366, height=768):
        return await self.ctx.get_current_page().setViewport({
            'width': width,
            'height': height
        })

    async def go_to(self, url):
        return await self.library_ctx.get_current_page().goto(url)

    async def go_back(self):
        return await self.library_ctx.get_current_page().go_back()

    async def reload_page(self):
        return await self.library_ctx.get_current_page().reload_page()

    async def get_window_count(self):
        pages = await self.library_ctx.get_all_pages()
        for page in pages:
            # Workaround: for force pages re-cache
            try:
                await page.title()
            except:
                return -1
        return len(await self.library_ctx.get_all_pages()) - 1

    async def wait_for_new_window_open(self, timeout=None):
        page_len = 0
        # Workaround:
        # We get length without force reset. For ensure that when we count page length.
        # Page length still not update / same as before open new window
        pre_page_len = len(await self.library_ctx.get_all_pages())
        timeout = self.timestr_to_secs_for_default_timeout(timeout)
        max_time = time.time() + timeout
        while time.time() < max_time:
            page_len = await self._get_window_count_async()
            if page_len > pre_page_len:
                return
            await asyncio.sleep(0.5)
        raise Exception('No new page has been open. pre: ' + str(pre_page_len) + ' current: ' + str(page_len))

    async def _get_window_count_async(self):
        pages = await self.library_ctx.get_all_pages()
        for page in pages:
            # Workaround: for force pages re-cache
            try:
                await page.title()
            except:
                return -1
        return len(await self.library_ctx.get_all_pages())

    async def switch_window(self, locator='MAIN'):
        pages = await self.library_ctx.get_all_pages()
        if locator == 'MAIN':
            page = pages[0]
            await page.bringToFront()
            return self.library_ctx.set_current_page(page)

        elif locator == 'NEW':
            page = pages[-1]
            await page.bringToFront()
            return self.library_ctx.set_current_page(page)

        elif 'title=' in locator:
            title = locator.replace('title=', '')
            for page in pages:
                page_title = await page.title()
                if page_title == title:
                    await page.bringToFront()
                    return self.library_ctx.set_current_page(page)
                self.info('Title mismatch: ' + page_title)

        elif 'url=' in locator:
            url = locator.replace('url=', '')
            for page in pages:
                if re.match(url, page.url):
                    await page.bringToFront()
                    return self.library_ctx.set_current_page(page)
                self.info('Url mismatch: ' + page.url)
        else:
            raise Exception('Sorry Switch window support only NEW, MAIN, title and url')
        raise Exception('Can\'t find specify page locator.')

    ##############################
    # iFrame
    ##############################
    async def select_frame(self, locator: str):
        element = await self.library_ctx.get_current_page().querySelector_with_selenium_locator(locator) 
        iframe = await element.contentFrame()
        self.library_ctx.get_current_page().set_current_iframe(iframe)

    def unselect_iframe(self):
        self.library_ctx.get_current_page().unselect_iframe()
    
    ##############################
    # Cookies
    ##############################
    async def get_cookie(self, name: str):
        cookies = await self.get_cookies()
        return cookies[name]
    
    async def get_cookies(self):
        cookies = await self.library_ctx.get_current_page().get_page().cookies()
        pairs = {}
        for cookie in cookies:
            pairs[cookie["name"]] = cookie["value"]
        return pairs

    async def add_cookie(self, name: str, value: str):
        await self.library_ctx.get_current_page().get_page().setCookie({
            'name': name,
            'value': value,
        })

    async def delete_all_cookies(self):
        cookies = await self.library_ctx.get_current_page().get_page().cookies()
        for cookie in cookies:
            await self.library_ctx.get_current_page().get_page().deleteCookie(cookie)
