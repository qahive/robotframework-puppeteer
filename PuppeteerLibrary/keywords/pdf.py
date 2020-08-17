from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.base.robotlibcore import keyword
from PuppeteerLibrary.keywords.pdf_async import PDFKeywordsAsync, DEFAULT_FILENAME_PAGE


class PDFKeywords(LibraryComponent):

    def __init__(self, ctx):
        super().__init__(ctx)
        self.async_func = PDFKeywordsAsync(self.ctx)
    
    @keyword
    def print_as_pdf(self, filename=DEFAULT_FILENAME_PAGE):
        """
        Print current web page as pdf file. This keyword only support with ``HEADLESS`` mode enable.

        The ``filename`` argument specifies filename and path to save the file.
        Default valid is 'pdf-{index}.pdf'.

        Example:

        | &{options} =   | create dictionary                             | headless=${False}  |
        | Open browser   | https://www.w3schools.com/html/html_forms.asp | options=${options} |
        | Print as PDF   |                                               |                    |
        | Print as PDF   | custom-pdf-{index}.pdf                        |                    |

        """
        return self.loop.run_until_complete(self.async_func.print_as_pdf_async(filename))
