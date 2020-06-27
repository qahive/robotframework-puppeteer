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
            kw_name = kw.lower().replace(' ', '_') +'_async'
            statements.append(self.ctx.keywords[kw_name](*args))

        try:
            return await asyncio.gather(*statements)
        except Exception as err:
            raise Exception(err)
