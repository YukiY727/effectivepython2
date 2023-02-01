import logging
import logging.config
from pythonic_thinking import check_python_version_by_sys

# logging.basicConfig(level=logging.WARNING, format='%(asctime)s:%(levelname)s:%(name)s:%(message)s:%(lineno)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.config.fileConfig('logconf.ini')

class NoPassFilter(logging.Filter):
    def filter(self, record):
        return "password" not in record.getMessage()

logger = logging.getLogger(__name__)
logger.addFilter(NoPassFilter())
# logger.warning("main.py")
logger.warning("password = hogehoge")
check_python_version_by_sys()
