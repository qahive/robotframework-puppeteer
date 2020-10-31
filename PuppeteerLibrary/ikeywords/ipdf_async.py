import os
from abc import ABC, abstractmethod
from PuppeteerLibrary.ikeywords.base_async_keywords import BaseAsyncKeywords

DEFAULT_FILENAME_PAGE = 'pdf-{index}.pdf'

class iPDFAsync(BaseAsyncKeywords, ABC):

    def __init__(self, library_ctx):
        super().__init__(library_ctx)
        self.log_dir = os.curdir
    
    @abstractmethod
    async def print_as_pdf(self, filename=DEFAULT_FILENAME_PAGE):
        pass
    
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
