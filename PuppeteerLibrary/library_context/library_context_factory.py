from .ilibrary_context import iLibraryContext
from PuppeteerLibrary.puppeteer.puppeteer_context import PuppeteerContext
from PuppeteerLibrary.playwright.playwright_context import PlaywrightContext

class LibraryContextFactory:

    def create(self, browser_type: str) -> iLibraryContext:
        """Return iLibraryContext based on specific browser_type

        Create context based on browser type (chrome, safari, webkit)
        """
        if browser_type.lower() == 'chrome':
            return PuppeteerContext(browser_type)
        elif browser_type.lower() == 'safari':
            return PlaywrightContext(browser_type)
        elif browser_type.lower() == 'webkit':
            return PlaywrightContext(browser_type)
        elif browser_type.lower() == 'firefox':
            return PlaywrightContext(browser_type)    
        else:
            raise Exception('Sorry, not supported for library type '+str(browser_type)+'.')
