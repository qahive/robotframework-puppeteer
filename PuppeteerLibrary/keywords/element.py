from PuppeteerLibrary.base.robotlibcore import keyword
from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.ikeywords.ielement_async import iElementAsync


class ElementKeywords(LibraryComponent):

    def __init__(self, ctx):
        super().__init__(ctx)

    def get_async_keyword_group(self) -> iElementAsync:
        return self.ctx.get_current_library_context().get_async_keyword_group(type(self).__name__)

    ##############################
    # Action
    ##############################
    @keyword
    def click_element(self, locator, noWaitAfter='False'):
        """Clicks element identified by ``locator``.

        The ``noWaitAfter`` argument specifies skip wait for animation after click.
        Only support for webkit and safari (Puppeteer)

        Example:

        | `Click Element`         | id:register          |            |
        | `Click Element`         | id:register          | ${True}    |
        """
        self.info(f"Clicking element '{locator}'.")
        self.loop.run_until_complete(self.get_async_keyword_group().click_element(
            locator=locator, 
            noWaitAfter=noWaitAfter
        ))

    @keyword
    def click_link(self, locator):
        """Clicks link identified by ``locator``.

        Example:

        | `Click Link`                                  | id:view_more          |
        """
        self.info(f"Clicking link '{locator}'.")
        return self.loop.run_until_complete(self.get_async_keyword_group().click_link(locator))

    @keyword
    def click_button(self, locator):
        """Clicks button identified by ``locator``.

        Example:

        | `Click Button`                                | id:submit          |
        """
        self.info(f"Clicking button '{locator}'.")
        self.loop.run_until_complete(self.get_async_keyword_group().click_button(locator))

    @keyword
    def click_image(self, locator):
        """Clicks image identified by ``locator``.

        Example:

        | `Click Image`                                 | id:cat_image          |
        """
        self.info(f"Clicking image '{locator}'.")
        self.loop.run_until_complete(self.get_async_keyword_group().click_image(locator))

    @keyword
    def click_element_at_coordinate(self, locator, xoffset, yoffset):
        """ Click element at specifict coordiate x and y offset
        """
        self.info(f"Clicking element at coordinate '{locator}' at xoffset: '{xoffset}', yoffset: '{yoffset}'.")
        self.loop.run_until_complete(self.get_async_keyword_group().click_element_at_coordinate(locator, xoffset, yoffset))

    @keyword
    def upload_file(self, locator, file_path):
        """ Upload file
        """
        return self.loop.run_until_complete(self.get_async_keyword_group().upload_file(locator, file_path))

    @keyword    
    def press_keys(self, locator, *keys):
        """ Press Keys

        Simulates the user pressing key(s) to an element or on the active page. 
        A superset of the `key` values can be found here. Examples of the keys are:
        `F1` - `F12`, `Digit0`- `Digit9`, `KeyA`- `KeyZ`, `Backquote`, `Minus`, `Equal`, `Backslash`, `Backspace`, `Tab`, `Delete`, `Escape`, `ArrowDown`, `End`, `Enter`, `Home`, `Insert`, `PageDown`, `PageUp`, `ArrowRight`, `ArrowUp`, etc.
        Please refer to a key https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key/Key_Values

        keys arguments can contain one or many strings

        Example:

        | `Press Keys`        | None              | A        |       |
        | `Press Keys`        | id=password       | Enter    |       |
        | `Press Keys`        | id=password       | A        | Enter |
        """
        self.info(f"Sending key(s) {keys} to {locator} element.")
        return self.loop.run_until_complete(self.get_async_keyword_group().press_keys(locator, *keys))

    ##############################
    # Status
    ##############################
    @keyword
    def element_should_be_disabled(self, locator):
        """	Verifies that element identified by locator is disabled.

        """
        return self.loop.run_until_complete(self.get_async_keyword_group().element_should_be_disabled(locator))

    @keyword
    def element_should_be_enabled(self, locator):
        """	Verifies that element identified by locator is enabled.

        """
        return self.loop.run_until_complete(self.get_async_keyword_group().element_should_be_enabled(locator))

    @keyword
    def element_should_be_visible(self, locator):
        """ Verifies that element identified by locator is visible.

        """
        return self.loop.run_until_complete(self.get_async_keyword_group().element_should_be_visible(locator))

    @keyword
    def element_should_not_be_visible(self, locator):
        """ Verifies that element identified by locator is not be visible.

        """
        return self.loop.run_until_complete(self.get_async_keyword_group().element_should_not_be_visible(locator))


    ##############################
    # Property
    ##############################
    @keyword
    def get_text(self, locator):
        """Returns text value of element identified by ``locator``.

        Example:

        | ${text}                                    | `Get Text`          | id:username |
        """
        return self.loop.run_until_complete(self.get_async_keyword_group().get_text(locator))

    @keyword
    def get_value(self, locator):
        """Returns specific attribute value of element identified by ``locator``.

        Example:

        | ${value}                                    | `Get Value`          | id:comment |
        """
        return self.loop.run_until_complete(self.get_async_keyword_group().get_attribute(locator, "value"))

    @keyword
    def get_element_attribute(self, locator, attribute):
        """ Return the value of ``attribute`` from the element.
        """
        return self.loop.run_until_complete(self.get_async_keyword_group().get_attribute(locator, attribute))

    @keyword
    def element_should_contain(self, locator, expected, ignore_case=False):
        """ Verifies that element locator contains text `expected`.

        """
        return self.loop.run_until_complete(self.get_async_keyword_group().element_should_contain(locator, expected, ignore_case))

    @keyword
    def element_should_not_contain(self, locator, expected, ignore_case=False):
        """ Verifies that element locator should not contains text `expected`.

        """
        return self.loop.run_until_complete(self.get_async_keyword_group().element_should_not_contain(locator, expected, ignore_case))

    @keyword
    def element_text_should_be(self, locator, expected, ignore_case=False):
        """ Verifies that element locator contains exact the text `expected`.

        """
        return self.loop.run_until_complete(self.get_async_keyword_group().element_text_should_be(locator, expected, ignore_case))

    @keyword
    def element_text_should_not_be(self, locator, expected, ignore_case=False):
        """ Verifies that element locator not contains exact the text `expected`.

        """
        return self.loop.run_until_complete(self.get_async_keyword_group().element_text_should_not_be(locator, expected, ignore_case))

    ##############################
    # Query Element
    ##############################
    @keyword
    def get_element_count(self, locator):
        """ Returns the number of elements matching ``locator``.
        """
        return len(self.loop.run_until_complete(self.get_async_keyword_group().find_elements(locator)))

    ##############################
    # Scrolling
    ##############################
    @keyword
    def scroll_element_into_view(self, locator):
        """ Scroll element into view
        """
        return self.loop.run_until_complete(self.get_async_keyword_group().scroll_element_into_view(locator))
