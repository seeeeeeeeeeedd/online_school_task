class User:
    def __init__(self, name, surname, phone_number):
        is_valid_fullname = self.__is_valid_fullname(name, surname)
        is_valid_phone_number = self.__is_valid_phone_number(phone_number)

        if is_valid_fullname and is_valid_phone_number:
            self.__name = name
            self.__surname = surname
            self.__phone_number = phone_number
        else:
            self.__name = 'Имя неизвестно'
            self.__surname = 'Фамилия неизвестна'
            self.__phone_number = 'Номер не указан'

    def __is_valid_fullname(self, name: str, surname: str) -> bool:
        if not isinstance(name, str) or not isinstance(surname, str):
            return False
        if not name.strip() or not surname.strip():
            return False

        return True

    def __is_valid_phone_number(self, phone_number: str) -> bool:
        if not isinstance(phone_number, str):
            return False
        if not phone_number.strip():
            return False
        if not phone_number.isdigit():
            return False

        return True
