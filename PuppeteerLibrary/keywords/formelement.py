from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.base.robotlibcore import keyword
from PuppeteerLibrary.keywords.formelement_async import FormElementKeywordsAsync


class FormElementKeywords(LibraryComponent):

    def __init__(self, ctx):
        super().__init__(ctx)
        self.async_func = FormElementKeywordsAsync(self.ctx)

    @keyword
    def input_text(self, locator, text, clear=True):
        """Types the given text into text field identified by ``locator``.

        If clear is true, the input element will be cleared before the text is typed into the element.
        On the other hand clear is false, the previous text will not be cleared from the element.

        Examples:
        | `Input Text` | id:name     | John Doe    |      |
        | `Input Text` | id:username | john        | True |

        """
        self.loop.run_until_complete(self.async_func.input_text_async(locator, text, clear))

    @keyword
    def clear_element_text(self, locator):
        """Clears value of text field identified by ``locator``.

        Example:

        | `Clear Element Text`                   | id:name          |
        """
        self.loop.run_until_complete(self.async_func.clear_element_text_async(locator))

