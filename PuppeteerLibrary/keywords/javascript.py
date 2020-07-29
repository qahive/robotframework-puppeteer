from PuppeteerLibrary.base.robotlibcore import keyword
from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.keywords.javascript_async import JavascriptKeywordsAsync


class JavascriptKeywords(LibraryComponent):

    def __init__(self, ctx):
        super().__init__(ctx)
        self.async_func = JavascriptKeywordsAsync(self.ctx)

    @keyword
    def execute_javascript(self, code):
        """Executes the given JavaScript code

        Examples:
        | `Handle Alert`       | ACCEPT                |
        | `Execute Javascript` | alert('Hello world'); |


        Examples:
        | `Execute Javascript` | console.log('Hi 5');  |

        """
        return self.loop.run_until_complete(self.async_func.execute_javascript_async(code))
