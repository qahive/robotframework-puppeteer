from PuppeteerLibrary.base.robotlibcore import keyword
from PuppeteerLibrary.ikeywords.iwaiting_async import iWaitingAsync
from PuppeteerLibrary.base.librarycomponent import LibraryComponent


class WaitingKeywords(LibraryComponent):

    def __init__(self, ctx):
        super().__init__(ctx)

    def get_async_keyword_group(self) -> iWaitingAsync:
        return self.ctx.get_current_library_context().get_async_keyword_group(type(self).__name__)

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

        ``Return`` request msg  with properties {url, method, body}

        Example:

        | Open browser       | ${HOME_PAGE_URL}       | options=${options}   |      |               |
        | Input Text         | id:username            | foo                  |      |               |
        | Input Text         | id:password            | bar                  |      |               |
        | Run Async Keywords | Click Element          | id:login_button      | AND  |               |
        | ...                | `Wait For Request Url` | ${URL_API}/login     | POST | username=demo |

        """
        return self.loop.run_until_complete(self.get_async_keyword_group().wait_for_request_url(url, method, body, timeout))

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

        ``Return`` request msg  with properties {url, status, body}

        Example:

        | Open browser       | ${HOME_PAGE_URL}        | options=${options}          |      |               |
        | Input Text         | id:username             | foo                         |      |               |
        | Input Text         | id:password             | bar                         |      |               |
        | Run Async Keywords | Click Element           | id:login_button             | AND  |               |
        | ...                | `Wait For Response Url` | ${URL_API}/login            | 200  | username=demo |

        """
        return self.loop.run_until_complete(self.get_async_keyword_group().wait_for_response_url(url, status, body, timeout))

    @keyword
    def wait_for_navigation(self, timeout=None):
        """
        Waits until web page navigates to new url or reloads.

        Example:

        | Open browser       | ${HOME_PAGE_URL}        | options=${options}          |      |
        | Input Text         | id:username             | foo                         |      |
        | Input Text         | id:password             | bar                         |      |
        | Run Async Keywords | Click Element           | id:login_button             | AND  |
        | ...                | `Wait For Navigation`   |                             |      |
        """
        return self.loop.run_until_complete(self.get_async_keyword_group().wait_for_navigation(timeout))

    @keyword
    def wait_until_page_contains_element(self, locator, timeout=None):
        """
        Waits until ``locator`` element appears on current page.

        Example:

        | Open browser                       | ${HOME_PAGE_URL}        | options=${options} |
        | `Wait Until Page Contains Element` | id:username             |                    |
        """
        self.loop.run_until_complete(self.get_async_keyword_group().wait_until_page_contains_element(locator, timeout))

    @keyword
    def wait_until_element_is_hidden(self, locator, timeout=None):
        """
        Waits until ``locator`` element is hide or removed from web page.

        Example:

        | Run Async Keywords                 | Click Element           | id:login_button             | AND  |
        | ...                                | Wait For Navigation     |                             |      |
        | `Wait Until Element Is Hidden`     | id:login_button         |                             |      |
        """
        return self.loop.run_until_complete(self.get_async_keyword_group().wait_until_element_is_hidden(locator, timeout))

    @keyword
    def wait_until_element_is_visible(self, locator, timeout=None):
        """
        Waits until ``locator`` element is displayed on web page.

        Example:

        | Run Async Keywords                 | Click Element           | id:login_button             | AND  |
        | ...                                | Wait For Navigation     |                             |      |
        | `Wait Until Element Is Visible`    | id:welcome              |                             |      |
        """
        return self.loop.run_until_complete(self.get_async_keyword_group().wait_until_element_is_visible(locator, timeout))

    @keyword
    def wait_until_page_contains(self, text, timeout=None):
        """
        Waits until ``text`` appears on current page.

        Example:

        | Run Async Keywords                 | Click Element                 | id:login_button             | AND  |
        | ...                                | Wait For Navigation           |                             |      |
        | `Wait Until Page Contains`         | Invalid user name or password |                             |      |
        """
        self.loop.run_until_complete(self.get_async_keyword_group().wait_until_page_contains(text, timeout))

    @keyword
    def wait_until_page_does_not_contains(self, text, timeout=None):
        """
        Waits until ``text`` disappears on current page.

        Example:

        | Run Async Keywords                  | Click Element                 | id:login_button             | AND  |
        | ...                                 | Wait For Navigation           |                             |      |
        | `Wait Until Page Does Not Contains` | Please input your user name   |                             |      |
        """
        return self.loop.run_until_complete(self.get_async_keyword_group().wait_until_page_does_not_contains(text, timeout))

    @keyword
    def wait_until_element_contains(self, locator, text, timeout=None):
        """
        Waits until ``locator`` element contains ``text``.

        Example:

        | Open browser                       | ${HOME_PAGE_URL}        | options=${options}          |
        | `Wait Until Element Contains`      | css:#container p        | Please input your user name |
        """
        return self.loop.run_until_complete(self.get_async_keyword_group().wait_until_element_contains(locator, text, timeout))

    @keyword
    def wait_until_element_does_not_contains(self, locator, text, timeout=None):
        """
        Waits until ``locator`` element does not contains ``text``.

        Example:

        | Run Async Keywords                     | Click Element                 | id:login_button             | AND  |
        | ...                                    | Wait For Navigation           |                             |      |
        | `Wait Until Element Does Not Contains` | css:#container p              | Please input your user name |      |
        """
        return self.loop.run_until_complete(self.get_async_keyword_group().wait_until_element_does_not_contains(locator, text, timeout))

    @keyword
    def wait_until_location_contains(self, expected, timeout=None):
        """
        Waits until the current URL contains `expected`.

        The `expected` argument contains the expected value in url.
        """
        return self.loop.run_until_complete(self.get_async_keyword_group().wait_until_location_contains(expected, timeout))

    @keyword
    def wait_until_location_does_not_contains(self, expected, timeout=None):
        """
        Waits until the current URL does not contains `expected`.

        The `expected` argument contains the expected value must not in url.
        """
        return self.loop.run_until_complete(self.get_async_keyword_group().wait_until_location_does_not_contains(expected, timeout))

    @keyword
    def wait_until_element_is_enabled(self, selenium_locator, timeout=None):
        """
        Waits until the specific element is Enabled.

        """
        return self.loop.run_until_complete(self.get_async_keyword_group().wait_until_element_is_enabled(selenium_locator, timeout))

    @keyword
    def wait_until_element_finished_animating(self, selenium_locator, timeout=None):
        """
        Waits until the specific element is finished animating.
        Check by check element position.

        """
        return self.loop.run_until_complete(self.get_async_keyword_group().wait_until_element_finished_animating(selenium_locator, timeout))
