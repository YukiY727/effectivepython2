# Standard Library
import logging
import logging.config

# Third Party Library
from list_and_dict import generate_csv, not_good_generator_catch_all
from pythonic_thinking import check_python_version_by_sys, hogehoge

# logging.basicConfig(level=logging.WARNING, format='%(asctime)s:%(levelname)s:%(name)s:%(message)s:%(lineno)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.config.fileConfig("logconf.ini")

not_good_generator_catch_all()


# check_python_version_by_sys()
class NoPassFilter(logging.Filter):
    def filter(self, record):
        return "password" not in record.getMessage()


logger = logging.getLogger(__name__)
# logger.addFilter(NoPassFilter())
# logger.warning("main.py")
# logger.warning("password = hogehoge")
# hogehoge()
