from student import Student
from teacher import Teacher


class School:
    def __init__(self, title: str):
        self.__title = title
        self.__students = []
        self.__teachers = []

    def add_student(self, student: Student) -> bool:
        if not isinstance(student, Student):
            print('Ошибка. Некорректные данные')

            return False

        self.__students.append(student)

        return True

    def add_teacher(self, teacher: Teacher) -> bool:
        if not isinstance(teacher, Teacher):
            print('Ошибка. Некорректные данные')

            return False

        self.__teachers.append(teacher)

        return True

    def find_student_by_name(self, name: str):
        for student in self.__students:
            if student.get_name().lower() == name.lower():
                return student

        return None

    def find_teacher_by_name(self, name: str):
        for teacher in self.__teachers:
            if teacher.get_name().lower() == name.lower():
                return teacher

        return None

    def show_all_students(self):
        if not self.__students:
            print('Список учеников пуст')
        else:
            for student in self.__students:
                print(student.get_info())

    def show_all_teachers(self):
        if not self.__teachers:
            print('Список преподавателей пуст')
        else:
            for teacher in self.__teachers:
                print(teacher.get_info())
