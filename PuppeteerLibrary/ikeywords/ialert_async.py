from PuppeteerLibrary.ikeywords.base_async_keywords import BaseAsyncKeywords
from abc import ABC, abstractmethod


class iAlertAsync(BaseAsyncKeywords, ABC):

    @abstractmethod
    async def handle_alert(self, action, prompt_text=''):
        pass
