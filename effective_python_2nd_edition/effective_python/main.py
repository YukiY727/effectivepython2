# Standard Library
import logging
import logging.config

# Third Party Library
from list_and_dict import generate_csv, not_good_generator_catch_all
from pythonic_thinking import check_python_version_by_sys, hogehoge

# logging.basicConfig(level=logging.WARNING, format='%(asctime)s:%(levelname)s:%(name)s:%(message)s:%(lineno)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.config.fileConfig("logconf.ini")


# check_python_version_by_sys()
class NoPassFilter(logging.Filter):
    def filter(self, record):
        return "password" not in record.getMessage()


logger = logging.getLogger(__name__)


# def counter():
#     i = 0
#     while True:
#         received = yield i
#         if received:
#             print("received: ", received, bool(received))
#             i = received
#         else:
#             print("received: ", received, bool(received))
#             i += 1
            
# c = counter()
# print(next(c))
# print(c.send(10))
# print(next(c))

# logger.addFilter(NoPassFilter())
# logger.warning("main.py")
# logger.warning("password = hogehoge")
# hogehoge()
