import abc
from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.base.robotlibcore import keyword


class iBrowserManagementAsync(LibraryComponent):

    @keyword
    @abc.abstractmethod
    async def open_browser_async(self, url, browser="chrome", alias=None, options=None):
        pass

    @keyword
    @abc.abstractmethod
    async def close_browser_async(self, alias=None):
        pass

    @keyword
    @abc.abstractmethod
    async def close_all_browser_async(self):
        pass

    @keyword
    @abc.abstractmethod
    async def close_puppeteer_async(self):
        pass
