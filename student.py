from user import User


class Student(User):
    def __init__(self, name, surname, phone_number):
        super().__init__(name, surname, phone_number)

        self.__courses = []
        self.__COURSES_SEPARATOR = ', '

    def sign_up_for_course(self, course_title: str) -> bool:
        is_valid = self.__is_valid_course_title(course_title)

        if is_valid:
            self.__courses.append(course_title)
            return True
        else:
            return False

    def learn(self, topic: str, teacher) -> tuple[bool, str]:
        if not isinstance(topic, str) or not topic.strip():
            return False, 'Тема не указана'

        return True, f'Студент {self.get_name()} изучает тему "{topic}" у преподавателя {teacher.get_name()}'

    def get_courses(self) -> list[str]:
        return list(self.__courses)

    def get_info(self) -> str:
        default_info = super().get_info()
        courses = self.get_courses()

        if not courses:
            courses_info = 'ничего нет'
        else:
            courses_info = self.__COURSES_SEPARATOR.join(courses)

        return f'{default_info}, Курсы: {courses_info}'

    def __is_valid_course_title(self, course_title: str) -> bool:
        if not isinstance(course_title, str):
            return False
        if not course_title.strip():
            return False
        if course_title in self.__courses:
            return False

        return True
