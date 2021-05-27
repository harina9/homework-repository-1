import pytest

from homework6.oop_2 import *

opp_teacher = Teacher("Daniil", "Shadrin")
advanced_python_teacher = Teacher("Aleksandr", "Smetanin")

lazy_student = Student("Roman", "Petrov")
good_student = Student("Lev", "Sokolov")

oop_hw = opp_teacher.create_homework("Learn OOP", 1)
docs_hw = opp_teacher.create_homework("Read docs", 5)

result_1 = good_student.do_homework(oop_hw, "I have done this hw")
result_2 = good_student.do_homework(docs_hw, "I have done this hw too")
result_3 = lazy_student.do_homework(docs_hw, "done")


def test_not_homework_passed_in_homework_result():
    with pytest.raises(TypeError):
        result_4 = HomeworkResult(good_student, "fff", "Solution")


opp_teacher.check_homework(result_1)


def test_teachers_and_Teacher_class_have_common_data():
    temp_1 = opp_teacher.homework_done
    temp_2 = Teacher.homework_done
    temp_3 = advanced_python_teacher.homework_done
    assert temp_1 == temp_2 == temp_3


opp_teacher.check_homework(result_2)
opp_teacher.check_homework(result_3)


def test_reset_homework_results_for_particular_homework():
    Teacher.reset_results(oop_hw)
    assert Teacher.homework_done[oop_hw] == []


def test_reset_all_homework_results():
    advanced_python_teacher.reset_results()
    assert not advanced_python_teacher.homework_done


def test_DeadlineError():
    late_hw = opp_teacher.create_homework("Out of Date Task", 0)
    with pytest.raises(DeadlineError):
        lazy_student.do_homework(late_hw, "It was not possible to make it in time")


def test_second_entry_of_the_same_homework_result_is_not_possible():
    result_11 = good_student.do_homework(oop_hw, "Some irrelevant comment")
    advanced_python_teacher.check_homework(result_11)

    with pytest.raises(RepeatedResultError):
        opp_teacher.check_homework(result_11)
