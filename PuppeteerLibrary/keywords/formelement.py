import asyncio
from PuppeteerLibrary.base.robotlibcore import keyword
from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.ikeywords.iformelement_async import iFormElementAsync


class FormElementKeywords(LibraryComponent):

    def __init__(self, ctx):
        super().__init__(ctx)

    def get_async_keyword_group(self) -> iFormElementAsync:
        return self.ctx.get_current_library_context().get_async_keyword_group(type(self).__name__)

    @keyword
    def input_text(self, locator, text, clear=True):
        """Types the given text into text field identified by ``locator``.

        If clear is true, the input element will be cleared before the text is typed into the element.
        On the other hand clear is false, the previous text will not be cleared from the element.

        Examples:
        | `Input Text` | id:name     | John Doe    |      |
        | `Input Text` | id:username | john        | True |

        """
        self.info(f"Typing text '{text}' into text field '{locator}'.")
        self.loop.run_until_complete(self.get_async_keyword_group().input_text(locator, text, clear))

    @keyword
    def input_password(self, locator, text, clear=True):
        """Types the given text into text field same as ``Input Text`` Keyword.

        Differentiate is only not log the input value into log file. 
        """
        self.info(f"Typing password into text field '{locator}'.")
        self.loop.run_until_complete(self.get_async_keyword_group().input_password(locator, text, clear))
        
    @keyword
    def clear_element_text(self, locator):
        """Clears value of text field identified by ``locator``.

        Example:

        | `Clear Element Text`                   | id:name          |
        """
        self.loop.run_until_complete(self.get_async_keyword_group().clear_element_text(locator))

    @keyword
    def download_file(self, locator, timeout=None):
        return self.loop.run_until_complete(self.get_async_keyword_group().download_file(locator, timeout))

    @keyword
    def upload_file(self, locator, file_path):
        return self.loop.run_until_complete(self.get_async_keyword_group().upload_file(locator, file_path))
