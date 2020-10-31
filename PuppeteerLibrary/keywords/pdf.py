from PuppeteerLibrary.ikeywords.ipdf_async import iPDFAsync, DEFAULT_FILENAME_PAGE
from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.base.robotlibcore import keyword

class PDFKeywords(LibraryComponent):

    def __init__(self, ctx):
        super().__init__(ctx)
    
    def get_async_keyword_group(self) -> iPDFAsync:
        return self.ctx.get_current_library_context().get_async_keyword_group(type(self).__name__)

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
        return self.loop.run_until_complete(self.get_async_keyword_group().print_as_pdf(filename))
