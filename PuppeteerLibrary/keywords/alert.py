from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.base.robotlibcore import keyword
from PuppeteerLibrary.keywords.alert_async import AlertKeywordsAsync
from PuppeteerLibrary.keywords.ialert_async import iAlertAsync


class AlertKeywords(LibraryComponent):

    def __init__(self, ctx):
        super().__init__(ctx)
        self.async_func = AlertKeywordsAsync(self.ctx)

    def get_async_keyword_group(self) -> iAlertAsync:
        return self.ctx.get_current_library_context().get_async_keyword_group(type(self).__name__)

    @keyword
    def handle_alert(self, action, prompt_text=''):
        """Handles the current alert and returns its message.

        action:
        - ACCEPT: Accept the alert i.e. press Ok. Default.
        - DISMISS: Dismiss the alert i.e. press Cancel.`.

        Example:

        | `Run Async Keywords` |                  |     |
        | ...    Handle Alert  | ACCEPT           | AND |
        | ...    Click Button  | id=alert_confirm |     |

        """
        return self.loop.run_until_complete(self.get_async_keyword_group().handle_alert(action, prompt_text))
