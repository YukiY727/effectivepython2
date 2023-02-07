# Standard Library
import logging
from urllib.parse import parse_qs

# Third Party Library
import pytest

# First Party Library
from effective_python.pythonic_thinking import (
    access_tuple,
    bubble_sort_not_unpack,
    bubble_sort_unpack,
    check_python_version_by_sys,
    check_relatively_prime_1,
    check_relatively_prime_2,
    check_relatively_prime_not_good,
    dict_key_and_place_index,
    display_byte_content,
    display_str_content,
    empty_list_for_else_block,
    f_strings_1,
    f_strings_2,
    for_break_else_block,
    for_else_block,
    get_first_int,
    log_enumerate_content,
    log_flavor,
    log_flavor_with_index,
    log_flavor_with_index_start_1,
    log_name_not_same_len,
    log_name_not_same_len_itertools,
    log_names_counts_longest_name_not_good,
    log_names_counts_longest_name_use_enumerate_not_good,
    log_names_counts_longest_name_use_zip,
    log_snack_calories,
    make_banana_smoothies,
    make_drink_cider_good,
    make_drink_cider_not_good,
    make_drink_lemonade_good,
    make_drink_lemonade_not_good,
    not_insert_new_index,
    print_items,
    problem_format_cstyle_1,
    problem_format_cstyle_2,
    problem_format_cstyle_4,
    read_bytes_file_by_r,
    read_bytes_file_by_rb,
    take_order,
    to_bytes,
    to_str,
    unpack_tuple_1,
    unpack_tuple_2,
    url_query_1,
    url_query_2,
    url_query_if_else_multilite,
    url_query_if_else_not_good,
    url_query_int_not_good,
    use_format_cstyle,
    use_string_format,
    while_false_block,
)

MODULE_NAME_PYTHONIC_THINKING = "effective_python.pythonic_thinking"


class Testindex1:
    def test_check_python_version(self, caplog):
        check_python_version_by_sys()
        assert (
            MODULE_NAME_PYTHONIC_THINKING,
            logging.INFO,
            "sys.version_info(major=3, minor=11, micro=1, releaselevel='final', serial=0)",
        ) in caplog.record_tuples

        assert (
            MODULE_NAME_PYTHONIC_THINKING,
            logging.INFO,
            "{'action': 'check python version', 'status': 'ok'}",
        ) in caplog.record_tuples


class Testindex3:
    def test_display_byte_content(self, caplog):
        display_byte_content()
        assert (MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "[104, 101, 108, 108, 111]") in caplog.record_tuples
        assert (MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "b'hello'") in caplog.record_tuples

    def test_display_str_content(self, caplog):
        display_str_content()
        assert (
            MODULE_NAME_PYTHONIC_THINKING,
            logging.INFO,
            "['a', '̀', ' ', 'p', 'r', 'o', 'p', 'o', 's']",
        ) in caplog.record_tuples
        assert (MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "à propos") in caplog.record_tuples

    def test_to_bytes(self):
        assert to_bytes("a") == b"a"
        assert to_bytes(b"a") == b"a"

    def test_to_str(self):
        assert to_str("a") == "a"
        assert to_str(b"a") == "a"

    def test_read_bytes_file_by_r(self):
        with pytest.raises(UnicodeDecodeError) as e:
            read_bytes_file_by_r()
        assert str(e.value) == "'utf-8' codec can't decode byte 0xf1 in position 0: invalid continuation byte"

    def test_read_bytes_file_by_rb(self, caplog):
        read_bytes_file_by_rb()
        assert (MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "b'\\xf1\\xf2\\xf3\\xf4\\xf5'") in caplog.record_tuples


