from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.base.robotlibcore import keyword
from PuppeteerLibrary.keywords.element_async import ElementKeywordsAsync


class ElementKeywords(LibraryComponent):

    def __init__(self, ctx):
        super().__init__(ctx)
        self.async_func = ElementKeywordsAsync(self.ctx)

    @keyword
    def click_element(self, locator):
        """Clicks element identified by ``locator``.

        Example:

        | `Click Element`                                  | id:register          |
        """
        return self.loop.run_until_complete(self.async_func.click_element_async(locator))

    @keyword
    def click_link(self, locator):
        """Clicks link identified by ``locator``.

        Example:

        | `Click Link`                                  | id:view_more          |
        """
        return self.loop.run_until_complete(self.async_func.click_link_async(locator))

    @keyword
    def click_button(self, locator):
        """Clicks button identified by ``locator``.

        Example:

        | `Click Button`                                | id:submit          |
        """
        self.loop.run_until_complete(self.async_func.click_button_async(locator))

    @keyword
    def click_image(self, locator):
        """Clicks image identified by ``locator``.

        Example:

        | `Click Image`                                 | id:cat_image          |
        """
        self.loop.run_until_complete(self.async_func.click_image_async(locator))

    @keyword
    def get_text(self, locator):
        """Returns text value of element identified by ``locator``.

        Example:

        | ${text}                                    | `Get Text`          | id:username |
        """
        return self.loop.run_until_complete(self.async_func.get_text_async(locator))

    @keyword
    def get_value(self, locator):
        """Returns specific attribute value of element identified by ``locator``.

        Example:

        | ${value}                                    | `Get Value`          | id:comment |
        """
        return self.loop.run_until_complete(self.async_func.get_text_async(locator))

    @keyword
    def element_should_be_disabled(self, locator):
        """	Verifies that element identified by locator is disabled.

        """
        return self.loop.run_until_complete(self.async_func.element_should_be_disabled_async(locator))

    @keyword
    def element_should_be_enabled(self, locator):
        """	Verifies that element identified by locator is enabled.

        """
        return self.loop.run_until_complete(self.async_func.element_should_be_enabled_async(locator))

    @keyword
    def element_should_be_visible(self, locator):
        """ Verifies that element identified by locator is visible.

        """
        return self.loop.run_until_complete(self.async_func.element_should_be_visible_async(locator))

    @keyword
    def element_should_not_be_visible(self, locator):
        """ Verifies that element identified by locator is not be visible.

        """
        return self.loop.run_until_complete(self.async_func.element_should_not_be_visible_async(locator))

    @keyword
    def element_should_contain(self, locator, expected, ignore_case=False):
        """ Verifies that element locator contains text `expected`.

        """
        return self.loop.run_until_complete(self.async_func.element_should_contain_async(locator, expected, ignore_case))

    @keyword
    def element_should_not_contain(self, locator, expected, ignore_case=False):
        """ Verifies that element locator should not contains text `expected`.

        """
        return self.loop.run_until_complete(self.async_func.element_should_not_contain_async(locator, expected, ignore_case))

    @keyword
    def element_text_should_be(self, locator, expected, ignore_case=False):
        """ Verifies that element locator contains exact the text `expected`.

        """
        return self.loop.run_until_complete(self.async_func.element_text_should_be_async(locator, expected, ignore_case))

    @keyword
    def element_text_should_not_be(self, locator, expected, ignore_case=False):
        """ Verifies that element locator not contains exact the text `expected`.

        """
        return self.loop.run_until_complete(self.async_func.element_text_should_not_be_async(locator, expected, ignore_case))

    @keyword
    def upload_file(self, locator, file_path):
        """ Upload file
        """
        return self.loop.run_until_complete(self.async_func.upload_file_async(locator, file_path))
