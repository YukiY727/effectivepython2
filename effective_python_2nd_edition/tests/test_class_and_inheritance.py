# Standard Library
import logging
# First Party Library
from effective_python.class_and_inheritance import (
    BySubjectGradebook,
    Gradebook,
    SimpleGradebook,
    WeightedGradebook,
    increment_with_report,
    tuple_average_grade,
    tuple_average_grade_name,
    write_test_files,
    update_and_log_dict,
)

CLASS_AND_INHERITANCE = "effective_python.class_and_inheritance"


class TestIndex37:
    def test_simple_gradebook(self):
        book = SimpleGradebook()
        book.add_student("Isaac Newton")
        book.report_grade("Isaac Newton", 90)
        book.report_grade("Isaac Newton", 110)
        assert book.average_grade("Isaac Newton") == 100

    def test_by_subject_gradebook(self):
        book = BySubjectGradebook()
        book.add_student("Albert Einstein")
        book.report_grade("Albert Einstein", "Math", 75)
        book.report_grade("Albert Einstein", "Math", 65)
        book.report_grade("Albert Einstein", "Gym", 90)
        book.report_grade("Albert Einstein", "Gym", 95)
        assert book.average_grade("Albert Einstein") == 81.25

    def test_weighted_gradebook(self):
        book = WeightedGradebook()
        book.add_student("Albert Einstein")
        book.report_grade("Albert Einstein", "Math", 75, 0.05)
        book.report_grade("Albert Einstein", "Math", 65, 0.15)
        book.report_grade("Albert Einstein", "Gym", 90, 0.40)
        book.report_grade("Albert Einstein", "Gym", 95, 0.40)
        assert book.average_grade("Albert Einstein") == 87.5

    def test_tuple_average_grade(self):
        assert tuple_average_grade() == 89.5

    def test_tuple_average_grade_name(self):
        assert tuple_average_grade_name() == 89.5

    def test_gradebook(self):
        book = Gradebook()
        albert = book.get_student("Albert Einstein")
        math = albert.get_subject("Math")
        math.report_grade(72, 0.05)
        math.report_grade(65, 0.15)
        math.report_grade(70, 0.80)
        gym = albert.get_subject("Gym")
        gym.report_grade(100, 0.40)
        gym.report_grade(85, 0.60)
        assert albert.average_grade() == 80.175


class TestIndex38:
    def test_update_and_log_dict(self, caplog):
        update_and_log_dict()
        assert (
            CLASS_AND_INHERITANCE,
            logging.INFO,
            "Before: {'green': 12, 'blue': 3}",
        ) in caplog.record_tuples

        assert (
            CLASS_AND_INHERITANCE,
            logging.INFO,
            "After: {'blue': 20, 'green': 12, 'orange': 9, 'red': 5}",
        ) in caplog.record_tuples

        assert (CLASS_AND_INHERITANCE, logging.INFO, "Key added") in caplog.record_tuples

    def test_increment_with_report(self):
        current = {"green": 12, "blue": 3}
        increments = {
            ("red", 5),
            ("blue", 17),
            ("orange", 9),
        }
        _, added_count = increment_with_report(current, increments)
        assert added_count == 2

# class TestIndex39:
#     def test_map_reduce(self):
        
        