class Testindex4:
    def test_use_format_percent(self, caplog):
        use_format_cstyle()
        assert (MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "Binary is 91, hex is 3167") in caplog.record_tuples

    def test_problem_format_percent_1(self, caplog):
        with pytest.raises(TypeError) as e:
            problem_format_cstyle_1()
            assert (MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "Binary is 91, hex is 3167") in caplog.record_tuples
        assert str(e.value) == "must be real number, not str"

    def test_problem_format_percent_2(self, caplog):
        problem_format_cstyle_2()
        assert (MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "#0: avocado    = 1.25") in caplog.record_tuples
        assert (MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "#1: banana     = 2.50") in caplog.record_tuples
        assert (MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "#2: cauliflower = 15.00") in caplog.record_tuples
        assert (MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "#1: Avocado    = 1") in caplog.record_tuples
        assert (MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "#2: Banana     = 2") in caplog.record_tuples
        assert (MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "#3: Cauliflower = 15") in caplog.record_tuples

    def test_problem_format_percent_4(self, caplog):
        problem_format_cstyle_4()
        assert (MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "Today's soup is lentil.") in caplog.record_tuples
        assert (
            MODULE_NAME_PYTHONIC_THINKING,
            logging.INFO,
            "Today's soup is lentil, oyster is kumamoto oysters, and special is schnitzel.",
        ) in caplog.record_tuples

    def test_use_string_format(self, caplog):
        use_string_format()
        assert (MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "1,234.57") in caplog.record_tuples
        assert (MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "     my string      ") in caplog.record_tuples
        assert (MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "my_var = 1.234") in caplog.record_tuples
        assert (MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "my_var     = 1.23") in caplog.record_tuples
        assert (MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "12.50%") in caplog.record_tuples
        assert (MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "1.23 replaces {}") in caplog.record_tuples
        assert (MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "my_var = 1.234") in caplog.record_tuples
        assert (MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "Max loves food. See Max cook.") in caplog.record_tuples

    def test_dict_key_and_place_index(self, caplog):
        dict_key_and_place_index()
        assert (MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "First course: 'k'") in caplog.record_tuples

    def test_f_strings_1(self, caplog):
        f_strings_1()
        assert (MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "my_var = 1.234") in caplog.record_tuples

    def test_f_strings_2(self, caplog):
        f_strings_2()
        assert (
            MODULE_NAME_PYTHONIC_THINKING,
            logging.INFO,
            "Pi with 3 decimal places is 1.234",
        ) in caplog.record_tuples


class Testindex5:
    def test_url_query_1(self, caplog):
        url_query_1()
        assert (
            MODULE_NAME_PYTHONIC_THINKING,
            logging.INFO,
            "{'red': ['5'], 'blue': ['0'], 'green': ['']}",
        ) in caplog.record_tuples
        assert (MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "Red:     ['5']") in caplog.record_tuples
        assert (MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "Green:   ['']") in caplog.record_tuples
        assert (MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "Opacity: None") in caplog.record_tuples

    def test_url_query_2(self, caplog):
        url_query_2()
        assert (
            MODULE_NAME_PYTHONIC_THINKING,
            logging.INFO,
            "{'red': ['5'], 'blue': ['0'], 'green': ['']}",
        ) in caplog.record_tuples
        assert (MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "Red:      5") in caplog.record_tuples
        assert (MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "Green:    0") in caplog.record_tuples
        assert (MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "Opacity:  0") in caplog.record_tuples

    def test_url_query_int_not_good(self, caplog):
        url_query_int_not_good()
        assert (MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "5") in caplog.record_tuples

    def test_url_query_if_else_not_good(self, caplog):
        url_query_if_else_not_good()
        assert (MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "5") in caplog.record_tuples

    def test_url_query_if_else_multilite(self, caplog):
        url_query_if_else_multilite()
        assert (MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "0") in caplog.record_tuples

    def test_get_first_int_not_default(self):
        my_values = parse_qs("red=5&blue=0&green=", keep_blank_values=True)
        assert get_first_int(my_values, "red") == 5

    def test_get_first_int_default(self):
        my_values = parse_qs("red=5&blue=0&green=", keep_blank_values=True)
        assert get_first_int(my_values, "pink") == 0


