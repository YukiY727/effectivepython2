# Standard Library
import logging

# Third Party Library
import pytest
from freezegun import freeze_time

# First Party Library
from effective_python.function import (
    careful_divide_return_bool_and_value,
    careful_divide_use_none,
    careful_divide_value_error,
    check_divide_value_error,
    fibonacci_a,
    flow_rate,
    flow_rate_add,
    get_avg_ratio,
    get_starts_many,
    get_stats,
    json_decode_good,
    json_decode_not_good,
    log1,
    fibonacci_b,
    log2,
    log3,
    log_parameters,
    log_time,
    my_func,
    remainder,
    safe_division_a,
    safe_division_b,
    safe_division_c,
    safe_division_d,
    safe_division_e,
    sort_priority1,
    sort_priority2,
    sort_priority3,
    sort_priority4,
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

    @pytest.mark.parametrize(
        "dividend, divisor, expected_result",
        [
            # 正常系テスト
            (1, 2, (True, 0.5)),
            (-1, 2, (True, -0.5)),
            (0, 1, (True, 0.0)),
            (5, 1.25, (True, 4.0)),
            (1.5, 0.5, (True, 3.0)),
            (5.5, 2.75, (True, 2.0)),
            # 異常系テスト
            (5, 0, (False, 0.0)),
            (-5, 0, (False, 0.0)),
            (0, 0, (False, 0.0)),
        ],
    )
    def test_careful_divide_return_bool_and_value(self, dividend, divisor, expected_result):
        assert careful_divide_return_bool_and_value(dividend, divisor) == expected_result

    def test_careful_divide_value_error(self):
        assert careful_divide_value_error(1, 2) == 0.5
        assert careful_divide_value_error(0, 1) == 0
        with pytest.raises(ValueError):
            careful_divide_value_error(5, 0)

    def test_check_divide_value_error(self, caplog):
        check_divide_value_error(1, 2)
        assert (
            MODULE_FUNCTION,
            logging.INFO,
            "Result: 0.5",
        ) in caplog.record_tuples

        caplog.clear()

        check_divide_value_error(2, 0)
        assert (MODULE_FUNCTION, logging.ERROR, "Invalid inputs") in caplog.record_tuples


class TestIndex21:
    def test_sort_priority1(self):
        numbers = [8, 3, 1, 2, 5, 4, 7, 6]
        groups = {2, 3, 5, 7}
        sort_priority1(numbers, groups)
        assert numbers == [2, 3, 5, 7, 1, 4, 6, 8]

    def test_sort_priority2(self):
        numbers = [8, 3, 1, 2, 5, 4, 7, 6]
        groups = {2, 3, 5, 7}
        assert sort_priority2(numbers, groups) is False  # Trueが返ってくるはず。

    def test_sort_priority3(self):
        numbers = [8, 3, 1, 2, 5, 4, 7, 6]
        groups = {2, 3, 5, 7}
        assert sort_priority3(numbers, groups) is True

    def test_sort_priority4(self):
        numbers = [8, 3, 1, 2, 5, 4, 7, 6]
        groups = {2, 3, 5, 7}
        assert sort_priority4(numbers, groups) is True


class TestIndex22:
    def test_log1(self, caplog):
        log1("test", [])
        assert (MODULE_FUNCTION, logging.INFO, "test") in caplog.record_tuples

    def test_log2(self, caplog):
        log2("test")
        assert (MODULE_FUNCTION, logging.INFO, "test") in caplog.record_tuples

    def test_my_func(self, caplog):
        my_func(*[1, 2])
        assert (MODULE_FUNCTION, logging.INFO, "(1, 2)") in caplog.record_tuples

    def test_log3(self, caplog):
        log3("test", 7, 8)
        assert (MODULE_FUNCTION, logging.INFO, "test - 7: 8") in caplog.record_tuples  # 想定外のログが出力されている


class TestIndex23:
    def test_remainder(self):
        assert remainder(20, 7) == 6
        assert remainder(20, divisor=7) == 6
        assert remainder(number=20, divisor=7) == 6
        assert remainder(divisor=7, number=20) == 6

        my_args = {"number": 20, "divisor": 7}
        assert remainder(**my_args) == 6

        my_kwargs = {"divisor": 7}
        assert remainder(number=20, **my_kwargs) == 6

        my_kwargs = {"number": 20}
        other_kwargs = {"divisor": 7}
        assert remainder(**my_kwargs, **other_kwargs) == 6

    def test_log_parameters(self, caplog):
        log_parameters(alpha=1.5, beta=9, gamma=4)
        assert (MODULE_FUNCTION, logging.INFO, "alpha = 1.5") in caplog.record_tuples
        assert (MODULE_FUNCTION, logging.INFO, "beta = 9") in caplog.record_tuples
        assert (MODULE_FUNCTION, logging.INFO, "gamma = 4") in caplog.record_tuples

    def test_flow_rate(self):
        assert flow_rate(weight_diff=0.5, time_diff=2) == 0.25

    def test_flow_rate_add(self):
        assert flow_rate_add(weight_diff=0.5, time_diff=2) == 0.25


class TestIndex24:
    @freeze_time("2019-01-01 00:00:00")
    def test_use_log_time_sleep(self, caplog):
        log_time("Hi there!")
        assert (MODULE_FUNCTION, logging.INFO, "2019-01-01 00:00:00: Hi there!") in caplog.record_tuples

    def test_json_decode_not_good(self, caplog):
        foo = json_decode_not_good("bad data")
        foo["stuff"] = 5
        bar = json_decode_not_good("also bad")
        bar["meep"] = 1
        assert foo == {"stuff": 5, "meep": 1}  # 想定している値ではない
        assert bar == {"stuff": 5, "meep": 1}

    def test_json_decode_good(self, caplog):
        foo = json_decode_good("bad data")
        foo["stuff"] = 5
        bar = json_decode_good("also bad")
        bar["meep"] = 1
        assert foo == {"stuff": 5}
        assert bar == {"meep": 1}


class TestIndex25:
    def test_safe_division_a(self):
        assert safe_division_a(1, 10**500, True, False) == 0
        assert safe_division_a(1, 0, False, True) == float("inf")

    def test_safe_division_b(self):
        assert safe_division_b(1, 10**500, ignore_overflow=True) == 0
        assert safe_division_b(1, 0, ignore_zero_division=True) == float("inf")
        assert safe_division_b(1, 0, False, True) == float("inf")  # 位置引数の書き方でも、動いてします

    def test_safe_division_c(self):
        assert safe_division_c(1, 10**500, ignore_overflow=True) == 0
        assert safe_division_c(1, 0, ignore_zero_division=True) == float("inf")
        with pytest.raises(TypeError):
            assert safe_division_c(1, 0, False, True) == float("inf")  # これで、位置引数の書き方で動かなくなる
        with pytest.raises(TypeError):
            safe_division_c(numerator=2, denominator=5)

    def test_safe_division_d(self):
        with pytest.raises(TypeError):
            safe_division_d(numerator=2, denominator=5)  # 位置専用引数にキーワード引数を渡すと、TypeErrorになる

    def test_safe_division_e(self):
        assert safe_division_e(22, 7) == 3.1428571429
        assert safe_division_e(22, 7, 5) == 3.14286
        assert safe_division_e(22, 7, ndigits=2) == 3.14


class TestIndex26:
    def test_fibonacci_a(self, caplog):
        assert fibonacci_a(4) == 3
        assert (
            MODULE_FUNCTION,
            logging.INFO,
            "fibonacci_a((0,), {}) -> 0",
        ) in caplog.record_tuples
        assert (
            MODULE_FUNCTION,
            logging.INFO,
            "fibonacci_a((1,), {}) -> 1",
        ) in caplog.record_tuples
        assert (
            MODULE_FUNCTION,
            logging.INFO,
            "fibonacci_a((2,), {}) -> 1",
        ) in caplog.record_tuples
        assert (
            MODULE_FUNCTION,
            logging.INFO,
            "fibonacci_a((3,), {}) -> 2",
        ) in caplog.record_tuples
        assert (
            MODULE_FUNCTION,
            logging.INFO,
            "fibonacci_a((4,), {}) -> 3",  # 本当は、fibonacci_aではなく、wrapper_aでログが出力されるべき
        ) in caplog.record_tuples

    def test_fibonacci_b(self, caplog):
        assert fibonacci_b(4) == 3
        assert (
            MODULE_FUNCTION,
            logging.INFO,
            "fibonacci_b((0,), {}) -> 0",
        ) in caplog.record_tuples
        assert (
            MODULE_FUNCTION,
            logging.INFO,
            "fibonacci_b((1,), {}) -> 1",
        ) in caplog.record_tuples
        assert (
            MODULE_FUNCTION,
            logging.INFO,
            "fibonacci_b((2,), {}) -> 1",
        ) in caplog.record_tuples
        assert (
            MODULE_FUNCTION,
            logging.INFO,
            "fibonacci_b((3,), {}) -> 2",
        ) in caplog.record_tuples
        assert (
            MODULE_FUNCTION,
            logging.INFO,
            "fibonacci_b((4,), {}) -> 3",
        ) in caplog.record_tuples
        
    