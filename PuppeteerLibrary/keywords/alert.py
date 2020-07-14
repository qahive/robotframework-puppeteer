from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.base.robotlibcore import keyword
from PuppeteerLibrary.keywords.alert_async import AlertKeywordsAsync


class AlertKeywords(LibraryComponent):

    def __init__(self, ctx):
        self.ctx = ctx
        self.async_func = AlertKeywordsAsync(self.ctx)

    @keyword
    def handle_alert(self, action, prompt_text=''):
        """Clicks element identified by ``locator``.

        Example:

        | `Click Element`                                  | id:register          |
        """
        return self.loop.run_until_complete(self.async_func.handle_alert_async(action, prompt_text))