class TestIndex6:
    def test_print_items(self, caplog):
        print_items()
        assert (MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "<class 'dict_items'>") in caplog.record_tuples
        assert (
            MODULE_NAME_PYTHONIC_THINKING,
            logging.INFO,
            "dict_items([('chips', 140), ('popcorn', 80), ('nuts', 190)])",
        ) in caplog.record_tuples
        assert (
            MODULE_NAME_PYTHONIC_THINKING,
            logging.INFO,
            "(('chips', 140), ('popcorn', 80), ('nuts', 190))",
        ) in caplog.record_tuples

    def test_access_tuple(self, caplog):
        access_tuple()
        assert (
            MODULE_NAME_PYTHONIC_THINKING,
            logging.INFO,
            "('chips', 140) and ('popcorn', 80)",
        ) in caplog.record_tuples

    def test_not_insert_new_index(self):
        with pytest.raises(TypeError) as e:
            not_insert_new_index()
        assert str(e.value) == "'tuple' object does not support item assignment"

    def test_unpack_tuple_1(self, caplog):
        unpack_tuple_1()
        assert (MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "Peanut and Butter") in caplog.record_tuples

    def test_unpack_tuple_2(self, caplog):
        unpack_tuple_2()
        assert (
            MODULE_NAME_PYTHONIC_THINKING,
            logging.INFO,
            "Favorite salty is pretzels with 100 calories",
        ) in caplog.record_tuples
        assert (
            MODULE_NAME_PYTHONIC_THINKING,
            logging.INFO,
            "Favorite sweet is cookies with 180 calories",
        ) in caplog.record_tuples
        assert (
            MODULE_NAME_PYTHONIC_THINKING,
            logging.INFO,
            "Favorite veggie is carrots with 20 calories",
        ) in caplog.record_tuples

    def test_bubble_sort_not_unpack(self):
        names = ["pretzels", "carrots", "arugula", "bacon"]
        assert bubble_sort_not_unpack(names) == ["arugula", "bacon", "carrots", "pretzels"]

    def test_bubble_sort_unpack(self):
        names = ["pretzels", "carrots", "arugula", "bacon"]
        assert bubble_sort_unpack(names) == ["arugula", "bacon", "carrots", "pretzels"]

    def test_log_snack_calories(self, caplog):
        snacks = [("bacon", 350), ("donut", 240), ("muffin", 190)]
        log_snack_calories(snacks)
        assert (
            MODULE_NAME_PYTHONIC_THINKING,
            logging.INFO,
            "#1: bacon has 350 calories",
        ) in caplog.record_tuples
        assert (
            MODULE_NAME_PYTHONIC_THINKING,
            logging.INFO,
            "#2: donut has 240 calories",
        ) in caplog.record_tuples
        assert (
            MODULE_NAME_PYTHONIC_THINKING,
            logging.INFO,
            "#3: muffin has 190 calories",
        ) in caplog.record_tuples


