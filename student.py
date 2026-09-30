from user import User


class Student(User):
    def __init__(self, name, surname, phone_number):
        super().__init__(name, surname, phone_number)

        self.__courses = []

    def sign_up_for_course(self, course_title: str) -> bool:
        is_valid = self.__is_valid_course_title(course_title)

        if is_valid:
            self.__courses.append(course_title)
            return True
        else:
            return False

    def __is_valid_course_title(self, course_title: str) -> bool:
        if not isinstance(course_title, str):
            return False
        if not course_title.strip():
            return False
        if course_title in self.__courses:
            return False

        return True
