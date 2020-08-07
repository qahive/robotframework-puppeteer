from PuppeteerLibrary.base.robotlibcore import keyword
from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.keywords.mockresponse_async import MockResponseKeywordsAsync


class MockResponseKeywords(LibraryComponent):

    def __init__(self, ctx):
        super().__init__(ctx)
        self.async_func = MockResponseKeywordsAsync(self.ctx)

    @keyword
    def mock_current_page_api_response(self, url, mock_response, method='GET', body=None):
        """
        Mock current page api response.

        The ``mock_response`` is a dictionary which can have the following fields:
        - ``status`` (int): Response status code, defaults to 200.
        - ``headers`` (dict): Optional response headers.
        - ``contentType`` (str): If set, equals to setting ``Content-Type`` response header.
        - ``body`` (str|bytes): Optional response body.

        The ``url`` is request url. url can be partial url match using regexp
        Match Options:

        | Options            | Url value                                        |
        | Exact match        | ^http://127.0.0.1:7272/ajax_info.json\\?count=3$ |
        | Partial match      | /ajax_info.json\\?count=3                        |
        | Regular expression | .*?/ajax_info.json\\?count=3                     |

        The ``method`` is HTTP Request Methods:
        - GET (default)
        - POST
        - PUT
        - HEAD
        - DELETE
        - PATCH

        The ``body`` is request body message. body can match using regexp

        Example:

        | &{response}                    | Create Dictionary          | body=I'm a mock response |
        | Mock Current Page Api Response | /ajax_info.json\\?count=3  | ${response}              |

        """
        return self.loop.run_until_complete(self.async_func.mock_current_page_api_response_async(url, mock_response, method, body))