class Testindex7:
    def test_log_flavor(self, caplog):
        log_flavor()
        assert (
            MODULE_NAME_PYTHONIC_THINKING,
            logging.INFO,
            "vanilla is delicious",
        ) in caplog.record_tuples
        assert (
            MODULE_NAME_PYTHONIC_THINKING,
            logging.INFO,
            "chocolate is delicious",
        ) in caplog.record_tuples
        assert (
            MODULE_NAME_PYTHONIC_THINKING,
            logging.INFO,
            "pecan is delicious",
        ) in caplog.record_tuples
        assert (
            MODULE_NAME_PYTHONIC_THINKING,
            logging.INFO,
            "strawberry is delicious",
        ) in caplog.record_tuples

    def test_log_flavor_with_index(self, caplog):
        log_flavor_with_index()
        assert (
            MODULE_NAME_PYTHONIC_THINKING,
            logging.INFO,
            "1: vanilla",
        ) in caplog.record_tuples
        assert (
            MODULE_NAME_PYTHONIC_THINKING,
            logging.INFO,
            "2: chocolate",
        ) in caplog.record_tuples
        assert (
            MODULE_NAME_PYTHONIC_THINKING,
            logging.INFO,
            "3: pecan",
        ) in caplog.record_tuples
        assert (
            MODULE_NAME_PYTHONIC_THINKING,
            logging.INFO,
            "4: strawberry",
        ) in caplog.record_tuples

    def test_log_enumerate_content(self, caplog):
        log_enumerate_content()
        assert (
            MODULE_NAME_PYTHONIC_THINKING,
            logging.INFO,
            "(0, 'vanilla')",
        ) in caplog.record_tuples
        assert (
            MODULE_NAME_PYTHONIC_THINKING,
            logging.INFO,
            "(1, 'chocolate')",
        ) in caplog.record_tuples

    def test_log_flavor_with_index_start_1(self, caplog):
        log_flavor_with_index_start_1()
        assert (
            MODULE_NAME_PYTHONIC_THINKING,
            logging.INFO,
            "1: vanilla",
        ) in caplog.record_tuples
        assert (
            MODULE_NAME_PYTHONIC_THINKING,
            logging.INFO,
            "2: chocolate",
        ) in caplog.record_tuples
        assert (
            MODULE_NAME_PYTHONIC_THINKING,
            logging.INFO,
            "3: pecan",
        ) in caplog.record_tuples
        assert (
            MODULE_NAME_PYTHONIC_THINKING,
            logging.INFO,
            "4: strawberry",
        ) in caplog.record_tuples


class Testindex8:
    def test_log_names_counts_longest_name_not_good(self, caplog):
        log_names_counts_longest_name_not_good()
        assert (
            MODULE_NAME_PYTHONIC_THINKING,
            logging.INFO,
            "[7, 4, 5]",
        ) in caplog.record_tuples
        assert (
            MODULE_NAME_PYTHONIC_THINKING,
            logging.INFO,
            "Cecilia",
        ) in caplog.record_tuples

    def test_log_names_counts_longest_name_use_enumerate_not_good(self, caplog):
        log_names_counts_longest_name_use_enumerate_not_good()
        assert (
            MODULE_NAME_PYTHONIC_THINKING,
            logging.INFO,
            "[7, 4, 5]",
        ) in caplog.record_tuples
        assert (
            MODULE_NAME_PYTHONIC_THINKING,
            logging.INFO,
            "Cecilia",
        ) in caplog.record_tuples

    def test_log_names_counts_longest_name_use_zip(self, caplog):
        log_names_counts_longest_name_use_zip()
        assert (
            MODULE_NAME_PYTHONIC_THINKING,
            logging.INFO,
            "Cecilia",
        ) in caplog.record_tuples

    def test_log_name_not_same_len(self, caplog):
        log_name_not_same_len()
        assert (
            MODULE_NAME_PYTHONIC_THINKING,
            logging.INFO,
            "Cecilia",
        ) in caplog.record_tuples
        assert (
            MODULE_NAME_PYTHONIC_THINKING,
            logging.INFO,
            "Lise",
        ) in caplog.record_tuples
        assert (
            MODULE_NAME_PYTHONIC_THINKING,
            logging.INFO,
            "Marie",
        ) in caplog.record_tuples

    def test_log_name_not_same_len_itertools(self, caplog):
        log_name_not_same_len_itertools()
        assert (
            MODULE_NAME_PYTHONIC_THINKING,
            logging.INFO,
            "Cecilia: 7",
        ) in caplog.record_tuples
        assert (
            MODULE_NAME_PYTHONIC_THINKING,
            logging.INFO,
            "Lise: 4",
        ) in caplog.record_tuples
        assert (
            MODULE_NAME_PYTHONIC_THINKING,
            logging.INFO,
            "Marie: 5",
        ) in caplog.record_tuples
        assert (
            MODULE_NAME_PYTHONIC_THINKING,
            logging.INFO,
            "Rosalind: None",
        ) in caplog.record_tuples


