import os
from PuppeteerLibrary.base.robotlibcore import keyword
from PuppeteerLibrary.base.librarycomponent import LibraryComponent


DEFAULT_FILENAME_PAGE = 'pdf-{index}.pdf'

class PDFKeywordsAsync(LibraryComponent):

    def __init__(self, ctx):
        self.ctx = ctx
        self.log_dir = os.curdir
    
    @keyword
    async def print_as_pdf_async(self, filename):
        path = self._get_pdf_path(filename)
        await self.ctx.current_page.emulateMedia('screen')
        await self.ctx.current_page.pdf({'path': path})
        self.info('Print as pdf: '+path)

    def _get_pdf_path(self, filename):
        directory = self.log_dir
        filename = filename.replace('/', os.sep)
        index = 0
        while True:
            index += 1
            formatted = self._format_path(filename, index)
            path = os.path.join(directory, formatted)
            if formatted == filename or not os.path.exists(path):
                return path

    def _format_path(self, file_path, index):
        return file_path.format_map(_SafeFormatter(index=index))

class _SafeFormatter(dict):

    def __missing__(self, key):
        return '{%s}' % key
