from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.base.robotlibcore import keyword
from PuppeteerLibrary.keywords.pdf_async import PDFKeywordsAsync


class PDFKeywords(LibraryComponent):

    def __init__(self, ctx):
        super().__init__(ctx)
        self.async_func = PDFKeywordsAsync(self.ctx)
    
    @keyword
    def print_as_pdf(self):
        return self.loop.run_until_complete(self.async_func.print_as_pdf_async())
