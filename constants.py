people_menu = """Дальнейшие операции:
    0 - возврат в главное меню;
    3 - добавление нового человека;
    4 - удаление человека;
    5 - просмотр телефонов человека;
    auto - просмотр машин человека;
    f - (forward) вперед;
    b - (backard) назад;
    p-<<number>> - номер страницы;
    9 - выход."""

phones_menu = """Дальнейшие операции:
    0 - возврат в главное меню;
    1 - возврат в просмотр людей;
    6 - добавление нового телефона;
    7 - удаление телефона;
    9 - выход."""

autos_menu = """Дальнейшие операции:
    0 - возврат в главное меню;
    1 - возврат в просмотр людей;
    a6 - добавление нового авто;
    a7 - удаление авто;
    a8 - изменение записи авто;
    9 - выход."""

main_menu = """Добро пожаловать! 
Основное меню (выберите цифру в соответствии с необходимым действием): 
    1 - просмотр людей;
    2 - сброс и инициализация таблиц;
    9 - выход."""

prompts = {
    "empty_line": "Укажите интересующую Вас запись (id для людей ,phone для телефонов, identity для авто) (0 - отмена):",
    "empty_line_error": "Пустая строка. Повторите ввод! (0 - отмена):",
    "no_rows_error": "Некорректный ввод!",
    "show_people": "Просмотр списка людей!\n№\tФамилия\tИмя\tОтчество",
    "primary_forbidden": "Нарушен Primary Key, запись не была вставлена"
}

records_per_page = 5