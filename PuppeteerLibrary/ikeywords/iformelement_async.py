from abc import ABC, abstractmethod
from PuppeteerLibrary.ikeywords.base_async_keywords import BaseAsyncKeywords


class iFormElementAsync(BaseAsyncKeywords, ABC):
    
    @abstractmethod
    async def input_text(self, locator: str, text: str, clear=True):
        pass

    @abstractmethod
    async def input_password(self, locator: str, text: str, clear=True):
        pass
    
    @abstractmethod
    async def clear_element_text(self, locator: str):
        pass
    
    @abstractmethod
    async def download_file(self, locator: str, timeout=None):
        pass

    @abstractmethod
    async def upload_file(self, locator: str, file_path: str):
        pass
