def show_menu():
    print('''
    1. Добавить заметку
    2. Редактировать заметку
    3. Найти заметку
    4. Показать заметки за дату
    5. Показать все заметки
    6. Удалить заметку
    7. Выход 
    ''')
    return input("Выберите действие: ")


def show_note(data):
    result = 'id:' + data['id'] + ' Название: ' + data['header'] + ' Текст: ' + data['body'] + ' Изменено: ' + data['modified']
    print(result)


def new_note_ui():
    note = input("Введите название: "), input('Введите текст: ')
    return note


def error_message():
    print("Ошибка. Значение не найдено")


def ask_for_id():
    return input('Введите id заметки: ')


def ask_for_date():
    return input('Введите дату в формате dd.mm.yyyy: ')

def confirm_result():
    print('Действие выполнено успешно')



