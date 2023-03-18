# Standard Library
import logging

logger = logging.getLogger(__name__)

# 19 複数の返り値では、4個以上の変数なら決してアンパックしない


def get_stats(numbers: list[int]):
    minimum = min(numbers)
    maximum = max(numbers)
    logger.info(f"minimum: {minimum}, maximum: {maximum}")
    return minimum, maximum


def get_avg_ratio(numbers: list[int]):
    average = sum(numbers) / len(numbers)
    scaled = [x / average for x in numbers]
    scaled.sort(reverse=True)
    longest, *middle, shortest = scaled
    logger.info(f"longest: {longest:>4.0%}, shortest: {shortest:>4.0%}")


def get_starts_many(numbers: list[int]):
    minimum = min(numbers)
    maximum = max(numbers)
    count = len(numbers)
    average = sum(numbers) / count
    sorted_numbers = sorted(numbers)
    middle = count // 2
    if count % 2 == 0:
        lower = sorted_numbers[middle - 1]
        upper = sorted_numbers[middle]
        median = (lower + upper) / 2
    else:
        median = sorted_numbers[middle]
    logger.info(f"Min: {minimum}, Max: {maximum}")
    logger.info(f"Count: {count}, Average: {average}, Median: {median}")
    # 返り値の順序を誤りやすい
    # 呼び出す時にPEP8で改行しなければならず、可読性が悪い
    return minimum, maximum, count, average, median


# 20 Noneを返すのではなく、例外を発生させる


def careful_divide_use_none(a: float, b: float) -> float | None:
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    if not result:
        logger.warning("Invalid inputs")


def careful_divide_return_bool_and_value(a: float, b: float) -> tuple[bool, float]:
    # 返り値を複数返しているのがわかりにくい
    try:
        return True, a / b
    except ZeroDivisionError:
        return False, 0.0


def careful_divide_value_error(a: float, b: float) -> float:
    """Divide a by b.

    Args:
        a (float)
        b (float)

    Raises:
        ValueError: when the inputs cannot be divided

    Returns:
        float: a / b
    """
    # 型付ができているため、bugを回避しやすい
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError("Invalid inputs") from e


def check_divide_value_error(a: float, b: float) -> None:
    # 返り値を確認する必要がない
    try:
        result = careful_divide_value_error(a, b)
    except ValueError:
        logger.error("Invalid inputs")
    else:
        logger.info(f"Result: {result:.1f}")


# 21. クロージャが変数スコープとどう関わるかを把握しておく


def sort_priority1(numbers: list[int], group: set[int]) -> None:
    # 以下の理由で動く
    # 1. pythonがクロージャをサポートしている
    #  クロージャとは、定義されたスコープの変数を参照する関数
    #  これにより、helper関数がsort_priority1関数のローカル変数groupを参照できる
    # 2. pythonでは関数がファーストクラスオブジェクトであるから
    #  つまり、直接参照でき、変数に代入したり、関数の引数に渡したり、if文の条件式に使ったりできる
    #  sortメッソどがクロージャ関数をkey引数として受け取ることができる
    # 3. pythonでは、タプルを含めたシーケンスの比較に特別な規則を持つ。
    # . 最初にインデックス0の要素を比較し、同じならインデックス1の要素を比較する
    #  これにより、helperクロージャの返り値がソート順で異なるグループになるようにできる。
    def helper(x: int) -> tuple[int, int]:
        if x in group:
            return (0, x)
        return (1, x)

    numbers.sort(key=helper)


def sort_priority2(numbers: list[int], group: set[int]) -> bool:
    # 優先度が高い要素があったかのフラグ
    found = False

    def helper(x: int) -> tuple[int, int]:
        if x in group:
            # pythonのインタープリタは、以下の順で参照する
            # 1. 現在の関数のスコープ
            # 2. (他の関数の中にある場合のように)外側のスコープ
            # 3. コードを含むモジュールのスコープ(グローバルスコープ)
            # 4. (lenやstrのような)組み込みスコープ
            # 下のfoundは、クロージャでの代入となり、helper内の新たな変数となる。
            found = True
            return (0, x)
        return (1, x)

    numbers.sort(key=helper)
    return found


def sort_priority3(numbers: list[int], group: set[int]) -> bool:
    found = False

    def helper(x: int) -> tuple[int, int]:
        # nonlocalを使うことで、外側のスコープの変数を参照できる
        # nonlocalは、グローバルスコープまでは行かない
        # ただ、あまり大きな関数では、使わない方がいい
        nonlocal found
        if x in group:
            found = True
            return (0, x)
        return (1, x)

    numbers.sort(key=helper)
    return found


class Sorter:
    def __init__(self, group: set[int]) -> None:
        self.group = group
        self.found = False

    def __call__(self, x: int) -> tuple[int, int]:
        if x in self.group:
            self.found = True
            return (0, x)
        return (1, x)


def sort_priority4(numbers: list[int], group: set[int]) -> None:
    sorter = Sorter(group)
    numbers.sort(key=sorter)
    return sorter.found


# 22. 可変長市引数を使って、見た目をすっきりさせる


