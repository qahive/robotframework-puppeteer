from PuppeteerLibrary.ikeywords.ipdf_async import iPDFAsync, DEFAULT_FILENAME_PAGE


class PlaywrightPDF(iPDFAsync):

    def __init__(self, library_ctx):
        super().__init__(library_ctx)

    async def print_as_pdf(self, filename=DEFAULT_FILENAME_PAGE):
        path = self._get_pdf_path(filename)
        await self.library_ctx.get_current_page().get_page().emulateMedia('screen')
        await self.library_ctx.get_current_page().get_page().pdf(
            path=path
        )
        self.info('Print as pdf: '+path)
