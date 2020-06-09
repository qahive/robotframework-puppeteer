from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.base.robotlibcore import keyword


class BrowserManagementKeywords(LibraryComponent):

    @keyword
    def open_browser(self):
        print('')

    @keyword
    def close_all_browsers(self):
        print('')

    @keyword
    def close_browser(self):
        print('')

    @keyword
    def switch_browser(self, index_or_alias):
        print('')

    @keyword
    def get_source(self):
        print('')

    @keyword
    def get_title(self):
        print('')

    @keyword
    def get_location(self):
        print('')

    @keyword
    def go_back(self):
        print('')

    @keyword
    def go_to(self, url):
        print('')

    @keyword
    def reload_page(self):
        print('')
