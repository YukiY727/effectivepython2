# Standard Library
import logging

# Third Party Library
import pytest

# First Party Library
from effective_python.function import (
    careful_divide_return_bool_and_value,
    careful_divide_use_none,
    careful_divide_value_error,
    get_avg_ratio,
    get_starts_many,
    get_stats,
)

MODULE_FUNCTION = "effective_python.function"


class TestIndex19:
    def test_get_stats(self, caplog):
        lengths = [1, 2, 3, 4, 5]
        assert get_stats(lengths) == (1, 5)
        assert (
            MODULE_FUNCTION,
            logging.INFO,
            "minimum: 1, maximum: 5",
        ) in caplog.record_tuples

    def test_get_avg_ratio(self, caplog):
        numbers = [1, 2, 3, 4, 5]
        get_avg_ratio(numbers)
        assert (
            MODULE_FUNCTION,
            logging.INFO,
            "longest: 167%, shortest:  33%",
        ) in caplog.record_tuples

    def test_get_starts_many(self, caplog):
        lengths = [63, 73, 72, 60, 67, 66, 71, 61, 72, 70]
        get_starts_many(lengths)
        assert (
            MODULE_FUNCTION,
            logging.INFO,
            "Min: 60, Max: 73",
        ) in caplog.record_tuples
        assert (
            MODULE_FUNCTION,
            logging.INFO,
            "Count: 10, Average: 67.5, Median: 68.5",
        ) in caplog.record_tuples

    def test_careful_divide(self, caplog):
        careful_divide_use_none(1, 2)
        assert len(caplog.record_tuples) == 0
        caplog.clear()
        careful_divide_use_none(0, 1)
        assert (  # このwarningは想定外のもの
            MODULE_FUNCTION,
            logging.WARNING,
            "Invalid inputs",
        ) in caplog.record_tuples
        caplog.clear()
        careful_divide_use_none(5, 0)
        assert (
            MODULE_FUNCTION,
            logging.WARNING,
            "Invalid inputs",
        ) in caplog.record_tuples

    def test_careful_divide_return_bool_and_value(self):
        assert careful_divide_return_bool_and_value(1, 2) == (True, 0.5)
        assert careful_divide_return_bool_and_value(0, 1) == (True, 0)
        assert careful_divide_return_bool_and_value(5, 0) == (False, 0.0)

    def test_careful_divide_value_error(self):
        assert careful_divide_value_error(1, 2) == 0.5
        assert careful_divide_value_error(0, 1) == 0
        with pytest.raises(ValueError):
            careful_divide_value_error(5, 0)
