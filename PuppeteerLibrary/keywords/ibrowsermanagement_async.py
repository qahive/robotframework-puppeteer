from abc import ABC, abstractmethod
from PuppeteerLibrary.base.librarycomponent import LibraryComponent


class iBrowserManagementAsync(LibraryComponent, ABC):

    @abstractmethod
    async def open_browser_async(self, url, browser="chrome", alias=None, options=None):
        pass

    @abstractmethod
    async def close_browser_async(self, alias=None):
        pass

    @abstractmethod
    async def close_all_browser_async(self):
        pass

    @abstractmethod
    async def close_puppeteer_async(self):
        pass
