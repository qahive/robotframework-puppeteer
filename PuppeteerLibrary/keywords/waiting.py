from PuppeteerLibrary.keywords.waiting_async import WaitingKeywordsAsync
from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.base.robotlibcore import keyword


class WaitingKeywords(LibraryComponent):

    def __init__(self, ctx):
        super().__init__(ctx)
        self.async_func = WaitingKeywordsAsync(self.ctx)

    @keyword
    def wait_for_request_url(self, url, method='GET', body=None, timeout=None):
        """
        Wait until web application sent request to ``url``.

        The ``url`` is request url. url can be partial url match using regexp
        Match Options:

        | Options            | Url value                              |
        | Exact match        | ^http://127.0.0.1:7272/ajax_info.json$ |
        | Partial match      | /ajax_info.json                        |
        | Regular expression | .*?/ajax_info.json                     |

        The ``method`` is HTTP Request Methods:
        - GET (default)
        - POST
        - PUT
        - HEAD
        - DELETE
        - PATCH

        The ``body`` is request body message. body can match using regexp

        Example:

        | Open browser       | ${HOME_PAGE_URL}       | options=${options}   |      |               |
        | Input Text         | id:username            | foo                  |      |               |
        | Input Text         | id:password            | bar                  |      |               |
        | Run Async Keywords | Click Element          | id:login_button      | AND  |               |
        | ...                | `Wait For Request Url` | ${URL_API}/login     | POST | username=demo |

        """
        return self.loop.run_until_complete(self.async_func.wait_for_request_url_async(url, method, body, timeout))

    @keyword
    def wait_for_response_url(self, url, status=200, body=None, timeout=None):
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
        Reference:[https://restfulapi.net/http-status-codes/|https://restfulapi.net/http-status-codes/]

        Example:

        | Open browser       | ${HOME_PAGE_URL}        | options=${options}          |      |               |
        | Input Text         | id:username             | foo                         |      |               |
        | Input Text         | id:password             | bar                         |      |               |
        | Run Async Keywords | Click Element           | id:login_button             | AND  |               |
        | ...                | `Wait For Response Url` | ${URL_API}/login            | 200  | username=demo |

        """
        return self.loop.run_until_complete(self.async_func.wait_for_response_url_async(url, status, body, timeout))

    @keyword
    def wait_for_navigation(self):
        """
        Waits until web page navigates to new url or reloads.

        Example:

        | Open browser       | ${HOME_PAGE_URL}        | options=${options}          |      |
        | Input Text         | id:username             | foo                         |      |
        | Input Text         | id:password             | bar                         |      |
        | Run Async Keywords | Click Element           | id:login_button             | AND  |
        | ...                | `Wait For Navigation`   |                             |      |
        """
        return self.loop.run_until_complete(self.async_func.wait_for_navigation_async())

    @keyword
    def wait_until_page_contains_element(self, locator, timeout=None):
        """
        Waits until ``locator`` element appears on current page.

        Example:

        | Open browser                       | ${HOME_PAGE_URL}        | options=${options} |
        | `Wait Until Page Contains Element` | id:username             |                    |
        """
        return self.loop.run_until_complete(self.async_func.wait_for_selenium_selector(locator, timeout))

    @keyword
    def wait_until_element_is_hidden(self, locator, timeout=None):
        """
        Waits until ``locator`` element is hide or removed from web page.

        Example:

        | Run Async Keywords                 | Click Element           | id:login_button             | AND  |
        | ...                                | Wait For Navigation     |                             |      |
        | `Wait Until Element Is Hidden`     | id:login_button         |                             |      |
        """
        return self.loop.run_until_complete(self.async_func.wait_until_element_is_hidden_async(locator, timeout))

    @keyword
    def wait_until_element_is_visible(self, locator, timeout=None):
        """
        Waits until ``locator`` element is displayed on web page.

        Example:

        | Run Async Keywords                 | Click Element           | id:login_button             | AND  |
        | ...                                | Wait For Navigation     |                             |      |
        | `Wait Until Element Is Visible`    | id:welcome              |                             |      |
        """
        return self.loop.run_until_complete(self.async_func.wait_until_element_is_visible_async(locator, timeout))

    @keyword
    def wait_until_page_contains(self, text, timeout=None):
        """
        Waits until ``text`` appears on current page.

        Example:

        | Run Async Keywords                 | Click Element                 | id:login_button             | AND  |
        | ...                                | Wait For Navigation           |                             |      |
        | `Wait Until Page Contains`         | Invalid user name or password |                             |      |
        """
        return self.loop.run_until_complete(self.async_func.wait_until_page_contains_async(text, timeout))

    @keyword
    def wait_until_page_does_not_contains(self, text, timeout=None):
        """
        Waits until ``text`` disappears on current page.

        Example:

        | Run Async Keywords                  | Click Element                 | id:login_button             | AND  |
        | ...                                 | Wait For Navigation           |                             |      |
        | `Wait Until Page Does Not Contains` | Please input your user name   |                             |      |
        """
        return self.loop.run_until_complete(self.async_func.wait_until_page_does_not_contains_async(text, timeout))

    @keyword
    def wait_until_element_contains(self, locator, text, timeout=None):
        """
        Waits until ``locator`` element contains ``text``.

        Example:

        | Open browser                       | ${HOME_PAGE_URL}        | options=${options}          |
        | `Wait Until Element Contains`      | css:#container p        | Please input your user name |
        """
        return self.loop.run_until_complete(self.async_func.wait_until_element_contains_async(locator, text, timeout))

    @keyword
    def wait_until_element_does_not_contains(self, locator, text, timeout=None):
        """
        Waits until ``locator`` element does not contains ``text``.

        Example:

        | Run Async Keywords                     | Click Element                 | id:login_button             | AND  |
        | ...                                    | Wait For Navigation           |                             |      |
        | `Wait Until Element Does Not Contains` | css:#container p              | Please input your user name |      |
        """
        return self.loop.run_until_complete(self.async_func.wait_until_element_does_not_contains_async(locator, text, timeout))

    @keyword
    def wait_until_location_contains(self, expected, timeout=None):
        """
        Waits until the current URL contains `expected`.

        The `expected` argument contains the expected value in url.
        """
        return self.loop.run_until_complete(self.async_func.wait_until_location_contains_async(expected, timeout))

    @keyword
    def wait_until_location_does_not_contains(self, expected, timeout=None):
        """
        Waits until the current URL does not contains `expected`.

        The `expected` argument contains the expected value must not in url.
        """
        return self.loop.run_until_complete(self.async_func.wait_until_location_does_not_contains_async(expected, timeout))
