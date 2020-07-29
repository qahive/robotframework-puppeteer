from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.base.robotlibcore import keyword
from PuppeteerLibrary.keywords.alert_async import AlertKeywordsAsync


class AlertKeywords(LibraryComponent):

    def __init__(self, ctx):
        super().__init__(ctx)
        self.async_func = AlertKeywordsAsync(self.ctx)

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
        return self.loop.run_until_complete(self.async_func.handle_alert_async(action, prompt_text))
