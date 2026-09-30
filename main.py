from student import Student
from teacher import Teacher

students = []
teachers = []

commands = {
    '1': 'Создать ученика',
    '2': 'Создать преподавателя',
    '3': 'Добавить учебные материалы',
    '4': 'Записать ученика на курс',
    '5': 'Показать всех учеников',
    '6': 'Показать всех преподавателей',
    '0': 'Выйти из программы'
}

(ADD_STUDENT_COMMAND, ADD_TEACHER_COMMAND, SIGN_UP_FOR_COURSE_COMMAND,
 ADD_COURSE_MATERIAL_COMMAND, SHOW_ALL_STUDENTS_COMMAND, SHOW_ALL_TEACHERS_COMMAND,
 EXIT_COMMAND) = commands.keys()

is_program_running = True

while is_program_running:

    print()
    for number, command in commands.items():
        print(f'{number}: {command}')

    user_command_number = input('Выберете действие и укажите его номер: ')

    if user_command_number in commands:
        if user_command_number == ADD_STUDENT_COMMAND:
            user_student_name = input('Укажите имя ученика: ').strip().capitalize()
            user_student_surname = input('Укажите фамилию ученика: ').strip().capitalize()
            user_student_phone_number = input('Укажите номер телефона без пробелов: ').strip()

            new_student = Student(user_student_name, user_student_surname, user_student_phone_number)
            students.append(new_student)
            print('Ученик успешно создан')
        elif user_command_number == ADD_TEACHER_COMMAND:
            user_teacher_name = input('Укажите имя преподавателя: ').strip().capitalize()
            user_teacher_surname = input('Укажите фамилию преподавателя: ').strip().capitalize()
            user_teacher_phone_number = input('Укажите номер телефона без пробелов: ').strip()

            new_teacher = Teacher(user_teacher_name, user_teacher_surname, user_teacher_phone_number)
            teachers.append(new_teacher)
            print('Преподаватель успешно создан')
        elif user_command_number == ADD_COURSE_MATERIAL_COMMAND:
            user_teacher_name = input('Укажите имя преподавателя, '
                                      'которому хотите добавить учебные материалы: ').strip().capitalize()
            is_teacher_found = False

            for teacher in teachers:
                if user_teacher_name == teacher.get_name():
                    user_course_material = input('Укажите учебный материал (учебник, атлас): ').strip().lower()
                    teacher.add_course_material(user_course_material)
                    is_teacher_found = True

            if not is_teacher_found:
                print('Преподаватель не найден')
        elif user_command_number == SIGN_UP_FOR_COURSE_COMMAND:
            user_student_name = input('Укажите имя ученика: ').strip().capitalize()

            is_student_found = False

            for student in students:
                if user_student_name == student.get_name():
                    user_course_title = input('Укажите название курса: ').strip().capitalize()
                    student.sign_up_for_course(user_course_title)
                    is_student_found = True
            if not is_student_found:
                print('Ученик не найден')
        elif user_command_number == SHOW_ALL_STUDENTS_COMMAND:
            if not students:
                print('Список учеников пуст')
            else:
                for student in students:
                    print(student.get_info())
        elif user_command_number == SHOW_ALL_TEACHERS_COMMAND:
            if not teachers:
                print('Список преподавателей пуст')
            else:
                for teacher in teachers:
                    print(teacher.get_info())
        elif user_command_number == EXIT_COMMAND:
            is_program_running = False
            print('Работа программы завершена')
    else:
        print('Неизвестная команда. Попробуйте снова')
