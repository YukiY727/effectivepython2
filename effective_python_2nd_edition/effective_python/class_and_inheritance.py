# Standard Library
from logging import getLogger

logger = getLogger(__name__)
# .37 組み込み型の深い入れ子にはせず、クラスを作成する


class SimpleGradebook:
    def __init__(self):
        self._grades: dict[str, list] = {}

    def add_student(self, name):
        self._grades[name] = []

    def report_grade(self, name, score):
        self._grades[name].append(score)

    def average_grade(self, name):
        grades = self._grades[name]
        return sum(grades) / len(grades)


# Standard Library
from collections import defaultdict


class BySubjectGradebook:
    # 少し、拡張しすぎだが、まだ読める
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = defaultdict(list)

    def report_grade(self, name, subject, score):
        by_subject: dict = self._grades[name]
        grade_list: list = by_subject[subject]
        grade_list.append(score)

    def average_grade(self, name):
        by_subject: dict = self._grades[name]
        total, count = 0, 0
        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)
        return total / count


class WeightedGradebook:
    # もう読めるものではない
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = defaultdict(list)

    def report_grade(self, name, subject, score, weight):
        by_subject: dict = self._grades[name]
        # このgrade_listが階層が深すぎて、読みにくい
        grade_list: list = by_subject[subject]
        grade_list.append((score, weight))

    def average_grade(self, name):
        by_subject: dict = self._grades[name]
        # 各教科の合計点と教科の総数を計算する
        total, count = 0, 0
        for subject, grades in by_subject.items():
            # 各教科の合計点と教科の総数を計算する
            subject_total, subject_count = 0, 0
            for score, weight in grades:
                # 各教科の合計点と教科の総数を計算する
                subject_total += score * weight
                subject_count += weight
            # 教科ごとの合計点と教科の総数を計算する
            total += subject_total
            count += subject_count
        # 全教科の合計点と教科の総数を計算する
        return total / count


def tuple_average_grade():
    # creates a list of tuples with grades and weight
    grades = []
    grades.append((95, 0.45))
    grades.append((85, 0.55))

    # calculate the total of the grades
    total = sum(score * weight for score, weight in grades)

    # calculate the total weight
    total_weight = sum(weight for _, weight in grades)

    # calculate the average grade
    average_grade = total / total_weight
    return average_grade


def tuple_average_grade_name():
    grades = []
    grades.append((95, 0.45, "Great job"))
    grades.append((85, 0.55, "Better next time"))
    total = sum(score * weight for score, weight, _ in grades)
    total_weight = sum(weight for _, weight, _ in grades)
    return total / total_weight


# Standard Library
from collections import namedtuple

# A student can have multiple subjects, and a subject can have multiple grades.
# A gradebook can have multiple students, and a student can have multiple subjects.

# The purpose of the code is to calculate the average grade of a student.
# The student's name is used as an argument to get_student(name).
# The context in which this code is used is in the school system,
# as the software that calculates the average grade of a student.

# Functions:
#   get_subject(name)
#   report_grade(score, weight)
#   average_grade()
#   get_student(name)
#   average_grade()

# Variables:
#   _grades
#   _subjects
#   _students

# Create a namedtuple type to store grades
Grade = namedtuple("Grade", ("score", "weight"))


# A Subject aggregates grades
class Subject:
    def __init__(self):
        self._grades: list[Grade] = []

    def report_grade(self, score: int, weight: int):
        self._grades.append(Grade(score, weight))

    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight


# A Student aggregates multiple subjects
class Student:
    def __init__(self) -> None:
        self._subjects = defaultdict(Subject)

    def get_subject(self, name):
        return self._subjects[name]

    def average_grade(self):
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count


# A Gradebook aggregates multiple students
class Gradebook:
    def __init__(self):
        self._students = defaultdict(Student)

    def get_student(self, name):
        return self._students[name]


# 38. 単純なインターフェースにはクラスの代わりに関数を使う


def log_missing():
    logger.info("Key added")
    return 0


def update_and_log_dict():
    current = {"green": 12, "blue": 3}
    increments = {
        ("red", 5),
        ("blue", 17),
        ("orange", 9),
    }
    # the feature can be decoupled by giving the log_missing function.
    result = defaultdict(log_missing, current)
    logger.info(f"Before: {dict(result)}")
    for key, amount in increments:
        result[key] += amount
    result = sorted(dict(result).items())
    logger.info(f"After: {dict(result)}")


def increment_with_report(current, increments):
    added_count = 0

    def missing():
        nonlocal added_count  # Stateful closure
        added_count += 1
        return 0

    result = defaultdict(missing, current)
    for key, amount in increments:
        result[key] += amount
    return result, added_count


class CountMissing:
    def __init__(self):
        self.added = 0

    def missing(self):
        self.added += 1
        return 0


def helper_increment_with_report(current, increments):
    # looking at the CountingMissing class by itself, it is not clear
    # when the missing method is called or how it is used until it is used in a defaltdict.
    counter = CountMissing()
    result = defaultdict(counter.missing, current)
    for key, amount in increments:
        result[key] += amount
    return result, counter.added


class BetterCountMissing:
    def __init__(self):
        self.added = 0

    def __call__(self):
        self.added += 1
        return 0


def helper_better_increment_with_report(current, increments):
    # By implementing __call__, we know that instances of the class may be used as function arguments.
    # It can tell the new reader that the purpose of the class is a closure that preserves the state.
    counter = BetterCountMissing()
    result = defaultdict(counter, current)
    for key, amount in increments:
        result[key] += amount
    return result, counter.added


# 39. @calssmethodポリルフィズムをtかって、オブジェクトをジェネリックに構築する


class InputData:
    def read(self):
        raise NotImplementedError


class PathInputData(InputData):
    def __init__(self, path):
        super.__init__()
        self.path = path

    def read(self):
        with open(self.path) as f:
            return f.read()


class Worker:
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError


class LineCountWorker(Worker):
    def map(self):
        data = self.input_data.read()
        self.result = data.count("¥n")

    def reduce(self, other):
        self.result += other.result


# Standard Library
import os


def generate_inputs(data_dir):
    for name in os.listdir(data_dir):
        yield PathInputData(os.path.join(data_dir, name))


def create_workers(input_list):
    workers = []
    for input_data in input_list:
        workers.append(LineCountWorker(input_data))
    return workers


# Standard Library
from threading import Thread


def execute(workers: list[LineCountWorker]):
    threads = [Thread(target=worker.map) for worker in workers]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    first, *rest = workers
    for worker in rest:
        first.reduce(worker)
    return first.result


def map_reduce(data_dir):
    inputs = generate_inputs(data_dir)
    workers = create_workers(inputs)
    return execute(workers)


# Standard Library
import random


def write_test_files():
    tempdir = "test_inputs"
    os.makedirs(tempdir)
    for i in range(3):
        with open(os.path.join(tempdir, str(i)), "w") as f:
            f.write("¥n" * 3)
    result = map_reduce(tempdir)
    logger.info(f"there are {result} lines")
