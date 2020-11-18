import asyncio
from robot.utils import timestr_to_secs
from robot.libraries.BuiltIn import _RunKeyword
from PuppeteerLibrary.keywords.browsermanagement import BrowserManagementKeywords
from PuppeteerLibrary.playwright.async_keywords.playwright_browsermanagement import PlaywrightBrowserManagement
from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.base.robotlibcore import keyword


class UtilityKeywords(LibraryComponent):

    def __init__(self, ctx):
        super().__init__(ctx)

    @keyword
    def set_timeout(self, timeout):
        """Sets the timeout that is used by various keywords.
        The value can be given as a number that is considered to be seconds or as a human-readable string like 1 second.
        The previous value is returned and can be used to restore the original value later if needed.
        See the Timeout section above for more information.

        Example:
        
        | Open page that loads slowly |	                 |            |
        | Set Timeout	              | ${orig timeout}	 |            |

        """
        orig_timeout = self.ctx.timeout
        self.ctx.get_current_library_context().timeout = timestr_to_secs(timeout)
        self.info('Original timeout is ' + str(orig_timeout) + ' seconds')
        return orig_timeout

    @keyword
    def run_async_keywords_and_return_first_completed(self, *keywords):
        """Executes all the given keywords in a asynchronous and wait until first keyword is completed
        
        ``Return`` Array of result for each keywords based on index

        Example
        | `Run Async Keywords And Return First Completed` | Wait for response url | ${HOME_PAGE_URL}/login.html | AND  |
        | ...                                             | Wait for response url | ${HOME_PAGE_URL}/home.html  |      |
        """
        run_keyword = _RunKeyword()
        return self.loop.run_until_complete( self._run_async_keywords_first_completed(run_keyword._split_run_keywords(list(keywords))) )

    async def _run_async_keywords_first_completed(self, iterable):
        org_statements = []
        index = 0
        for kw, args in iterable:
            kw_name = kw.lower().replace(' ', '_')
            async_keywords = self.ctx.keywords[kw_name].__self__.get_async_keyword_group()
            org_statements.append(self._wrapped_async_keyword_return_index(index, getattr(async_keywords, kw_name)(*args) ))
            index += 1
        statements = org_statements
        error_stack_trace = ''
        while True:
            done, pending = await asyncio.wait(statements, return_when=asyncio.FIRST_COMPLETED)
            statements = pending
            for future in done:
                try:
                    # Raise an exception if coroutine failed
                    result_index = future.result()
                    # Force cancel all pending
                    for p in pending:
                        p.cancel()
                    return result_index
                except Exception as e:
                    error_stack_trace += str(e)+'\n'
                    continue
            if len(pending) == 0:
                raise Exception("All async keywords failed \r\n"+ error_stack_trace)

    async def _wrapped_async_keyword_return_index(self, index, future):
        await future
        return index

    @keyword
    def run_async_keywords(self, *keywords):
        """Executes all the given keywords in a asynchronous and wait until all keyword is completed

        ``Return`` Array of result for each keywords based on index

        Example:
        | Open browser         | ${HOME_PAGE_URL}      | options=${options}          |     |
        | `Run Async Keywords` | Click Element         | id:login_button             | AND |
        | ...                  | Wait for response url | ${HOME_PAGE_URL}/home.html  |     |

        """
        run_keyword = _RunKeyword()
        return self.loop.run_until_complete( self._new_run_async_keywords(run_keyword._split_run_keywords(list(keywords))) )

    async def _new_run_async_keywords(self, iterable):        
        statements = []
        for kw, args in iterable:
            kw_name = kw.lower().replace(' ', '_')
            async_keywords = self.ctx.keywords[kw_name].__self__.get_async_keyword_group()
            statements.append(getattr(async_keywords, kw_name)(*args))
        try:
            return await asyncio.gather(*statements)
        except Exception as err:
            raise Exception(err)

    async def _run_async_keywords(self, iterable):
        statements = []
        for kw, args in iterable:
            kw_name = kw.lower()
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

