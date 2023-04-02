# Standard Library
import logging
from typing import Iterator

# 27. mapやfilterの代わりにリスト内包表記を使う
logger = logging.getLogger(__name__)


def square_endnotes_list(int_list: list[int]) -> list[int]:
    """Return the square of each number in the list."""
    return [x**2 for x in int_list]


def even_squares_list(int_list: list[int]) -> list[int]:  # 簡単なフィルタリングも簡単に書ける
    return [x**2 for x in int_list if x % 2 == 0]


def even_squares_dict(int_list: list[int]) -> dict[int:int]:  # 辞書にも使える
    return {x: x**2 for x in int_list if x % 2 == 0}


def threes_cubed_set(int_list: list[int]) -> set[int]:  # 集合にも使える
    return {x**3 for x in int_list if x % 3 == 0}


# 28. 内包表記では、3つ以上の式を避ける


def double_list_endnotes(double_int_list: list[list[int]]) -> list[int]:
    return [x for rows in double_int_list for x in rows]


def double_list_square_endnotes(double_int_list: list[list[int]]) -> list[list[int]]:
    return [[x**2 for x in row] for row in double_int_list]


def triple_list_endnotes(triple_list: list[list[list[int]]]) -> list[int]:  # 読みづらい
    return [x for sublist1 in triple_list for sublist2 in sublist1 for x in sublist2]


def triple_list_indent(triple_list: list[list[list[int]]]) -> list[int]:  # 一つ前と比べたらまだマシ
    flat = []
    for sublist1 in triple_list:
        for sublist2 in sublist1:
            flat.extend(sublist2)
    return flat


def endnotes_filter_and(int_list: list[int]) -> list[int]:
    return [x for x in int_list if x > 4 and x % 2 == 0]


def endnotes_filter_if(int_list: list[int]) -> list[int]:
    return [x for x in int_list if x > 4 if x % 2 == 0]


def division_three_and_sum_10_over(double_int_list: list[list[int]]) -> list[list[int]]:  # 読みづらい
    return [[x for x in row if x % 3 == 0] for row in double_int_list if sum(row) >= 10]


# 29. 代入式を使い内包表記での繰り返しの作業をなくす


def get_batches(count: int, size: int) -> int:
    return count // size


def cal_batches_indent(stock: dict[str:int], order: list[str]) -> dict[str, int]:
    result = {}
    for name in order:
        count = stock.get(name, 0)
        batches = get_batches(count, 8)
        if batches:
            result[name] = batches
    return result


def cal_batches_endnotes(stock: dict[str:int], order: list[str]) -> dict[str, int]:
    return {name: get_batches(stock.get(name, 0), 8) for name in order if get_batches(stock.get(name, 0), 8)}


def cal_batches_endnotes_walras(stock: dict[str:int], order: list[str]) -> dict[str, int]:
    return {name: batches for name in order if (batches := get_batches(stock.get(name, 0), 8))}


