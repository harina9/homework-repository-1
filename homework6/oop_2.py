"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную
1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)
HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'
    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания
2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.
3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования
4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.
    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.
PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""


import datetime
from collections import defaultdict


class DeadlineError(Exception):
    """You are late"""


class RepeatedResultError(Exception):
    """This homework result has been accepted previously"""


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Student(Person):
    def do_homework(self, homework, result):
        if homework.is_active():
            return HomeworkResult(self, homework, result)
        else:
            raise DeadlineError("You are late")


class Teacher(Person):
    homework_done = defaultdict(list)

    @staticmethod
    def create_homework(*args):
        return Homework(*args)

    def check_homework(self, homework_result):

        if not isinstance(homework_result, HomeworkResult):
            raise TypeError("You gave a not HomeworkResult object")

        if homework_result in self.homework_done[homework_result.homework]:
            raise RepeatedResultError(
                "This homework result has been accepted previously"
            )

        if len(homework_result.solution) > 5:
            self.homework_done[homework_result.homework].append(homework_result)
            return True
        else:
            return False

    @classmethod
    def reset_results(cls, homework=None):
        if homework and isinstance(homework, Homework):
            cls.homework_done[homework].clear()
        else:
            cls.homework_done.clear()


class Homework:
    def __init__(self, task_text, task_timedelta):
        self.text = task_text
        self.created = datetime.datetime.now()
        self.deadline = datetime.timedelta(days=task_timedelta)

    def is_active(self):
        """returns True if deadline is not passed, False otherwise"""
        return datetime.datetime.now() < self.created + self.deadline


class HomeworkResult:
    def __init__(self, author, homework, solution):
        self.author = author

        if isinstance(homework, Homework):
            self.homework = homework
        else:
            raise TypeError("You gave a not Homework object")

        self.solution = solution
        self.created = datetime.datetime.now()
