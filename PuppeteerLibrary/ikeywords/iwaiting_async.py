from abc import ABC, abstractmethod
from PuppeteerLibrary.ikeywords.base_async_keywords import BaseAsyncKeywords


class iWaitingAsync(BaseAsyncKeywords, ABC):

    @abstractmethod
    async def wait_for_request_url(self, url, method='GET', body=None, timeout=None):
        pass

    @abstractmethod
    async def wait_for_response_url(self, url, status=200, body=None, timeout=None):
        pass

    @abstractmethod
    async def wait_for_navigation(self, timeout=None):
        pass

    @abstractmethod
    async def wait_until_page_contains_element(self, locator, timeout=None):
        pass

    @abstractmethod
    async def wait_until_element_is_hidden(self, locator, timeout=None):
        pass

    @abstractmethod
    async def wait_until_element_is_visible(self, locator, timeout=None):
        pass

    @abstractmethod
    async def wait_until_page_contains(self, text, timeout=None):
        pass

    @abstractmethod
    async def wait_until_page_does_not_contains(self, text, timeout=None):
        pass

    @abstractmethod
    async def wait_until_element_contains(self, locator, text, timeout=None):
        pass

    @abstractmethod
    async def wait_until_element_does_not_contains(self, locator, text, timeout=None):
        pass

    @abstractmethod
    async def wait_until_location_contains(self, expected, timeout=None):
        pass

    @abstractmethod
    async def wait_until_location_does_not_contains(self, expected, timeout=None):
        pass

    @abstractmethod
    async def wait_until_element_is_enabled(self, locator, timeout=None):
        pass

    @abstractmethod
    async def wait_until_element_finished_animating(self, locator, timeout=None):
        pass
