import logging

logger = logging.getLogger(__name__)
# 1使用するpythonのバージョンを確認する


import sys


def check_python_version_by_sys():
    assert sys.version_info >= (3, 6), "Python 3.6 or later is required"
    logger.info(sys.version_info)
    logger.info({"action": "check python version", "status": "ok"})


# check_python_version_by_sys()
# 2pep8スタイルガイドに従ってコードを書く
# black, flake8などを使うようにする

# 3bytesとstrの違いを理解する
def display_byte_content():
    a = b"h\x65llo"
    logger.info(list(a))
    logger.info(a)


def display_str_content():
    a = "a\u0300 propos"
    logger.info(list(a))
    logger.info(a)


def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode("utf-8")
    else:
        value = bytes_or_str
    return value  # Instance of str


def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode("utf-8")
    else:
        value = bytes_or_str
    return value  # Instance of bytes


import os
from pathlib import Path


def read_bytes_file_by_r():
    with open(os.path.join(Path(__file__).parents[0], "data", "pythonic_thinking", "data.bin"), "r") as f:
        data = f.read()
    logger.info(data)


def read_bytes_file_by_rb():
    with open(os.path.join(Path(__file__).parents[0], "data", "pythonic_thinking", "data.bin"), "rb") as f:
        data = f.read()
    logger.info(data)


def read_bytes_file_by_encode_cp():
    with open(
        os.path.join(Path(__file__).parents[0], "data", "pythonic_thinking", "data.bin"), "r", encoding="cp1252"
    ) as f:
        data = f.read()
    assert data == "ñòóôõ"


# 4Cスタイルフォーマット文字列とstr.formatを使わず、f文字列を使う


def use_format_cstyle():
    a = 0b1011011
    b = 0xC5F
    logger.info("Binary is %d, hex is %d" % (a, b))


def problem_format_cstyle_1():
    # %演算子の両側がきちんと揃っているかチェックする必要がある。
    key = "my_var"
    value = 1.234
    logger.info("%-10s = %.2f" % (key, value))
    logger.info("%-10s = %.2f" % (value, key))


def problem_format_cstyle_2():
    # 可読性が悪い
    pantry = [
        ("avocado", 1.25),
        ("banana", 2.5),
        ("cauliflower", 15),
    ]
    for i, (item, count) in enumerate(pantry):
        logger.info("#%d: %-10s = %.2f" % (i, item, count))  # outputが少しわかりづらい

    for i, (item, count) in enumerate(pantry):
        logger.info("#%d: %-10s = %d" % (i + 1, item.title(), round(count)))  # 読みづらくなってしまう


def problem_format_cstyle_3():
    # 同じ変数を使いたい場合は、変数を複数回定義しなければならない
    template = "%s loves food. See %s cook."
    name = "Max"
    logger.info(template % (name, name))
    name = "brad"
    logger.info(template % (name.title(), name.title()))


def dict_format():
    # 一つ目の問題を解決する
    key = "my_var"
    value = 1.234
    old_way = "%-10s = %.2f" % (key, value)
    new_way = "%(key)-10s = %(value).2f" % {"key": key, "value": value}
    reordered = "%(key)-10s = %(value).2f" % {"value": value, "key": key}
    assert old_way == new_way == reordered


def solve_problem_3():
    name = "Max"
    temaplate = "%s loves food. See %s cook."
    before = temaplate % (name, name)
    temaplate = "%(name)s loves food. See %(name)s cook."
    after = temaplate % {"name": name}
    assert before == after


def problem_format_cstyle_4():
    # 辞書を使うと変数名を多く定義しなければならない
    pantry = [
        ("avocado", 1.25),
        ("banana", 2.5),
        ("cauliflower", 15),
    ]
    for i, (item, count) in enumerate(pantry):
        before = "#%d: %-10s = %d" % (i + 1, item.title(), round(count))
        after = "#%(index)d: %(item)-10s = %(count)d" % {"index": i + 1, "item": item.title(), "count": round(count)}
        assert before == after

    soup = "lentil"
    logger.info("Today's soup is %(soup)s." % {"soup": soup})

    menu = {
        "soup": "lentil",
        "oyster": "kumamoto",
        "special": "schnitzel",
    }
    logger.info("Today's soup is %(soup)s, oyster is %(oyster)s oysters, and special is %(special)s." % menu)


