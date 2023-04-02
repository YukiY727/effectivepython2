# Standard Library
import logging

# Third Party Library
import pytest

# First Party Library
from effective_python.endnotes_and_generators import (
    MyError,
    animate,
    animate_composed,
    cal_batches_endnotes,
    cal_batches_endnotes_walras,
    cal_batches_indent,
    cal_batches_iterator,
    complex_wave,
    complex_wave_modulating,
    division_three_and_sum_10_over,
    double_list_endnotes,
    double_list_square_endnotes,
    endnotes_filter_and,
    endnotes_filter_if,
    endnotes_value,
    endnotes_walras_leak,
    even_squares_dict,
    even_squares_list,
    generator_value,
    generator_value_square,
    index_words_iterator,
    index_words_list,
    iter_accumulate,
    iter_chain,
    iter_combinations,
    iter_combinations_with_replacement,
    iter_cycle,
    iter_dropwhile,
    iter_filterfalse,
    iter_islice,
    iter_permutations,
    iter_product,
    iter_repeat,
    iter_takewhile,
    iter_tee,
    iter_zip_longest,
    my_generator_one_way,
    my_generator_send,
    normalize,
    read_visits_iterator_and_normalize,
    read_visits_iterator_and_normalize_class,
    read_visits_iterator_and_normalize_copy,
    read_visits_iterator_and_normalize_defensive_class,
    read_visits_iterator_and_normalize_defensive_class_iter,
    read_visits_iterator_and_normalize_func,
    run_animate,
    run_modulating,
    run_my_generator1,
    run_my_generator2,
    run_timer,
    run_timer_class,
    run_transmit,
    square_endnotes_list,
    threes_cubed_set,
    triple_list_endnotes,
    triple_list_indent,
    wave,
    wave_modulating,
)

ENDNOTES_AND_GENERATORS = "effective_python.endnotes_and_generators"


class TestIndex27:
    def test_square_endnotes_list(self):
        input_list = [1, 2, 3]
        expected_list = [1, 4, 9]
        assert square_endnotes_list(input_list) == expected_list

    def test_even_squares_list(self):
        input_list = [1, 2, 3]
        expected_list = [4]
        assert even_squares_list(input_list) == expected_list

    def test_even_squares_dict(self):
        input_list = [1, 2, 3]
        expected_dict = {2: 4}
        assert even_squares_dict(input_list) == expected_dict

    def test_threes_cubed_set(self):
        input_list = [1, 2, 3]
        expected_set = {27}
        assert threes_cubed_set(input_list) == expected_set


