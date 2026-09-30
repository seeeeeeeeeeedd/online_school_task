from user import User


class Teacher(User):
    def __init__(self, name, surname, phone_number):
        super().__init__(name, surname, phone_number)

        self.__course_materials = []

    def add_course_material(self, course_material: str) -> bool:
        is_valid = self.__is_valid_course_material(course_material)

        if is_valid:
            self.__course_materials.append(course_material)
            return True
        else:
            return False

    def __is_valid_course_material(self, course_material: str) -> bool:
        if not isinstance(course_material, str):
            return False
        if not course_material.strip():
            return False
        if course_material in self.__course_materials:
            return False

        return True
