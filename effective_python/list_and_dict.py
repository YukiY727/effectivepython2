# Standard Library
import logging

logger = logging.getLogger(__name__)


# 11 シーケンスをどのようにスライスするか知っておく
def slice_start_end():
    a = ["a", "b", "c", "d", "e", "f", "g", "h"]
    logger.info(a[2:5])
    logger.info(a[1:7])
    logger.info(a[6:-1])
    assert a[:5] == a[0:5]


def over_len_slice():
    # スライスの長さがリストの長さより長い場合、リストの長さまでエラーが出ずに取得できる。
    a = ["a", "b", "c", "d", "e", "f", "g", "h"]
    logger.info(a[:20])
    logger.info(a[-20:])


def modify_list_slice():
    # スライスして取得したリストを変更しても、元のリストは変更されない
    a = ["a", "b", "c", "d", "e", "f", "g", "h"]
    b = a[3:]
    logger.info(f"Before:{b}")
    b[1] = 99
    logger.info(f"After:{b}")
    logger.info(f"Original:{a}")


def slice_short_len():
    # スライスの長さがリストの長さより短い場合、代入するとリストの長さが変わる
    a = ["a", "b", "c", "d", "e", "f", "g", "h"]
    logger.info(f"Before:{a}")
    a[2:7] = [99, 22, 14]
    logger.info(f"After:{a}")


def slice_long_len():
    # スライスの長さがリストの長さより短い場合、代入するとリストの長さが変わる
    a = ["a", "b", "c", "d", "e", "f", "g", "h"]
    logger.info(f"Before:{a}")
    a[2:3] = [99, 22]
    logger.info(f"After:{a}")


def all_slice_duplication_different_object():
    # スライスを使って、複製すると、異なるオブジェクトを参照する
    a = ["a", "b", "c", "d", "e", "f", "g", "h"]
    b = a[:]
    logger.info(f"a == b {a == b}")
    logger.info(f"a is b {a is b}")


def all_slice_duplication_same_object():
    # スライスを使わずに、複製すると、同じオブジェクトを参照する
    a = ["a", "b", "c", "d", "e", "f", "g", "h"]
    b = a
    logger.info(f"Before:a {a}")
    logger.info(f"Before:b {b}")
    a[:] = [101, 102, 103]
    logger.info(a is b)
    logger.info(f"After:a {a}")
    logger.info(f"After:b {b}")


# 12 1つの式では、ストライドとスライスを同時に使わない
def stride():
    x = ["red", "orange", "yellow", "green", "blue", "purple"]
    odds = x[::2]
    events = x[1::2]
    logger.info(f"odds:{odds}")
    logger.info(f"events:{events}")


def byte_stride():
    # バイトでもストライドは使える
    x = b"mongoose"
    logger.info(x[::-1])


def unicode_stride():
    # Unicodeでもストライドは使える
    x = "寿司"
    logger.info(x[::-1])


def unicode_encode_stride():
    # Unicodeをutf-8にエンコードしてからだと、ストライドは使えない
    x = "寿司"
    y = x.encode("utf-8")[::-1]
    logger.info(y)
    logger.info(y.decode("utf-8"))


def kind_of_stride():
    # ストライドの負、及びストライドとスライスの兼用は読みにくい
    x = ["a", "b", "c", "d", "e", "f", "g", "h"]
    logger.info(x[::2])
    logger.info(x[::-2])
    logger.info(x[2::2])
    logger.info(x[-2::-2])
    logger.info(x[-2:2:-2])
    logger.info(x[2:2:-2])


def split_stride_and_slice():
    # ストライドとスライスは実行時間とメモリに余裕があれば、分けて書く
    x = ["a", "b", "c", "d", "e", "f", "g", "h"]
    y = x[::2]
    z = y[1:-1]
    logger.info(z)


# 13 スライスではなくcatch-allアンパックを使う


def log_old_car():
    car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]
    car_age_descending = sorted(car_ages, reverse=True)
    oldest, second_oldest, *others = car_age_descending
    logger.info(f"oldest:{oldest}")
    logger.info(f"second_oldest:{second_oldest}")
    logger.info(f"others:{others}")


def log_oldest_youngest():
    car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]
    car_age_descending = sorted(car_ages, reverse=True)
    oldest, *others, youngest = car_age_descending
    logger.info(f"oldest:{oldest}")
    logger.info(f"youngest:{youngest}")
    logger.info(f"others:{others}")