def use_string_format():
    a = 1234.5678
    formatted = format(a, ",.2f")  # 数字を3桁でカンマ区切りにして、小数点以下2桁まで表示する
    logger.info(formatted)

    b = "my string"
    formatted = format(b, "^20s")  # 文字列を20文字の中央に配置する
    logger.info(formatted)

    key = "my_var"
    value = 1.234
    logger.info("{} = {}".format(key, value))  # 位置引数を使う

    logger.info("{:<10} = {:.2f}".format(key, value))

    logger.info("%.2f%%" % 12.5)  # 12.50%

    logger.info("{} replaces {{}}".format(1.23))  # 1.23 replaces {}

    # 1つ目の問題を解決する
    logger.info("{1} = {0}".format(value, key))

    # 3つ目の問題を解決する
    name = "Max"
    logger.info("{0} loves food. See {0} cook.".format(name))

    # 2つ目の問題は解決できない
    pantry = [
        ("avocado", 1.25),
        ("banana", 2.5),
        ("cauliflower", 15),
    ]
    for i, (item, count) in enumerate(pantry):
        old_style = "#%d: %-10s = %d" % (i + 1, item.title(), round(count))
        new_style = "#{}: {:<10} = {}".format(i + 1, item.title(), round(count))
        assert old_style == new_style


def dict_key_and_place_index():
    menu = {
        "soup": "lentil",
        "oyster": "kumamoto",
        "special": "schnitzel",
    }
    logger.info("First course: {menu[oyster][0]!r}".format(menu=menu))  # First course: kumamoto

    # 4つ目の問題(変数を多く定義しないといけない)が解決しない
    old_template = "Today's soup is %(soup)s, oyster is %(oyster)s oysters, and special is %(special)s."
    old_formatted = old_template % menu
    new_template = "Today's soup is {soup}, oyster is {oyster} oysters, and special is {special}."
    new_formatted = new_template.format(**menu)
    assert old_formatted == new_formatted


def f_strings_1():
    key = "my_var"
    value = 1.234
    formatted = f"{key} = {value}"
    logger.info(formatted)

    logger.info(f"{key!r:<10} = {value:.2f}")

    f_string = f"{key:<10} = {value:.2f}"
    c_tuple = "%-10s = %.2f" % (key, value)
    str_args = "{:<10} = {:.2f}".format(key, value)
    str_kw = "{key:<10} = {value:.2f}".format(key=key, value=value)
    c_dict = "%(key)-10s = %(value).2f" % {"key": key, "value": value}
    assert f_string == c_tuple == str_args == str_kw == c_dict


def f_strings_2():
    pantry = [
        ("avocado", 1.25),
        ("banana", 2.5),
        ("cauliflower", 15),
    ]
    for i, (item, count) in enumerate(pantry):
        old_style = "#%d: %-10s = %d" % (i + 1, item.title(), round(count))
        new_style = f"#{i + 1}: {item.title():<10} = {round(count)}"
        assert old_style == new_style

    places = 3
    number = 1.2345
    logger.info(f"Pi with {places} decimal places is {number:.{places}f}")


# 5複雑な式の代わりにヘルパー関数を使う

from urllib.parse import parse_qs


def url_query_1():
    my_values = parse_qs("red=5&blue=0&green=", keep_blank_values=True)
    logger.info(repr(my_values))
    logger.info(f"Red:     {my_values.get('red')}")
    logger.info(f"Green:   {my_values.get('green')}")
    logger.info(f"Opacity: {my_values.get('opacity')}")


