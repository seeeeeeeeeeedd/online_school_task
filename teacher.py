from user import User


class Teacher(User):
    def __init__(self, name, surname, phone_number):
        super().__init__(name, surname, phone_number)

        self.__course_materials_separator = ', '
        self.__course_materials = []

    def add_course_material(self, course_material: str) -> bool:
        is_valid = self.__is_valid_course_material(course_material)

        if is_valid:
            self.__course_materials.append(course_material)
            return True
        else:
            return False

    def get_course_materials(self) -> list[str]:
        return list(self.__course_materials)

    def get_info(self) -> str:
        default_info = super().get_info()
        course_materials = self.get_course_materials()

        if not course_materials:
            course_materials_info = 'ничего нет'
        else:
            course_materials_info = self.__course_materials_separator.join(course_materials)

        return f'{default_info}, Содержимое курсов (учебные материалы): {course_materials_info}'

    def __is_valid_course_material(self, course_material: str) -> bool:
        if not isinstance(course_material, str):
            return False
        if not course_material.strip():
            return False
        if course_material in self.__course_materials:
            return False

        return True
