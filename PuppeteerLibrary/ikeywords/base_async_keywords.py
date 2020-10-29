from robot.api import logger
from robot.utils import timestr_to_secs
from PuppeteerLibrary.library_context.ilibrary_context import iLibraryContext


class BaseAsyncKeywords:

    def __init__(self, library_ctx: iLibraryContext):
        self.library_ctx = library_ctx

    def info(self, msg, html=False):
        logger.info(msg, html)

    def debug(self, msg, html=False):
        logger.debug(msg, html)

    def warn(self, msg, html=False):
        logger.warn(msg, html)

    def timestr_to_secs_for_default_timeout(self, timeout):
        if timeout is None or timeout == '':
            timeout = self.library_ctx.timeout
        return timestr_to_secs(timeout)