class TestIndex9:
    def test_for_else_block(self, caplog):
        for_else_block()
        assert (MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "Loop 0") in caplog.record_tuples
        assert (MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "Loop 1") in caplog.record_tuples
        assert (MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "Loop 2") in caplog.record_tuples
        assert (MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "Else block!") in caplog.record_tuples

    def test_for_break_else_block(self, caplog):
        for_break_else_block()
        assert (MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "Loop 0") in caplog.record_tuples
        assert (MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "Loop 1") in caplog.record_tuples
        assert caplog.record_tuples.count((MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "Loop 2")) == 0
        assert caplog.record_tuples.count((MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "Else block!")) == 0

    def test_empty_list_for_else_block(self, caplog):
        empty_list_for_else_block()
        assert (MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "For Else block!") in caplog.record_tuples
        assert caplog.record_tuples.count((MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "Never runs")) == 0

    def test_while_flase_block(self, caplog):
        while_false_block()
        assert (MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "While Else block!") in caplog.record_tuples
        assert caplog.record_tuples.count((MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "Never runs")) == 0

    def test_check_relatively_prime_not_good(self, caplog):
        check_relatively_prime_not_good()
        assert (MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "Testing 2") in caplog.record_tuples
        assert (MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "Testing 3") in caplog.record_tuples
        assert (MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "Testing 4") in caplog.record_tuples
        assert (MODULE_NAME_PYTHONIC_THINKING, logging.INFO, "relatively prime") in caplog.record_tuples

    def test_check_relatively_prime_1(self):
        assert check_relatively_prime_1(4, 9)
        assert not check_relatively_prime_1(3, 9)

    def test_check_relatively_prime_2(self):
        assert check_relatively_prime_2(4, 9)
        assert not check_relatively_prime_2(3, 9)


@pytest.fixture()
def mock_make_lemonade(mocker):
    return mocker.patch("effective_python.pythonic_thinking.make_lemonade")


@pytest.fixture()
def mock_out_of_stock(mocker):
    return mocker.patch("effective_python.pythonic_thinking.out_of_stock")


@pytest.fixture()
def mock_make_cider(mocker):
    return mocker.patch("effective_python.pythonic_thinking.make_cider")


@pytest.fixture()
def mock_slice_bananas(mocker):
    return mocker.patch("effective_python.pythonic_thinking.sline_bananas")


@pytest.fixture()
def mock_make_smoothie(mocker):
    return mocker.patch("effective_python.pythonic_thinking.make_smoothies")


class TestIndex10:
    def test_make_drink_lemonade_not_good(self, mock_make_lemonade, mock_out_of_stock):
        make_drink_lemonade_not_good()
        mock_make_lemonade.assert_called_once()
        mock_out_of_stock.assert_not_called()

    def test_make_drink_lemonade_good(self, mock_make_lemonade, mock_out_of_stock):
        make_drink_lemonade_good()
        mock_make_lemonade.assert_called_once()
        mock_out_of_stock.assert_not_called()

    def test_make_drink_cider_not_good(self, mock_make_cider, mock_out_of_stock):
        make_drink_cider_not_good()
        mock_make_cider.assert_called_once()
        mock_out_of_stock.assert_not_called()

    def test_make_drink_cider_good(self, mock_make_cider, mock_out_of_stock):
        make_drink_cider_good()
        mock_make_cider.assert_called_once()
        mock_out_of_stock.assert_not_called()

    def test_make_banana_smoothies(self, mock_slice_bananas, mock_make_smoothie):
        make_banana_smoothies()
        mock_slice_bananas.assert_called_once()
        mock_make_smoothie.assert_called_once()

    def test_take_order(self, mock_slice_bananas, mock_make_smoothie, mock_make_cider, mock_make_lemonade):
        take_order()
        mock_slice_bananas.assert_called_once()
        mock_make_smoothie.assert_called_once()
        mock_make_cider.assert_not_called()
        mock_make_lemonade.assert_not_called()
