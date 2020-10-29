import asyncio
from PuppeteerLibrary.ikeywords.ialert_async import iAlertAsync


class PuppeteerAlert(iAlertAsync):

    def __init__(self, library_ctx):
        super().__init__(library_ctx)

    async def handle_alert(self, action, prompt_text=''):
        return self.library_ctx.get_current_page().get_page().on('dialog', lambda dialog: asyncio.ensure_future(self.handle_dialog(dialog, action, prompt_text)))

    async def handle_dialog(self, dialog, action, prompt_text=''):
        if action == 'ACCEPT':
            await dialog.accept(prompt_text)
        elif action == 'DISMISS':
            await dialog.dismiss()