def log_best_car():
    # あまりおすすめはできないが、複数のレベルのネストの場合、複数のcatch-allアンパックが使える
    car_inventory = {
        "Downtown": ("Silver Shadow", "Pinto", "DMC"),
        "Airport": ("Skyline", "Viper", "Gremlin", "Nova"),
    }
    ((loc1, (best1, *rest1)), (loc2, (best2, *rest2))) = car_inventory.items()
    logger.info(f"Best at {loc1} is {best1} , {len(rest1)} others")
    logger.info(f"Best at {loc2} is {best2} , {len(rest2)} others")


def short_catch_all_unpack():
    # catch-allアンパックは、リストの長さがアンパック先よりも短いの場合、
    # 空のリストを返す
    a, *b = [1]
    logger.info(f"a:{a}")
    logger.info(f"b:{b}")


def iter_catch_all_unpack():
    # catch-allアンパックは、イテレータの場合、イテレータが空になるまでアンパックする
    # ただ、listで静的に代入する方が簡単
    a, *b = iter(range(3))
    logger.info(f"a:{a}")
    logger.info(f"b:{b}")


def generate_csv():
    # Standard Library
    import datetime
    import random

    yield ("Date", "Make", "Model", "Year", "Price")
    makes = ["Toyota", "Honda", "Ford", "Chevrolet", "BMW"]
    models = ["Camry", "Accord", "Mustang", "Corvette", "X5"]
    years = list(range(2010, 2023))
    for i in range(200):
        date = datetime.date.today() - datetime.timedelta(days=i)
        make = random.choice(makes)
        model = random.choice(models)
        year = random.choice(years)
        price = random.randint(10000, 50000)

        yield (date.strftime("%Y-%m-%d"), make, model, year, price)


def not_good_generator_catch_all():
    all_csv_rows = list(generate_csv())
    header = all_csv_rows[0]
    rows = all_csv_rows[1:]
    logger.info(f"header:{header}")
    logger.info(f"row count:{len(rows)}")


def good_generator_catch_all():
    all_csv_rows = list(generate_csv())
    heder, *rows = all_csv_rows
    logger.info(f"header:{heder}")
    logger.info(f"row count:{len(rows)}")


# 14 key引数を使い、複雑な基準でソートする
class Tool:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f"Tool({self.name!r}, {self.weight})"


def sort_by_name():
    tools = [
        Tool("level", 3.5),
        Tool("hammer", 1.25),
        Tool("screwdriver", 0.5),
        Tool("chisel", 0.25),
    ]
    # key引数を使うと、ソートの基準を変更できる
    logger.info(f"sort_by_name:{sorted(tools, key=lambda x: x.name)}")


def tuple_sort_stand():
    saw = (5, "saw")
    jackhammer = (20, "jackhammer")
    # タプルの場合、先頭の要素から順に比較する
    assert not (saw < jackhammer)

    drill = (10, "drill")
    sander = (10, "sander")
    assert drill[0] == sander[0]  # 同じ重さ
    assert drill[1] < sander[1]  # 英字順で比較
    assert drill < sander  # よってdillが前にくる


def sort_weight_name():
    tools = [
        Tool("level", 3.5),
        Tool("hammer", 1.25),
        Tool("screwdriver", 0.5),
        Tool("chisel", 0.5),
    ]
    # 重さが同じ場合、名前でソートする
    logger.info(f"sort_weight_name:{sorted(tools, key=lambda x: (x.weight, x.name))}")


def sort_weight_name_reverse():
    tools = [
        Tool("level", 3.5),
        Tool("hammer", 1.25),
        Tool("screwdriver", 0.5),
        Tool("chisel", 0.5),
    ]
    # 重さが同じ場合、名前でソートする
    # 逆順にする場合、reverse=Trueを指定する
    logger.info(f"sort_weight_name_reverse:{sorted(tools, key=lambda x: (x.weight, x.name), reverse=True)}")


def sort_minus_weight_name():
    tools = [
        Tool("level", 3.5),
        Tool("hammer", 1.25),
        Tool("screwdriver", 0.5),
        Tool("chisel", 0.5),
    ]
    # 重さが同じ場合、名前でソートする
    # 逆順にする場合、マイナスでも指定できる。ただし、数字以外は使えない
    logger.info(f"sort_minus_weight_name:{sorted(tools, key=lambda x: (-x.weight, x.name))}")
