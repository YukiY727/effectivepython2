from urllib.parse import parse_qs

import pytest

from effective_python.pythonic_thinking import (
    check_python_version_by_sys,
    dict_key_and_place_index,
    f_strings_1,
    f_strings_2,
    get_first_int,
    print_items,
    problem_format_cstyle_1,
    problem_format_cstyle_2,
    problem_format_cstyle_4,
    read_bytes_file_by_r,
    read_bytes_file_by_rb,
    sample_bytes,
    sample_str,
    to_bytes,
    to_str,
    url_query_1,
    url_query_2,
    url_query_if_else_multilite,
    url_query_if_else_not_good,
    url_query_int_not_good,
    use_format_cstyle,
    use_string_format,
)


class Testindex1:
    def test_check_python_version(self, capsys):
        check_python_version_by_sys()
        out = capsys.readouterr()
        assert out.out == (
            "sys.version_info(major=3, minor=11, micro=0, releaselevel='final', serial=0)\nPython version is ok\n"
        )


class Testindex3:
    def test_sample_bytes(self, capsys):
        sample_bytes()
        out = capsys.readouterr()
        assert out.out == "[104, 101, 108, 108, 111]\nb'hello'\n"

    def test_sample_str(self, capsys):
        sample_str()
        out = capsys.readouterr()
        assert out.out == "['a', '̀', ' ', 'p', 'r', 'o', 'p', 'o', 's']\nà propos\n"

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

    def test_read_bytes_file_by_rb(self, capsys):
        read_bytes_file_by_rb()
        out = capsys.readouterr()
        assert out.out == "b'\\xf1\\xf2\\xf3\\xf4\\xf5'\n"


class Testindex4:
    def test_use_format_percent(self, capsys):
        use_format_cstyle()
        out = capsys.readouterr()
        assert out.out == "Binary is 91, hex is 3167\n"

    def test_problem_format_percent_1(self, capsys):
        with pytest.raises(TypeError) as e:
            problem_format_cstyle_1()
            out = capsys.readouterr()
            assert out.out == "Binary is 91, hex is 3167\n"
        assert str(e.value) == "must be real number, not str"

    def test_problem_format_percent_2(self, capsys):
        problem_format_cstyle_2()
        out = capsys.readouterr()
        assert out.out == (
            "#0: avocado    = 1.25\n"
            "#1: banana     = 2.50\n"
            "#2: cauliflower = 15.00\n"
            "#1: Avocado    = 1\n"
            "#2: Banana     = 2\n"
            "#3: Cauliflower = 15\n"
        )

    def test_problem_format_percent_4(self, capsys):
        problem_format_cstyle_4()
        out = capsys.readouterr()
        assert out.out == (
            "Today's soup is lentil.\n"
            "Today's soup is lentil, oyster is kumamoto oysters, and special is schnitzel.\n"
        )

    def test_use_string_format(self, capsys):
        use_string_format()
        out = capsys.readouterr()
        assert out.out == (
            "1,234.57\n"
            "     my string      \n"
            "my_var = 1.234\n"
            "my_var     = 1.23\n"
            "12.50%\n"
            "1.23 replaces {}\n"
            "my_var = 1.234\n"
            "Max loves food. See Max cook.\n"
        )

    def test_dict_key_and_place_index(self, capsys):
        dict_key_and_place_index()
        out = capsys.readouterr()
        assert out.out == ("First course: 'k'\n")

    def test_f_strings_1(self, capsys):
        f_strings_1()
        out = capsys.readouterr()
        assert out.out == ("my_var = 1.234\n" "'my_var'   = 1.23\n")

    def test_f_strings_2(self, capsys):
        f_strings_2()
        out = capsys.readouterr()
        assert out.out == ("Pi with 3 decimal places is 1.234\n")


class Testindex5:
    def test_url_query_1(self, capsys):
        url_query_1()
        out = capsys.readouterr()
        assert out.out == (
            "{'red': ['5'], 'blue': ['0'], 'green': ['']}\n"  # noqa
            "Red:      ['5']\n"  # noqa
            "Green:    ['']\n"  # noqa
            "Opacity:  None\n"  # noqa
        )

    def test_url_query_2(self, capsys):
        url_query_2()
        out = capsys.readouterr()
        assert out.out == (
            "{'red': ['5'], 'blue': ['0'], 'green': ['']}\n"  # noqa
            "Red:      5\n"  # noqa
            "Green:    0\n"  # noqa
            "Opacity:  0\n"  # noqa
        )

    def test_url_query_int_not_good(self, capsys):
        url_query_int_not_good()
        out = capsys.readouterr()
        assert out.out == ("5\n")

    def test_url_query_if_else_not_good(self, capsys):
        url_query_if_else_not_good()
        out = capsys.readouterr()
        assert out.out == ("5\n")

    def test_url_query_if_else_multilite(self, capsys):
        url_query_if_else_multilite()
        out = capsys.readouterr()
        assert out.out == ("0\n")

    def test_get_first_int_not_default(self):
        my_values = parse_qs("red=5&blue=0&green=", keep_blank_values=True)
        assert get_first_int(my_values, "red") == 5

    def test_get_first_int_default(self):
        my_values = parse_qs("red=5&blue=0&green=", keep_blank_values=True)
        assert get_first_int(my_values, "pink") == 0


class TestIndex6:
    def test_print_items(self, capsys):
        print_items()
        out = capsys.readouterr()
        assert out.out == (
            "<class 'dict_items'>\n"  # noqa
            "dict_items([('chips', 140), ('popcorn', 80), ('nuts', 190)])\n"  # noqa
            "(('chips', 140), ('popcorn', 80), ('nuts', 190))\n"  # noqa
        )


    # def test_access_tuple(self, capsys):
    #     access_tuple()
    #     out = capsys.readouterr()