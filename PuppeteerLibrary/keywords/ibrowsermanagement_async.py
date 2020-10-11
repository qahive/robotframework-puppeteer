from abc import ABC, abstractmethod
from PuppeteerLibrary.base.librarycomponent import LibraryComponent


class iBrowserManagementAsync(LibraryComponent, ABC):

    @abstractmethod
    async def go_to(self, url):
        pass
