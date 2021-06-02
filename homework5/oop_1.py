"""
Необходимо создать 3 класса и взаимосвязь между ними (Student, Teacher,
Homework)
Наследование в этой задаче использовать не нужно.
Для работы с временем использовать модуль datetime
1. Homework принимает на вход 2 атрибута: текст задания и количество дней
на это задание
Атрибуты:
    text - текст задания
    deadline - хранит объект datetime.timedelta с количеством
    дней на выполнение
    created - c точной датой и временем создания
Методы:
    is_active - проверяет не истекло ли время на выполнение задания,
    возвращает boolean
2. Student
Атрибуты:
    last_name
    first_name
Методы:
    do_homework - принимает объект Homework и возвращает его же,
    если задание уже просрочено, то печатет 'You are late' и возвращает None
3. Teacher
Атрибуты:
     last_name
     first_name
Методы:
    create_homework - текст задания и количество дней на это задание,
    возвращает экземпляр Homework
    Обратите внимание, что для работы этого метода не требуется сам объект.
PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
from datetime import datetime, timedelta


class Homework:
    def __init__(self, text, deadline):
        """Homework class constructor
        :param text: homework text
        :param deadline: amount of days after that homework will become invalid
        """
        self.text = text
        self.deadline = timedelta(days=deadline)
        self.created = datetime.now()

    def is_active(self):
        """Homework class method
        returns True if deadline is still available"""
        if self.deadline + self.created < datetime.now():
            return True
        else:
            return False


class Student:
    def __init__(self, first_name, last_name):
        """Student class constructor
        :param first_name: student's name
        :param last_name: student's surname
        """
        self.first_name = first_name
        self.last_name = last_name

    def do_homework(self, my_homework):
        """Class Student method
        accepts object Homework and returns it if 'is_active' is True"""
        if my_homework.is_active() is False:
            print("You are late")
            return None
        else:
            return my_homework


class Teacher:
    def __init__(self, first_name, last_name):
        """Teacher class constructor
        :param first_name: teacher's name
        :param last_name: teacher's surname
        """
        self.first_name = first_name
        self.last_name = last_name

    def create_homework(self, text, deadline):
        """Class Teacher method
        return object Homework"""
        return Homework(text, deadline)


if __name__ == "__main__":
    teacher = Teacher("Daniil", "Shadrin")
    student = Student("Roman", "Petrov")
    print(teacher.last_name)
    print(student.first_name)

    expired_homework = teacher.create_homework("Learn functions", 0)
    print(expired_homework.deadline)  # 0:00:00
    print(expired_homework.text)  # 'Learn functions
    print(expired_homework.created)  # Example: 2019-05-26 16:44:30.688762

    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too("create 2 simple classes", 5)
    print(oop_homework.deadline)  # 5 days, 0:00:00

    student.do_homework(oop_homework)
    print(student.do_homework(expired_homework))  # You are late

    new_homework = Homework("Do task1", 4)
    print(new_homework.is_active())
