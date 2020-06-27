from PuppeteerLibrary.keywords.waiting_async import WaitingKeywordsAsync
from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.base.robotlibcore import keyword


class WaitingKeywords(LibraryComponent):

    def __init__(self, ctx):
        self.ctx = ctx
        self.async_func = WaitingKeywordsAsync(self.ctx)

    @keyword
    def wait_for_request_url(self, url, method='GET', timeout=None):
        """
        Wait until web application sent request to ``url``.

		The ``url`` is request url.

        The ``method`` is HTTP Request Methods:
        - GET (default)
        - POST
        - PUT
        - HEAD
        - DELETE
        - PATCH

        Example:

        | Open browser       | ${HOME_PAGE_URL}      | options=${options}          |      |
        | Input Text         | id:username           | foo                         |      |
        | Input Text         | id:password           | bar                         |      |
        | Run Async Keywords | Click Element         | id:login_button             | AND  |
        | ...                | `Wait For Request Url`| ${HOME_PAGE_URL-API}/login  | POST |

		"""
        return self.loop.run_until_complete(self.async_func.wait_for_request_url_async(url, method , timeout))

    @keyword
    def wait_for_response_url(self, url, status=200, timeout=None):
        """
        Wait until web application received response from ``url``.

		The ``url`` is response url.

        The ``status`` is HTTP Status Codes:
        - 200 (default)
        - 201
        - 204
        - 400
        - 401
		- 404
		- 500
        Referernce: `https://restfulapi.net/http-status-codes/`

        Example:

        | Open browser       | ${HOME_PAGE_URL}       | options=${options}          |      |
        | Input Text         | id:username            | foo                         |      |
        | Input Text         | id:password            | bar                         |      |
        | Run Async Keywords | Click Element          | id:login_button             | AND  |
        | ...                | `Wait For Response Url`| ${HOME_PAGE_URL-API}/login  | 200  |

		"""
        return self.loop.run_until_complete(self.async_func.wait_for_response_url_async(url, status, timeout))

    @keyword
    def wait_for_function(self, page_function):
        """Wait for page trigger function"""
        return self.loop.run_until_complete(self.async_func.wait_for_function_async(page_function))

    @keyword
    def wait_for_navigation(self):
        """Wait for navigation from any redirect"""
        return self.loop.run_until_complete(self.async_func.wait_for_navigation_async())

    @keyword
    def wait_until_page_contains_element(self, locator, timeout=None):
        """Wait until page contains element within specific timeout"""
        return self.loop.run_until_complete(self.async_func.wait_for_selenium_selector(locator, timeout))

    @keyword
    def wait_until_element_is_hidden(self, locator, timeout=None):
        return self.loop.run_until_complete(self.async_func.wait_until_element_is_hidden_async(locator, timeout))

    @keyword
    def wait_until_element_is_visible(self, locator, timeout=None):
        return self.loop.run_until_complete(self.async_func.wait_until_element_is_visible_async(locator, timeout))

    @keyword
    def wait_until_page_contains(self, text, timeout=None):
        """Waits until ``text`` appears on the current page"""
        return self.loop.run_until_complete(self.async_func.wait_until_page_contains_async(text, timeout))

    @keyword
    def wait_until_page_does_not_contains(self, text, timeout=None):
        """Waits until ``text`` appears on the current page"""
        return self.loop.run_until_complete(self.async_func.wait_until_page_does_not_contains_async(text, timeout))

    @keyword
    def wait_until_element_contains(self, locator, text, timeout=None):
        """Waits until the ``element`` contains ``text``."""
        return self.loop.run_until_complete(self.async_func.wait_until_element_contains_async(locator, text, timeout))

    @keyword
    def wait_until_element_does_not_contains(self, locator, text, timeout=None):
        """Waits until the ``element`` does not contains ``text``."""
        return self.loop.run_until_complete(self.async_func.wait_until_element_does_not_contains_async(locator, text, timeout))