class TestIndex28:
    def test_double_list_endnotes(self):
        input_list = [[1, 2], [3, 4]]
        expected_list = [1, 2, 3, 4]
        assert double_list_endnotes(input_list) == expected_list

    def test_double_list_square_endnotes(self):
        input_list = [[1, 2], [3, 4]]
        expected_list = [[1, 4], [9, 16]]
        assert double_list_square_endnotes(input_list) == expected_list

    def test_triple_list_endnotes(self):
        input_list = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
        expected_list = [1, 2, 3, 4, 5, 6, 7, 8]
        assert triple_list_endnotes(input_list) == expected_list

    def test_triple_list_indent(self):
        input_list = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
        expected_list = [1, 2, 3, 4, 5, 6, 7, 8]
        assert triple_list_indent(input_list) == expected_list

    def test_endnotes_filter_and(self):
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected_list = [6, 8, 10]
        assert endnotes_filter_and(input_list) == expected_list

    def test_endnotes_filter_if(self):
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected_list = [6, 8, 10]
        assert endnotes_filter_if(input_list) == expected_list

    def test_division_three_and_sum_10_over(self):
        input_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected_list = [[6], [9]]
        assert division_three_and_sum_10_over(input_list) == expected_list

    def test_cal_batches_indent(self):
        stock = {
            "nails": 125,
            "screws": 35,
            "wingnuts": 8,
            "washers": 24,
        }
        order = ["screws", "wingnuts", "clips"]
        assert cal_batches_indent(stock, order) == {"screws": 4, "wingnuts": 1}

    def test_cal_batches_endnotes(self):
        stock = {
            "nails": 125,
            "screws": 35,
            "wingnuts": 8,
            "washers": 24,
        }
        order = ["screws", "wingnuts", "clips"]
        assert cal_batches_endnotes(stock, order) == {"screws": 4, "wingnuts": 1}

    def test_cal_batches_endnotes_walras(self):
        stock = {
            "nails": 125,
            "screws": 35,
            "wingnuts": 8,
            "washers": 24,
        }
        order = ["screws", "wingnuts", "clips"]
        assert cal_batches_endnotes_walras(stock, order) == {"screws": 4, "wingnuts": 1}

    def test_endnotes_walras_leak(self, caplog):
        stock = {
            "nails": 125,
            "screws": 35,
            "wingnuts": 8,
            "washers": 24,
        }
        endnotes_walras_leak(stock)
        assert (
            ENDNOTES_AND_GENERATORS,
            logging.INFO,
            "Last item of [3844, 289, 144] is 12 ** 2 = 144",
        ) in caplog.record_tuples

    def test_cal_batches_iterator(self):
        stock = {
            "nails": 125,
            "screws": 35,
            "wingnuts": 8,
            "washers": 24,
        }
        order = ["screws", "wingnuts", "clips"]
        found = cal_batches_iterator(stock, order)
        assert next(found) == ("screws", 4)
        assert next(found) == ("wingnuts", 1)


class TestIndex30:
    def test_index_words_list(self):
        input_text = "Four score and seven years ago"
        expected = [0, 5, 11, 15, 21, 27]
        assert index_words_list(input_text) == expected

    def test_index_words_iterator(self):
        input_text = "Four score and seven years ago"
        expected = [0, 5, 11, 15, 21, 27]
        assert list(index_words_iterator(input_text)) == expected


class TestIndex31:
    def test_normalize(self):
        input_list = [10, 20, 20]
        assert normalize(input_list) == [20, 40, 40]

    def test_read_visits_iterator_and_normalize(self):
        assert read_visits_iterator_and_normalize() == []  # 空のリストを返す

    def test_read_visits_iterator_and_normalize_copy(self):
        assert read_visits_iterator_and_normalize_copy() == [20, 40, 40]  # copyを使っているので、空のリストを返さない

    def test_read_visits_iterator_and_normalize_func(self):
        assert read_visits_iterator_and_normalize_func() == [20, 40, 40]  # 毎回iteratorを作成しているので、空のリストを返さない

    def test_read_visits_iterator_and_normalize_class(self):
        assert read_visits_iterator_and_normalize_class() == [20, 40, 40]  # 毎回iteratorを作成しているので、空のリストを返さない

    def test_read_visits_iterator_and_normalize_defensive(self):
        assert read_visits_iterator_and_normalize_defensive_class() == [20, 40, 40]  # 毎回iteratorを作成しているので、空のリストを返さない

    def test_read_visits_iterator_and_normalize_defensive_class_iter(self):
        with pytest.raises(TypeError):
            read_visits_iterator_and_normalize_defensive_class_iter()


class TestIndex32:
    def test_endnotes_value(self):
        assert endnotes_value() == [3, 3, 3]

    def test_generator_value(self):
        it = generator_value()
        assert next(it) == 3
        assert next(it) == 3

    def test_generator_value_square(self):
        it = generator_value_square()
        assert next(it) == (3, 100)


