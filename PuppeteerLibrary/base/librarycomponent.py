from robot.api import logger
from PuppeteerLibrary.base.context import ContextAware


class LibraryComponent(ContextAware):

    def info(self, msg, html=False):
        logger.info(msg, html)

    def debug(self, msg, html=False):
        logger.debug(msg, html)

    def warn(self, msg, html=False):
        logger.warn(msg, html)

