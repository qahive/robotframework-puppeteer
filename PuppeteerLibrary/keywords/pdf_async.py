from PuppeteerLibrary.base.robotlibcore import keyword
from PuppeteerLibrary.base.librarycomponent import LibraryComponent


class PDFKeywordsAsync(LibraryComponent):

    def __init__(self, ctx):
        self.ctx = ctx
    
    @keyword
    async def print_as_pdf_async(self):
        await self.ctx.current_page.emulateMedia('screen')
        await self.ctx.current_page.pdf({'path': 'page.pdf'})