class TestIndex33:
    def test_run(self, caplog):
        run_animate(animate)
        assert caplog.record_tuples.count((ENDNOTES_AND_GENERATORS, logging.INFO, "delta: 5.0")) == 4
        assert caplog.record_tuples.count((ENDNOTES_AND_GENERATORS, logging.INFO, "delta: 0.0")) == 3
        assert caplog.record_tuples.count((ENDNOTES_AND_GENERATORS, logging.INFO, "delta: 3.0")) == 2

    def test_animate_compose(self, caplog):
        run_animate(animate_composed)
        assert caplog.record_tuples.count((ENDNOTES_AND_GENERATORS, logging.INFO, "delta: 5.0")) == 4
        assert caplog.record_tuples.count((ENDNOTES_AND_GENERATORS, logging.INFO, "delta: 0.0")) == 3
        assert caplog.record_tuples.count((ENDNOTES_AND_GENERATORS, logging.INFO, "delta: 3.0")) == 2


class TestIndex34:
    def test_run_transmit(self, caplog):
        run_transmit(wave(3.0, 3))
        assert caplog.record_tuples.count((ENDNOTES_AND_GENERATORS, logging.INFO, "Output:   0.0")) == 1
        assert caplog.record_tuples.count((ENDNOTES_AND_GENERATORS, logging.INFO, "Output:   2.6")) == 1
        assert caplog.record_tuples.count((ENDNOTES_AND_GENERATORS, logging.INFO, "Output:  -2.6")) == 1

    def test_my_generator_one_way(self, caplog):
        my_generator_one_way()
        assert (ENDNOTES_AND_GENERATORS, logging.INFO, "output = 1") in caplog.record_tuples
        assert (ENDNOTES_AND_GENERATORS, logging.INFO, "received = None") in caplog.record_tuples

    def test_my_generator_send(self, caplog):
        my_generator_send()
        assert (ENDNOTES_AND_GENERATORS, logging.INFO, "output = 1") in caplog.record_tuples
        assert (ENDNOTES_AND_GENERATORS, logging.INFO, "received = hello") in caplog.record_tuples

    def test_run_modulating(self, caplog):
        run_modulating(wave_modulating(12))
        assert (ENDNOTES_AND_GENERATORS, logging.INFO, "Output is None") in caplog.record_tuples
        assert (ENDNOTES_AND_GENERATORS, logging.INFO, "Output:   0.0") in caplog.record_tuples

    def test_complex_wave(self, caplog):
        run_transmit(complex_wave())
        assert caplog.record_tuples.count((ENDNOTES_AND_GENERATORS, logging.INFO, "Output:   0.0")) == 2
        assert caplog.record_tuples.count((ENDNOTES_AND_GENERATORS, logging.INFO, "Output:   2.6")) == 2
        assert caplog.record_tuples.count((ENDNOTES_AND_GENERATORS, logging.INFO, "Output:  -2.6")) == 2

    def test_complex_wave_modulating(self, caplog):
        run_modulating(complex_wave_modulating())  # 上手く動かない
        assert caplog.record_tuples.count((ENDNOTES_AND_GENERATORS, logging.INFO, "Output is None")) == 3

    def test_run_cascading(self, caplog):
        assert (
            ENDNOTES_AND_GENERATORS,
            logging.INFO,
            "Output is None",
        ) not in caplog.record_tuples  # Noneが出力されていないことを確認


class TestIndex35:
    def test_run_my_generator1(self, caplog):
        with pytest.raises(MyError):
            run_my_generator1()
        assert (ENDNOTES_AND_GENERATORS, logging.INFO, "1") in caplog.record_tuples
        assert (ENDNOTES_AND_GENERATORS, logging.INFO, "2") in caplog.record_tuples

    def test_run_my_generator2(self, caplog):
        run_my_generator2()
        assert (ENDNOTES_AND_GENERATORS, logging.INFO, "1") in caplog.record_tuples
        assert (ENDNOTES_AND_GENERATORS, logging.INFO, "2") in caplog.record_tuples
        assert (ENDNOTES_AND_GENERATORS, logging.INFO, "got MyError") in caplog.record_tuples
        assert (ENDNOTES_AND_GENERATORS, logging.INFO, "4") in caplog.record_tuples

    def test_run_timer(self, caplog):
        run_timer()
        assert (ENDNOTES_AND_GENERATORS, logging.INFO, "3 seconds remaining") in caplog.record_tuples
        assert (ENDNOTES_AND_GENERATORS, logging.INFO, "2 seconds remaining") in caplog.record_tuples
        assert (ENDNOTES_AND_GENERATORS, logging.INFO, "1 seconds remaining") in caplog.record_tuples

    def test_run_timer_class(self, caplog):
        run_timer_class()
        assert (ENDNOTES_AND_GENERATORS, logging.INFO, "3 seconds remaining") in caplog.record_tuples
        assert (ENDNOTES_AND_GENERATORS, logging.INFO, "2 seconds remaining") in caplog.record_tuples
        assert (ENDNOTES_AND_GENERATORS, logging.INFO, "1 seconds remaining") in caplog.record_tuples