def url_query_2():
    my_values = parse_qs("red=5&blue=0&green=", keep_blank_values=True)
    logger.info(repr(my_values))

    logger.info(f"Red:      {my_values.get('red', [''])[0] or 0}")
    # 空文字列はFalse判定になる。
    logger.info(f"Green:    {my_values.get('green', [''])[0] or 0}")
    logger.info(f"Opacity:  {my_values.get('opacity', [''])[0] or 0}")

    # しかし、これらは読みづらい上、整数になって返ってくることを保証していない。


def url_query_int_not_good():
    my_values = parse_qs("red=5&blue=0&green=", keep_blank_values=True)
    # これでは、何をしているかが分かりにくい
    red = int(my_values.get("red", [""])[0] or 0)
    logger.info(red)


def url_query_if_else_not_good():
    my_values = parse_qs("red=5&blue=0&green=", keep_blank_values=True)
    red_str = my_values.get("red", [""])
    # red_strの中身が空文字列の場合、red_str[0]はFalseになり、bool値判定していることがわかりやすい
    red = int(red_str[0]) if red_str[0] else 0
    logger.info(red)


def url_query_if_else_multilite():
    my_values = parse_qs("red=5&blue=0&green=", keep_blank_values=True)
    # 上のurl_query_if_else_not_goodは、if-elseのネストが深くなると読みづらくなる。複雑でなければ、上の方法でもよい
    green_str = my_values.get("green", [""])
    if green_str[0]:
        green = int(green_str[0])
    else:
        green = 0
    logger.info(green)


def get_first_int(values: dict[str : list[str]], key: str, default=0):
    # ヘルパー関数にすることで、可読性上がる。
    # 読みやすさで得られる利益は常に簡潔さをもたらす便益を上回る。
    found = values.get(key, [""])
    if found[0]:
        return int(found[0])
    else:
        return default


# 6インデックスではなく、複数代入アンパックを使う
def print_items():
    snack_calories = {
        "chips": 140,
        "popcorn": 80,
        "nuts": 190,
    }
    items = tuple(snack_calories.items())
    logger.info(type(snack_calories.items()))
    logger.info(snack_calories.items())
    logger.info(items)


def access_tuple():
    snack_calories = {
        "chips": 140,
        "popcorn": 80,
        "nuts": 190,
    }
    items = tuple(snack_calories.items())
    first = items[0]
    second = items[1]
    logger.info(f"{first} and {second}")


def not_insert_new_index():
    # tupleはimmutableなので、新しい要素を追加できない
    pair = ("Peanut", "Butter")
    pair[0] = "Peanuts"


def unpack_tuple_1():
    item = ("Peanut", "Butter")
    first, second = item
    logger.info(f"{first} and {second}")


def unpack_tuple_2():
    # よくない書き方だが、以下のような書き方もできる
    favorite_snacks = {
        "salty": ("pretzels", 100),
        "sweet": ("cookies", 180),
        "veggie": ("carrots", 20),
    }
    (
        (type1, (name1, cals1)),  # noqa
        (type2, (name2, cals2)),  # noqa
        (type3, (name3, cals3)),
    ) = favorite_snacks.items()  # noqa

    logger.info(f"Favorite {type1} is {name1} with {cals1} calories")
    logger.info(f"Favorite {type2} is {name2} with {cals2} calories")
    logger.info(f"Favorite {type3} is {name3} with {cals3} calories")


def bubble_sort_not_unpack(a: list):
    for _ in range(len(a)):
        for i in range(1, len(a)):
            if a[i] < a[i - 1]:
                temp = a[i]
                a[i] = a[i - 1]
                a[i - 1] = temp
    return a


def bubble_sort_unpack(a: list):
    for _ in range(len(a)):
        for i in range(1, len(a)):
            if a[i] < a[i - 1]:
                a[i], a[i - 1] = a[i - 1], a[i]
    # a[i - 1], a[i]が一時的な無名tupleになり、a[i], a[i - 1]に代入された後、そのtupleは破棄される
    return a


def log_snack_calories(snaks: list[tuple[str, int]]):
    # 以下のように書くと、indexを使う必要がなくなる。pythonicな書き方
    for rank, (name, cals) in enumerate(snaks, 1):
        logger.info(f"#{rank}: {name} has {cals} calories")
