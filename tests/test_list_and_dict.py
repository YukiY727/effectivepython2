# Standard Library
import logging

# Third Party Library
import pytest

# First Party Library
from effective_python.list_and_dict import (
    all_slice_duplication_different_object,
    all_slice_duplication_same_object,
    byte_stride,
    good_generator_catch_all,
    kind_of_stride,
    log_best_car,
    log_old_car,
    log_oldest_youngest,
    modify_list_slice,
    not_good_generator_catch_all,
    over_len_slice,
    short_catch_all_unpack,
    slice_long_len,
    slice_short_len,
    slice_start_end,
    sort_by_name,
    sort_weight_name,
    sort_minus_weight_name,
    split_stride_and_slice,
    stride,
    sort_weight_name_reverse,
    unicode_encode_stride,
    unicode_stride,
)

MODULE_NAME_LIST_AND_DICT = "effective_python.list_and_dict"


class TestIndex11:
    def test_slice_start_end(self, caplog):
        slice_start_end()
        assert (MODULE_NAME_LIST_AND_DICT, logging.INFO, "['c', 'd', 'e']") in caplog.record_tuples
        assert (
            MODULE_NAME_LIST_AND_DICT,
            logging.INFO,
            "['b', 'c', 'd', 'e', 'f', 'g']",
        ) in caplog.record_tuples
        assert (MODULE_NAME_LIST_AND_DICT, logging.INFO, "['g']") in caplog.record_tuples

    def test_over_len_slice(self, caplog):
        over_len_slice()
        assert (
            MODULE_NAME_LIST_AND_DICT,
            logging.INFO,
            "['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']",
        ) in caplog.record_tuples
        assert (
            MODULE_NAME_LIST_AND_DICT,
            logging.INFO,
            "['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']",
        ) in caplog.record_tuples

    def test_modify_slice(self, caplog):
        modify_list_slice()
        assert (
            MODULE_NAME_LIST_AND_DICT,
            logging.INFO,
            "Before:['d', 'e', 'f', 'g', 'h']",
        ) in caplog.record_tuples
        assert (
            MODULE_NAME_LIST_AND_DICT,
            logging.INFO,
            "After:['d', 99, 'f', 'g', 'h']",
        ) in caplog.record_tuples
        assert (
            MODULE_NAME_LIST_AND_DICT,
            logging.INFO,
            "Original:['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']",
        ) in caplog.record_tuples

    def test_slice_short_len(self, caplog):
        slice_short_len()
        assert (
            MODULE_NAME_LIST_AND_DICT,
            logging.INFO,
            "Before:['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']",
        ) in caplog.record_tuples
        assert (
            MODULE_NAME_LIST_AND_DICT,
            logging.INFO,
            "After:['a', 'b', 99, 22, 14, 'h']",
        ) in caplog.record_tuples

    def test_slice_long_len(self, caplog):
        slice_long_len()
        assert (
            MODULE_NAME_LIST_AND_DICT,
            logging.INFO,
            "Before:['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']",
        ) in caplog.record_tuples
        assert (
            MODULE_NAME_LIST_AND_DICT,
            logging.INFO,
            "After:['a', 'b', 99, 22, 'd', 'e', 'f', 'g', 'h']",
        ) in caplog.record_tuples

    def test_all_slice_duplication_different_object(self, caplog):
        all_slice_duplication_different_object()
        assert (
            MODULE_NAME_LIST_AND_DICT,
            logging.INFO,
            "a == b True",
        ) in caplog.record_tuples
        assert (
            MODULE_NAME_LIST_AND_DICT,
            logging.INFO,
            "a is b False",
        ) in caplog.record_tuples

    def test_all_slice_duplication_same_object(self, caplog):
        all_slice_duplication_same_object()
        assert (
            MODULE_NAME_LIST_AND_DICT,
            logging.INFO,
            "Before:a ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']",
        ) in caplog.record_tuples
        assert (
            MODULE_NAME_LIST_AND_DICT,
            logging.INFO,
            "Before:b ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']",
        ) in caplog.record_tuples
        assert (
            MODULE_NAME_LIST_AND_DICT,
            logging.INFO,
            "True",
        ) in caplog.record_tuples
        assert (
            MODULE_NAME_LIST_AND_DICT,
            logging.INFO,
            "After:a [101, 102, 103]",
        ) in caplog.record_tuples
        assert (
            MODULE_NAME_LIST_AND_DICT,
            logging.INFO,
            "After:b [101, 102, 103]",
        ) in caplog.record_tuples

    def test_stride(self, caplog):
        stride()
        assert (
            MODULE_NAME_LIST_AND_DICT,
            logging.INFO,
            "odds:['red', 'yellow', 'blue']",
        ) in caplog.record_tuples
        assert (
            MODULE_NAME_LIST_AND_DICT,
            logging.INFO,
            "events:['orange', 'green', 'purple']",
        ) in caplog.record_tuples

    def test_byte_stride(self, caplog):
        byte_stride()
        assert (
            MODULE_NAME_LIST_AND_DICT,
            logging.INFO,
            "b'esoognom'",
        ) in caplog.record_tuples

    def test_unicode_stride(self, caplog):
        unicode_stride()
        assert (
            MODULE_NAME_LIST_AND_DICT,
            logging.INFO,
            "司寿",
        ) in caplog.record_tuples

    def test_unicode_encode_stride(self):
        with pytest.raises(UnicodeDecodeError):
            unicode_encode_stride()

    def test_kind_of_stride(self, caplog):
        kind_of_stride()
        assert (
            MODULE_NAME_LIST_AND_DICT,
            logging.INFO,
            "['a', 'c', 'e', 'g']",
        ) in caplog.record_tuples
        assert (
            MODULE_NAME_LIST_AND_DICT,
            logging.INFO,
            "['h', 'f', 'd', 'b']",
        ) in caplog.record_tuples
        assert (
            MODULE_NAME_LIST_AND_DICT,
            logging.INFO,
            "['c', 'e', 'g']",
        ) in caplog.record_tuples
        assert (
            MODULE_NAME_LIST_AND_DICT,
            logging.INFO,
            "['g', 'e', 'c', 'a']",
        ) in caplog.record_tuples
        assert (
            MODULE_NAME_LIST_AND_DICT,
            logging.INFO,
            "['g', 'e']",
        ) in caplog.record_tuples
        assert (
            MODULE_NAME_LIST_AND_DICT,
            logging.INFO,
            "[]",
        ) in caplog.record_tuples

    def test_split_stride_and_slice(self, caplog):
        split_stride_and_slice()
        assert (
            MODULE_NAME_LIST_AND_DICT,
            logging.INFO,
            "['c', 'e']",
        ) in caplog.record_tuples


