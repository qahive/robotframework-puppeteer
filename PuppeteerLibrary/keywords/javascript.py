from PuppeteerLibrary.base.robotlibcore import keyword
from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.ikeywords.ijavascript_async import iJavascriptAsync


class JavascriptKeywords(LibraryComponent):

    def __init__(self, ctx):
        super().__init__(ctx)

    def get_async_keyword_group(self) -> iJavascriptAsync:
        return self.ctx.get_current_library_context().get_async_keyword_group(type(self).__name__)

    @keyword
    def execute_javascript(self, code):
        """Executes the given JavaScript code

        Examples:
        | `Handle Alert`       | ACCEPT                |
        | `Execute Javascript` | alert('Hello world'); |


        Examples:
        | `Execute Javascript` | console.log('Hi 5');  |

        """
        return self.loop.run_until_complete(self.get_async_keyword_group().execute_javascript(code))
