import asyncio
from PuppeteerLibrary.ikeywords.ialert_async import iAlertAsync


class PlaywrightAlert(iAlertAsync):

    def __init__(self, library_ctx):
        super().__init__(library_ctx)

    async def handle_alert(self, action, prompt_text=''):
        pass
