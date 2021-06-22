import datetime

import pytest

from homework5.oop_1 import Homework, Student, Teacher


def test_creating_homework():
    teacher = Teacher("Daniil", "Shadrin")
    expired_homework = teacher.create_homework("Learn functions", 0)
    assert isinstance(expired_homework, Homework)
    assert expired_homework.deadline == datetime.timedelta(0)
    assert expired_homework.text == "Learn functions"


def test_creating_function_from_method_and_using_it():
    teacher = Teacher("Daniil", "Shadrin")
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too("create 2 simple classes", 5)
    assert oop_homework.deadline == datetime.timedelta(days=5)