def log1(message: str, values: list[int]) -> None:
    # valuesには、何か入れなければならない
    if values:
        values_str = ", ".join(str(x) for x in values)
        logger.info(f"{message}: {values_str}")
    else:
        logger.info(message)


def log2(message: str, *values: tuple[int]) -> None:
    # valuesには、何も入れなくても良い
    # ただし、valuesはタプルになる
    # 呼び出しもとで、引数を増やせてしまう
    if values:
        values_str = ", ".join(str(x) for x in values)
        logger.info(f"{message}: {values_str}")
    else:
        logger.info(message)


def my_func(*args: tuple[int]) -> None:
    # *argsはタプルになる
    logger.info(args)


def log3(sequence: list[int], message: str, *values: tuple[int]) -> None:
    # *valuesはタプルになる
    # キーワード引数を使うことで、bugを防ぐことができる
    if values:
        values_str = ", ".join(str(x) for x in values)
        logger.info(f"{sequence} - {message}: {values_str}")
    else:
        logger.info(f"{sequence} - {message}")


# 23 キーワード引数にオプションの振る舞いを与える


# 1. 初めて見る人が、関数の振る舞いを理解しやすい
def remainder(number: int, divisor: int) -> int:
    return number % divisor


def log_parameters(**kwargs: dict[str, int]) -> None:
    for key, value in kwargs.items():
        logger.info(f"{key} = {value}")


# 2. デフォルト値の振る舞いをすることができる
def flow_rate(weight_diff: int, time_diff: int, period: int = 1) -> float:
    return (weight_diff / time_diff) * period


# 3. 新しい引数が追加されても、デフォルト値を設定しておけば、呼び出しもとのコードを変更する必要がない
def flow_rate_add(weight_diff: int, time_diff: int, period: int = 1, units_per_kg: int = 1) -> float:
    return ((weight_diff * units_per_kg) / time_diff) * period


# 24 動的なデフォルト引数を指定する時は、Noneとdocstringを使う

# Standard Library
from datetime import datetime
from typing import Optional


def log_time(message: str, when: Optional[datetime] = None) -> None:
    """Log a message with a timestamp.

    Args:
        message: Message to log.
        when: datetime of when the message occurred.
            Defaults to the present time.
    """
    if when is None:
        when = datetime.now()
    logger.info(f"{when}: {message}")


# Standard Library
import json


def json_decode_not_good(data: str, default: dict[str, int] = {}) -> dict[str, int]:
    """Load JSON data from a string.

    Args:
        data: JSON data to decode.
        default: Value to return if decoding fails.
    """
    # if default is None:
    #     default = {}
    try:
        return json.loads(data)
    except ValueError:
        return default


def json_decode_good(data: str, default: dict[str, int] = None) -> dict[str, int]:
    """Load JSON data from a string.

    Args:
        data: JSON data to decode.
        default: Value to return if decoding fails.
            Defaults to an empty dictionary.
    """
    if default is None:
        default = {}
    try:
        return json.loads(data)
    except ValueError:
        return default


# 25. キーワード専用引数と位置専用引数で明確さを高める


def safe_division_a(number: int, divisor: int, ignore_overflow: bool, ignore_zero_division: bool) -> float:
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float("inf")
        else:
            raise


def safe_division_b(
    number: int, divisor: int, ignore_overflow: bool = False, ignore_zero_division: bool = False
) -> float:
    # デフォルト値を設定すれば、例外フラグをオーバーライドして使えば良い
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float("inf")
        else:
            raise


def safe_division_c(
    number: int, divisor: int, *, ignore_overflow: bool = False, ignore_zero_division: bool = False
) -> float:
    # *を使うことで、位置引数のおわりと、キーワード専用引数の始まりを明確にする
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float("inf")
        else:
            raise


def safe_division_d(
    numerator: int, denominator: int, /, *, ignore_overflow: bool = False, ignore_zero_division: bool = False
) -> float:
    # /を使うことで、位置専用引数の終わりを明確にする
    try:
        return numerator / denominator
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float("inf")
        else:
            raise


def safe_division_e(
    numerator: int,
    denominator: int,
    /,
    ndigits: int = 10,
    *,
    ignore_overflow: bool = False,
    ignore_zero_division: bool = False,
) -> float:
    # /と*の間の引数は位置引数でもキーワード引数でも使える(pythonの関数の引数のデフォルト)
    try:
        fraction = numerator / denominator
        return round(fraction, ndigits)
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float("inf")
        else:
            raise


# 26. functools.wrapsを使って関数デコレータを定義する


def trace_a(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f"{func.__name__}({args!r}, {kwargs!r}) -> {result!r}")

        return result

    return wrapper


@trace_a
def fibonacci_a(n):
    if n in (0, 1):
        return n
    return fibonacci_a(n - 2) + fibonacci_a(n - 1)


# Standard Library
from functools import wraps


def trace_b(func):
    @wraps(func)  # これを使うことで、デコレータを使う前の関数の情報を保持する
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f"{func.__name__}({args!r}, {kwargs!r}) -> {result!r}")

        return result
    return wrapper

@trace_b
def fibonacci_b(n):
    if n in (0, 1):
        return n
    return fibonacci_b(n - 2) + fibonacci_b(n - 1)
