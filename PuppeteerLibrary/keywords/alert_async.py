import asyncio

from PuppeteerLibrary.base.robotlibcore import keyword
from PuppeteerLibrary.base.librarycomponent import LibraryComponent


class AlertKeywordsAsync(LibraryComponent):

    @keyword
    async def handle_alert_async(self, action, prompt_text=''):
        return self.ctx.get_current_page().on('dialog', lambda dialog: asyncio.ensure_future(self.handle_dialog(dialog, action, prompt_text)))

    async def handle_dialog(self, dialog, action, prompt_text=''):
        if action == 'ACCEPT':
            await dialog.accept(prompt_text)
        elif action == 'DISMISS':
            await dialog.dismiss()