class TestIndex13:
    def test_log_old_car(self, caplog):
        log_old_car()
        assert (
            MODULE_NAME_LIST_AND_DICT,
            logging.INFO,
            "oldest:20",
        ) in caplog.record_tuples
        assert (
            MODULE_NAME_LIST_AND_DICT,
            logging.INFO,
            "second_oldest:19",
        ) in caplog.record_tuples
        assert (
            MODULE_NAME_LIST_AND_DICT,
            logging.INFO,
            "others:[15, 9, 8, 7, 6, 4, 1, 0]",
        ) in caplog.record_tuples

    def test_log_oldest_youngest(self, caplog):
        log_oldest_youngest()
        assert (
            MODULE_NAME_LIST_AND_DICT,
            logging.INFO,
            "oldest:20",
        ) in caplog.record_tuples
        assert (
            MODULE_NAME_LIST_AND_DICT,
            logging.INFO,
            "youngest:0",
        ) in caplog.record_tuples
        assert (
            MODULE_NAME_LIST_AND_DICT,
            logging.INFO,
            "others:[19, 15, 9, 8, 7, 6, 4, 1]",
        ) in caplog.record_tuples

    def test_log_best_car(self, caplog):
        log_best_car()
        assert (
            MODULE_NAME_LIST_AND_DICT,
            logging.INFO,
            "Best at Downtown is Silver Shadow , 2 others",
        ) in caplog.record_tuples
        assert (
            MODULE_NAME_LIST_AND_DICT,
            logging.INFO,
            "Best at Airport is Skyline , 3 others",
        ) in caplog.record_tuples

    def test_short_catch_all_unpack(self, caplog):
        short_catch_all_unpack()
        assert (
            MODULE_NAME_LIST_AND_DICT,
            logging.INFO,
            "a:1",
        ) in caplog.record_tuples
        assert (
            MODULE_NAME_LIST_AND_DICT,
            logging.INFO,
            "b:[]",
        ) in caplog.record_tuples

    def test_not_good_generator_catch_all(self, caplog):
        not_good_generator_catch_all()
        assert (
            MODULE_NAME_LIST_AND_DICT,
            logging.INFO,
            "header:('Date', 'Make', 'Model', 'Year', 'Price')",
        ) in caplog.record_tuples
        assert (
            MODULE_NAME_LIST_AND_DICT,
            logging.INFO,
            "row count:200",
        ) in caplog.record_tuples

    def test_good_generator_catch_all(self, caplog):
        good_generator_catch_all()
        assert (
            MODULE_NAME_LIST_AND_DICT,
            logging.INFO,
            "header:('Date', 'Make', 'Model', 'Year', 'Price')",
        ) in caplog.record_tuples
        assert (
            MODULE_NAME_LIST_AND_DICT,
            logging.INFO,
            "row count:200",
        ) in caplog.record_tuples


class TestIndex14:
    def test_sort_by_name(self, caplog):
        sort_by_name()
        assert (
            MODULE_NAME_LIST_AND_DICT,
            logging.INFO,
            "sort_by_name:[Tool('chisel', 0.25), Tool('hammer', 1.25), Tool('level', 3.5), Tool('screwdriver', 0.5)]",
        ) in caplog.record_tuples

    def test_sort_weight_name(self, caplog):
        sort_weight_name()
        assert (
            MODULE_NAME_LIST_AND_DICT,
            logging.INFO,
            "sort_weight_name:[Tool('chisel', 0.5), Tool('screwdriver', 0.5), Tool('hammer', 1.25), Tool('level', 3.5)]",
        ) in caplog.record_tuples

    def test_sort_weight_name_reverse(self, caplog):
        sort_weight_name_reverse()
        assert (
            MODULE_NAME_LIST_AND_DICT,
            logging.INFO,
            "sort_weight_name_reverse:[Tool('level', 3.5), Tool('hammer', 1.25), Tool('screwdriver', 0.5), Tool('chisel', 0.5)]",
        ) in caplog.record_tuples

    def test_sort_minus_weight_name(self, caplog):
        sort_minus_weight_name()
        assert (
            MODULE_NAME_LIST_AND_DICT,
            logging.INFO,
            "sort_minus_weight_name:[Tool('level', 3.5), Tool('hammer', 1.25), Tool('chisel', 0.5), Tool('screwdriver', 0.5)]",
        ) in caplog.record_tuples