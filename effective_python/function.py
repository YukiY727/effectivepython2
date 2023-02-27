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
    # 型付ができているため、bugを回避しやすい
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError("Invalid inputs") from e
