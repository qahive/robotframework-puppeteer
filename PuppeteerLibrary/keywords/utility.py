import asyncio
from robot.libraries.BuiltIn import _RunKeyword
from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.base.robotlibcore import keyword


class UtilityKeywords(LibraryComponent):

    @keyword
    def run_async_keywords(self, *keywords):
        # Ensure that script load async keywords before run async keywords function
        """Executes all the given keywords in a asynchronous and wait until all keyword is completed

        Example:

        | Open browser         | ${HOME_PAGE_URL}      | options=${options}          |     |
        | `Run Async Keywords` | Click Element         | id:login_button             | AND |
        | ...                  | Wait for response url | ${HOME_PAGE_URL}/home.html  |     |

        """
        self.ctx.load_async_keywords()
        run_keyword = _RunKeyword()
        self.loop.run_until_complete( self._run_async_keywords(run_keyword._split_run_keywords(list(keywords))) )

    async def _run_async_keywords(self, iterable):
        statements = []
        for kw, args in iterable:
            kw_name = kw.lower().replace(' ', '_') + '_async'
            statements.append(self.ctx.keywords[kw_name](*args))

        try:
            return await asyncio.gather(*statements)
        except Exception as err:
            raise Exception(err)

    @keyword
    def enable_debug_mode(self, slowMo=150, devtools=True):
        """Enable debug mode.

        The ``slowMo`` argument specifies delay for each test step.
        The ``devtools`` argument specifies enable devtools or not.

        Example:

        | Enable Debug Mode |                       |      |
        | Open browser      | http://127.0.0.1:7272 |      |
        | Input text        | id:username_field     | demo |
        | Input text        | id:password_field     | mode |

        """
        self.ctx.debug_mode = True
        self.ctx.debug_mode_options['headless'] = False
        self.ctx.debug_mode_options['slowMo'] = slowMo
        self.ctx.debug_mode_options['devtools'] = devtools

    @keyword
    def disable_debug_mode(self):
        """Disable debug mode. This keyword will close all browser and reset debug mode to False.
        """
        async def disable_debug_mode_async():
            await self.ctx.browser.close()

        self.loop.run_until_complete(disable_debug_mode_async())
        self.ctx.debug_mode = False
        self.ctx.clear_browser()