class TestIndex36:
    def test_iter_chain(self):
        assert iter_chain() == [1, 2, 3, 4, 5, 6]

    def test_iter_repeat(self):
        assert iter_repeat() == [7, 7, 7]

    def test_iter_tee(self):
        assert iter_tee() == ([1, 2, 3], [1, 2, 3])

    def test_iter_zip_longest(self, caplog):
        iter_zip_longest()
        assert (ENDNOTES_AND_GENERATORS, logging.INFO, "zip: [('one', 1), ('two', 2)]") in caplog.record_tuples
        assert (
            ENDNOTES_AND_GENERATORS,
            logging.INFO,
            "zip_longest: [('one', 1), ('two', 2), ('three', 'nope')]",
        ) in caplog.record_tuples

    def test_iter_slice(self, caplog):
        iter_islice()
        assert (ENDNOTES_AND_GENERATORS, logging.INFO, "first three: [1, 2, 3]") in caplog.record_tuples
        assert (ENDNOTES_AND_GENERATORS, logging.INFO, "middle odds: [1, 3, 5]") in caplog.record_tuples

    def test_iter_takewhile(self, caplog):
        iter_takewhile()
        assert (ENDNOTES_AND_GENERATORS, logging.INFO, "less than three: [1, 2]") in caplog.record_tuples

    def test_iter_dropwhile(self, caplog):
        iter_dropwhile()
        assert (ENDNOTES_AND_GENERATORS, logging.INFO, "upward than three: [3, 4, 5, 6]") in caplog.record_tuples

    def test_iter_filterfalse(self, caplog):
        iter_filterfalse()
        assert (ENDNOTES_AND_GENERATORS, logging.INFO, "filter false: [2, 4, 6]") in caplog.record_tuples

    def test_iter_accumulate(self, caplog):
        iter_accumulate()
        assert (ENDNOTES_AND_GENERATORS, logging.INFO, "accumulate: [1, 3, 6, 10, 15, 21]") in caplog.record_tuples
        assert (ENDNOTES_AND_GENERATORS, logging.INFO, "modulo : [1, 3, 1, 0, 0, 1]") in caplog.record_tuples

    def test_iter_product(self, caplog):
        iter_product()
        assert (
            ENDNOTES_AND_GENERATORS,
            logging.INFO,
            "single: [(1, 1), (1, 2), (2, 1), (2, 2)]",
        ) in caplog.record_tuples
        assert (
            ENDNOTES_AND_GENERATORS,
            logging.INFO,
            "multiple: [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]",
        ) in caplog.record_tuples

    def test_iter_permutations(self, caplog):
        iter_permutations()
        assert (
            ENDNOTES_AND_GENERATORS,
            logging.INFO,
            "permutations: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]",
        ) in caplog.record_tuples

    def test_iter_combinations(self, caplog):
        iter_combinations()
        assert (
            ENDNOTES_AND_GENERATORS,
            logging.INFO,
            "combinations: [(1, 2), (1, 3), (2, 3)]",
        ) in caplog.record_tuples

    def iter_combinations_with_replacement(self, caplog):
        iter_combinations_with_replacement()
        assert (
            ENDNOTES_AND_GENERATORS,
            logging.INFO,
            "combinations_with_replacement: [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]",
        ) in caplog.record_tuples
