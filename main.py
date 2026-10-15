from student import Student
from teacher import Teacher
from school import School

UNKNOWN_COMMAND_MESSAGE = 'Неизвестная команда. Попробуйте снова'

commands = {
    '1': 'Создать ученика',
    '2': 'Создать преподавателя',
    '3': 'Добавить учебные материалы',
    '4': 'Записать ученика на курс',
    '5': 'Провести занятие',
    '6': 'Посетить занятие',
    '7': 'Показать всех учеников',
    '8': 'Показать всех преподавателей',
    '0': 'Выйти из программы'
}

(ADD_STUDENT_COMMAND, ADD_TEACHER_COMMAND, ADD_COURSE_MATERIAL_COMMAND, SIGN_UP_FOR_COURSE_COMMAND, TEACH_COMMAND,
 LEARN_COMMAND, SHOW_ALL_STUDENTS_COMMAND, SHOW_ALL_TEACHERS_COMMAND, EXIT_COMMAND) = commands.keys()

school = School('Онлайн-школа')


def print_commands():
    for number, command in commands.items():
        print(f'{number}: {command}')


def get_person_data():
    name = input('Укажите имя: ').strip().capitalize()
    surname = input('Укажите фамилию: ').strip().capitalize()
    phone_number = input('Укажите номер телефона без пробелов: ').strip()

    return name, surname, phone_number


def find_student():
    user_student_name = input('Укажите имя ученика: ').strip().capitalize()
    student = school.find_student_by_name(user_student_name)

    if not student:
        print('Ученик не найден')
    return student


def find_teacher():
    user_teacher_name = input('Укажите имя преподавателя: ').strip().capitalize()
    teacher = school.find_teacher_by_name(user_teacher_name)

    if not teacher:
        print('Преподаватель не найден')
    return teacher


is_program_running = True

while is_program_running:
    print()
    print_commands()

    user_command_number = input('Выберите действие и укажите его номер: ')

    if user_command_number in commands:
        if user_command_number == ADD_STUDENT_COMMAND:
            name, surname, phone_number = get_person_data()
            new_student = Student(name, surname, phone_number)
            school.add_student(new_student)

            print('Ученик успешно создан')
        elif user_command_number == ADD_TEACHER_COMMAND:
            name, surname, phone_number = get_person_data()
            new_teacher = Teacher(name, surname, phone_number)
            school.add_teacher(new_teacher)

            print('Преподаватель успешно создан')
        elif user_command_number == ADD_COURSE_MATERIAL_COMMAND:
            teacher = find_teacher()

            if teacher:
                user_course_material = input('Укажите учебный материал: ').strip()
                teacher.add_course_material(user_course_material)
        elif user_command_number == SIGN_UP_FOR_COURSE_COMMAND:
            student = find_student()

            if student:
                user_course_title = input('Укажите название курса: ').strip().capitalize()
                student.sign_up_for_course(user_course_title)
        elif user_command_number == TEACH_COMMAND:
            teacher = find_teacher()

            if teacher:
                student = find_student()

                if student:
                    user_topic = input('Укажите тему занятия: ').strip()
                    success, message = teacher.teach(user_topic, student)

                    print(message)
        elif user_command_number == LEARN_COMMAND:
            student = find_student()

            if student:
                teacher = find_teacher()

                if teacher:
                    user_topic = input('Укажите тему занятия: ').strip()
                    success, message = student.learn(user_topic, teacher)

                    print(message)
        elif user_command_number == SHOW_ALL_STUDENTS_COMMAND:
            school.show_all_students()
        elif user_command_number == SHOW_ALL_TEACHERS_COMMAND:
            school.show_all_teachers()
        elif user_command_number == EXIT_COMMAND:
            is_program_running = False
            print('Работа программы завершена')
        else:
            print(UNKNOWN_COMMAND_MESSAGE)
    else:
        print(UNKNOWN_COMMAND_MESSAGE)