def endnotes_walras_leak(stock: dict[str:int]):
    half = [(squared := last**2) for count in stock.values() if (last := count // 2) > 10]
    logger.info(f"Last item of {half} is {last} ** 2 = {squared}")  # ウォルラスではリークが起きる


def cal_batches_iterator(stock: dict[str:int], order: list[str]) -> Iterator[str:int]:
    return ((name, batches) for name in order if (batches := get_batches(stock.get(name, 0), 8)))


# 30. listを返さずに、ジェネレータを返すことを考える


def index_words_list(text: str) -> list[int]:
    # 1.コードが読みづらい
    # 2.メモリを消費する
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == " ":
            result.append(index + 1)
    return result


def index_words_iterator(text: str) -> Iterator[int]:
    # ジェネレータを使うと、コードが簡潔になる
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == " ":
            yield index + 1


# Standard Library
# 31. 引数に対してイテレータを使う時には確実さを優先する
import os
from pathlib import Path
from typing import Callable


def normalize(numbers: list[float]) -> list[float]:
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


def read_visits(data_path: str) -> Iterator[int]:
    with open(data_path) as f:
        for line in f:
            yield int(line)


def read_visits_iterator_and_normalize() -> list[float]:
    data_path = os.path.join(Path(__file__).parents[0], "data", "endnotes_and_generators", "my_numbers.txt")
    it = read_visits(data_path)
    percentages = normalize(it)  # StopIteration例外がnormalizeで発生している
    return percentages


def normalize_copy(numbers: list[float]) -> list[float]:
    numbers = list(numbers)  # コピーを作る。ただ、copyが巨大になる可能性がある。
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


def read_visits_iterator_and_normalize_copy() -> list[float]:
    data_path = os.path.join(Path(__file__).parents[0], "data", "endnotes_and_generators", "my_numbers.txt")
    it = read_visits(data_path)
    percentages = normalize_copy(it)
    return percentages


def normalize_func(get_iter: Callable[[], Iterator[float]]) -> list[float]:
    total = sum(get_iter())  # 新しいイテレータを作る
    result = []
    for value in get_iter():
        percent = 100 * value / total
        result.append(percent)
    return result


def read_visits_iterator_and_normalize_func() -> list[float]:
    data_path = os.path.join(Path(__file__).parents[0], "data", "endnotes_and_generators", "my_numbers.txt")
    percentages = normalize_func(lambda: read_visits(data_path))  # lambda式を渡さなければいけない
    return percentages


class ReadVisits:
    def __init__(self, data_path: str):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


def read_visits_iterator_and_normalize_class() -> list[float]:
    data_path = os.path.join(Path(__file__).parents[0], "data", "endnotes_and_generators", "my_numbers.txt")
    visits = ReadVisits(data_path)
    percentages = normalize(visits)
    return percentages


# Standard Library
from collections.abc import Iterator


def normalize_defensive(numbers: list[float]) -> list[float]:
    if isinstance(numbers, Iterator):  # イテレータは良くない
        raise TypeError("Must supply a container")
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


def read_visits_iterator_and_normalize_defensive_class() -> list[float]:
    data_path = os.path.join(Path(__file__).parents[0], "data", "endnotes_and_generators", "my_numbers.txt")
    visits = ReadVisits(data_path)
    percentages = normalize_defensive(visits)
    return percentages


def read_visits_iterator_and_normalize_defensive_class_iter():
    data_path = os.path.join(Path(__file__).parents[0], "data", "endnotes_and_generators", "my_numbers.txt")
    visits = ReadVisits(data_path)
    visits = iter(visits)
    percentages = normalize_defensive(visits)
    return percentages


# 32. 大きなリスト内包表記にはジェネレータ式を考える
def endnotes_value():
    value = [
        len(x)
        for x in open(os.path.join(Path(__file__).parents[0], "data", "endnotes_and_generators", "my_numbers.txt"))
    ]
    return value


def generator_value():
    it = (
        len(x)
        for x in open(os.path.join(Path(__file__).parents[0], "data", "endnotes_and_generators", "my_numbers.txt"))
    )
    return it


def generator_value_square():
    it = (
        (len(x), int(x) ** 2)
        for x in open(os.path.join(Path(__file__).parents[0], "data", "endnotes_and_generators", "my_numbers.txt"))
    )
    return it


# 33. yield fromで複数のジェネレータを作る
def move(period, speed):
    for _ in range(period):
        yield speed


def pause(delay):
    for _ in range(delay):
        yield 0


def animate():
    for delta in move(4, 5.0):
        yield delta
    for delta in pause(3):
        yield delta
    for delta in move(2, 3.0):
        yield delta


def render(delta):
    logger.info(f"delta: {delta:.1f}")


def run_animate(func):
    # ジェネレータがいれこになっていて、わかりづらい
    for delta in func():
        render(delta)


def animate_composed():
    yield from move(4, 5.0)
    yield from pause(3)
    yield from move(2, 3.0)


# import timeit

# def child():
#     for i in range(10_0000):
#         yield i
# def slow():
#     for i in child():
#         yield i
# def fast():
#     yield from child()

# baseline = timeit.timeit(
#     stmt= "for _ in slow(): pass",
#     globals=globals(),
#     number=50)
# print(f"baseline: {baseline:.2f}s")

# comparison = timeit.timeit(
#     stmt= "for _ in fast(): pass",
#     globals=globals(),
#     number=50)
# print(f"comparison: {comparison:.2f}s")

# reduction = (baseline - comparison) / baseline
# print(f"{reduction:.1%} less time")

# 34. sendでジェネレータにデータを注入するのは避ける

# Standard Library
import math
from collections.abc import Generator


def wave(amplitude, steps):
    step_size = 2 * math.pi / steps
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        output = amplitude * fraction
        yield output


def transmit(output):
    if output is None:
        logger.info("Output is None")
    else:
        logger.info(f"Output: {output:>5.1f}")


def run_transmit(it):
    for output in it:
        transmit(output)


def my_generator():
    received = yield 1
    logger.info(f"received = {received}")


def my_generator_one_way():
    it = iter(my_generator())
    output = next(it)  # 最初のジェネレータの出力を取得
    logger.info(f"output = {output}")
    try:
        next(it)  # 終わるまでジェレネータを回す
    except StopIteration:
        pass
    else:
        assert False


def my_generator_send():
    it = iter(my_generator())
    output = it.send(None)  # receivedにNoneを送信outputには1が入る
    logger.info(f"output = {output}")
    try:
        it.send("hello")  # receivedにhelloを送信
    except StopIteration:
        pass


def wave_modulating(steps: int) -> Generator[int]:
    step_size = 2 * math.pi / steps
    amplitude = yield  # 最初の振れ幅を受け取る
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        output = amplitude * fraction
        amplitude = yield output  # 次の振れ幅を受け取る


def run_modulating(it: Generator) -> None:
    amplitudes: list[None | int] = [None, 7, 7, 7, 2, 2, 2, 2, 10, 10, 10, 10, 10]
    for amplitude in amplitudes:
        output = it.send(amplitude)  # yieldとsendの関係は、初めての人にはわかりづらい
        transmit(output)


def complex_wave():
    yield from wave(3.0, 3)
    yield from wave(3.0, 3)


def complex_wave_modulating() -> Generator[int]:
    yield from wave_modulating(3)  # wave_modulatingのジェネレータが呼び出されるたびに、amplitudeがNoneになる
    yield from wave_modulating(4)
    yield from wave_modulating(5)


def wave_cascading(amplitude_it: Iterator[int], steps: int) -> Generator[int]:
    step_size = 2 * math.pi / steps
    for amplitude in amplitude_it:
        for step in range(steps):
            radians = step * step_size
            fraction = math.sin(radians)
            amplitude = next(amplitude_it)  # 次の振れ幅を取得
            output = amplitude * fraction
            yield output


def complex_wave_cascading(amplitude_it: Iterator[int]) -> Generator[int]:
    yield from wave_cascading(amplitude_it, 3)
    yield from wave_cascading(amplitude_it, 4)
    yield from wave_cascading(amplitude_it, 5)


def run_cascading():
    amplitudes = [7, 7, 7, 2, 2, 2, 2, 10, 10, 10, 10, 10]
    it = complex_wave_cascading(iter(amplitudes))
    for amplitude in amplitudes:
        output = next(it)
        transmit(output)


# 35. ジェネレータでthrowによる状態遷移を起こすのは避ける
class MyError(Exception):
    pass


def my_generator1():
    yield 1
    yield 2
    yield 3


def run_my_generator1():
    it = my_generator1()
    logger.info(next(it))
    logger.info(next(it))
    logger.info(it.throw(MyError, "error message"))


def my_generator2():
    yield 1

    try:
        yield 2
    except MyError:
        logger.info("got MyError")

    else:
        yield 3

    yield 4


def run_my_generator2():
    it = my_generator2()
    logger.info(next(it))
    logger.info(next(it))
    logger.info(it.throw(MyError, "error message"))


class Reset(Exception):
    pass


def timer(period):
    current = period
    while current:
        current -= 1
        try:
            yield current
        except Reset:
            current = period


RESETS = [False, False, False, True, False, True, False, False, False, False, False, False, False, False]


def check_for_reset():
    return RESETS.pop(0)


def announce(remaining):
    logger.info(f"{remaining} seconds remaining")


def run_timer():
    # インデントの深さがさまざまで、読みにくい
    it = timer(4)
    while True:
        try:
            if check_for_reset():
                current = it.throw(Reset)
            else:
                current = next(it)
        except StopIteration:
            break
        else:
            announce(current)


class Timer:
    def __init__(self, period) -> None:
        self.current = period
        self.period = period

    def reset(self):
        self.current = self.period

    def __iter__(self):
        while self.current:
            self.current -= 1
            yield self.current


def run_timer_class():
    # 明らかに読みやすい
    timer = Timer(4)
    for remaining in timer:
        if check_for_reset():
            timer.reset()
        announce(remaining)


# Standard Library
# 36. イテレータとジェネレータの作業では、itertoolsを使う
import itertools


def iter_chain():
    it = itertools.chain([1, 2, 3], [4, 5, 6])
    return list(it)


def iter_repeat():
    it = itertools.repeat(7, 3)
    return list(it)


def iter_cycle():
    it = itertools.cycle([1, 2])
    return [next(it) for _ in range(3)]


def iter_tee():
    # 1つのイテレータを分割して、第二引数で指定した数だけイテレータを作る
    it1, it2 = itertools.tee([1, 2, 3], 2)
    return list(it1), list(it2)


def iter_zip_longest():
    keys = ["one", "two", "three"]
    values = [1, 2]
    normal = list(zip(keys, values))
    logger.info(f"zip: {normal}")

    it = itertools.zip_longest(keys, values, fillvalue="nope")
    longest = list(it)
    logger.info(f"zip_longest: {longest}")


def iter_islice():
    values = [1, 2, 3, 4, 5, 6]
    first_three = itertools.islice(values, 3)
    logger.info(f"first three: {list(first_three)}")

    middle_odds = itertools.islice(values, 0, 5, 2)
    logger.info(f"middle odds: {list(middle_odds)}")


def iter_takewhile():
    values = [1, 2, 3, 4, 5, 6]
    less_than_three = itertools.takewhile(lambda x: x < 3, values)
    logger.info(f"less than three: {list(less_than_three)}")


def iter_dropwhile():
    values = [1, 2, 3, 4, 5, 6]
    upward_than_three = itertools.dropwhile(lambda x: x < 3, values)
    logger.info(f"upward than three: {list(upward_than_three)}")


def iter_filterfalse():
    values = [1, 2, 3, 4, 5, 6]
    evens = itertools.filterfalse(lambda x: x % 2, values)
    logger.info(f"filter false: {list(evens)}")


def iter_accumulate():
    values = [1, 2, 3, 4, 5, 6]
    running_total = itertools.accumulate(values)
    logger.info(f"accumulate: {list(running_total)}")

    def sum_modulo_5(x, y):
        return (x + y) % 5

    modulo_reduce = itertools.accumulate(values, sum_modulo_5)

    logger.info(f"modulo : {list(modulo_reduce)}")


def iter_product():
    # カーネルの直積
    single = itertools.product([1, 2], repeat=2)
    logger.info(f"single: {list(single)}")

    multiple = itertools.product([1, 2], ["a", "b"])
    logger.info(f"multiple: {list(multiple)}")


def iter_permutations():
    # イテレータからN個の要素を取り出す順列を生成する
    it = itertools.permutations([1, 2, 3], 2)
    logger.info(f"permutations: {list(it)}")


def iter_combinations():
    # イテレータからN個の要素を取り出す組み合わせを生成する
    it = itertools.combinations([1, 2, 3], 2)
    logger.info(f"combinations: {list(it)}")


def iter_combinations_with_replacement():
    # combinationsと同じだが、同じ要素の組み合わせを許す
    it = itertools.combinations_with_replacement([1, 2, 3], 2)
    logger.info(f"combinations with replacement: {list(it)}")
