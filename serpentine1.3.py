import csv
import os
import subprocess
from pystyle import Colors, Colorate, Center, Box

# Цвета для форматирования
COLOR_CODE = {
    "RESET": "\033[0m",
    "UNDERLINE": "\033[04m",
    "GREEN": "\033[32m",
    "YELLOW": "\033[93m",
    "RED": "\033[31m",
    "CYAN": "\033[36m",
    "BOLD": "\033[01m",
    "PINK": "\033[95m",
    "URL_L": "\033[36m",
    "LI_G": "\033[92m",
    "F_CL": "\033[0m",
    "DARK": "\033[90m",
}

# Функция для очистки консоли
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# ASCII баннер
banner = """
  ██████ ▓█████  ██▀███   ██▓███  ▓█████  ███▄    █ ▄▄▄█████▓ ██▓ ███▄    █ ▓█████ 
▒██    ▒ ▓█   ▀ ▓██ ▒ ██▒▓██░  ██▒▓█   ▀  ██ ▀█   █ ▓  ██▒ ▓▒▓██▒ ██ ▀█   █ ▓█   ▀ 
░ ▓██▄   ▒███   ▓██ ░▄█ ▒▓██░ ██▓▒▒███   ▓██  ▀█ ██▒▒ ▓██░ ▒░▒██▒▓██  ▀█ ██▒▒███   
  ▒   ██▒▒▓█  ▄ ▒██▀▀█▄  ▒██▄█▓▒ ▒▒▓█  ▄ ▓██▒  ▐▌██▒░ ▓██▓ ░ ░██░▓██▒  ▐▌██▒▒▓█  ▄ 
▒██████▒▒░▒████▒░██▓ ▒██▒▒██▒ ░  ░░▒████▒▒██░   ▓██░  ▒██▒ ░ ░██░▒██░   ▓██░░▒████▒
▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒▓ ░▒▓░▒▓▒░ ░  ░░░ ▒░ ░░ ▒░   ▒ ▒   ▒ ░░   ░▓  ░ ▒░   ▒ ▒ ░░ ▒░ ░
░ ░▒  ░ ░ ░ ░  ░  ░▒ ░ ▒░░▒ ░      ░ ░  ░░ ░░   ░ ▒░    ░     ▒ ░░ ░░   ░ ▒░ ░ ░  ░
░  ░  ░     ░     ░░   ░ ░░          ░      ░   ░ ░   ░       ▒ ░   ░   ░ ░    ░   
      ░     ░  ░   ░                 ░  ░         ░           ░           ░    ░  ░
"""

# Рамка с информацией о владельце, версии и цене
info_box = """
OWNER: Susanoooooooo
────────────────────
Version: 1.3 Beta
────────────────────
Price: ?? /Month
"""

# Вывод баннера с градиентом
def display_banner():
    clear_console()
    combined_banner = f"{banner}{' ' * 5}{info_box}"
    print(Colorate.Horizontal(Colors.green_to_white, Center.XCenter(combined_banner)))

def main_menu():
    menu_options = [
        ["1. Поиск по номеру", "5. Поиск в локальной базе данных по ФИО"],
        ["2. Поиск по почте", "6. Информация о домене"],
        ["3. Поиск по IP", "7. Доксинг"],
        ["4. Поиск по социальным сетям", "8. Сканирование портов"],
        ["9. Выход", ""]
    ]
    
    # Создание меню в рамке
    menu_box = Box.DoubleCube("Меню\n" + "\n".join([f"{left:<40} {right}" for left, right in menu_options]))
    print(Colorate.Horizontal(Colors.green_to_white, Center.XCenter(menu_box)))

def get_mail(database_file, search_value):
    found = False

    with open(database_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 9:
            email = data[8]
            if search_value in email:
                user_id = data[0]
                registration_date = data[1]
                last_name = data[2]
                first_name = data[3]
                middle_name = data[4]
                birthday = data[5]
                gender = data[6]
                phone = data[7]
                role = data[9]
                class_name = data[13]
                address = data[19]
                country = data[16]
                citizenship = data[15]
                region = data[17]
                municipal_education = data[18]
                institution_name = data[20]

                print(f'''{COLOR_CODE["RED"]}
╔══════                                               ══════╗
║                                                           ║
                {COLOR_CODE["RED"]}[+]ID пользователя: {user_id}
                [+]Дата регистрации: {registration_date}
                [+]Фамилия: {last_name}
                [+]Имя: {first_name}
                [+]Отчество: {middle_name}
                [+]Дата рождения: {birthday}
                [+]Пол: {gender}
                [+]Телефон: {phone}
                [+]Почта: {email}
                [+]Роль: {role}
                [+]Класс: {class_name}
                [+]Адрес: {address}
                [+]Страна: {country}
                [+]Гражданство: {citizenship}
                [+]Регион: {region}
                [+]Муниципальное образование: {municipal_education}
                [+]Наименование учреждения: {institution_name}
{COLOR_CODE["GREEN"]}
║                                                           ║
╚══════                                               ══════╝
''')
                found = True

    if not found:
        print(f'{COLOR_CODE["RED"]}[ERROR]Ничего не найдено в базе данных по почте.{COLOR_CODE["RESET"]}')

def get_fio(database_file, search_value):
    found = False

    with open(database_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 5:
            last_name = data[2]
            first_name = data[3]
            middle_name = data[4]
            full_name = f"{last_name} {first_name} {middle_name}".strip().lower()
            if search_value.lower() in full_name:
                user_id = data[0]
                registration_date = data[1]
                birthday = data[5]
                gender = data[6]
                phone = data[7]
                email = data[8]
                role = data[9]
                class_name = data[13]
                address = data[19]
                country = data[16]
                citizenship = data[15]
                region = data[17]
                municipal_education = data[18]
                institution_name = data[20]

                print(f'''{COLOR_CODE["RED"]}
╔══════                                               ══════╗
║                                                           ║
                {COLOR_CODE["RED"]}[+]ID пользователя: {user_id}
                [+]Дата регистрации: {registration_date}
                [+]Фамилия: {last_name}
                [+]Имя: {first_name}
                [+]Отчество: {middle_name}
                [+]Дата рождения: {birthday}
                [+]Пол: {gender}
                [+]Телефон: {phone}
                [+]Почта: {email}
                [+]Роль: {role}
                [+]Класс: {class_name}
                [+]Адрес: {address}
                [+]Страна: {country}
                [+]Гражданство: {citizenship}
                [+]Регион: {region}
                [+]Муниципальное образование: {municipal_education}
                [+]Наименование учреждения: {institution_name}
{COLOR_CODE["GREEN"]}
║                                                           ║
╚══════                                               ══════╝
''')
                found = True

    if not found:
        print(f'{COLOR_CODE["RED"]}[ERROR]Ничего не найдено в базе данных по ФИО.{COLOR_CODE["RESET"]}')

def main():
    while True:
        display_banner()
        main_menu()
        choice = input(Colorate.Horizontal(Colors.green_to_white, "\nВыберите опцию: "))
        
        if choice == '1':
            subprocess.run(['python', 'number.py'])
        
        elif choice == '2':
            email = input(Colorate.Horizontal(Colors.green_to_white, "Введите электронную почту: "))
            get_mail('bd1.csv', email)
        
        elif choice == '3':
            subprocess.run(['python', 'ip.py'])
        
        elif choice == '4':
            subprocess.run(['python', 'social_media.py'])
        
        elif choice == '5':
            fio = input(Colorate.Horizontal(Colors.green_to_white, "Введите ФИО: "))
            get_fio('bd1.csv', fio)
        
        elif choice == '6':
            subprocess.run(['python', 'domain_info.py'])
        
        elif choice == '7':
            subprocess.run(['python', 'dox_template.py'])
        
        elif choice == '8':
            subprocess.run(['python', 'port_scan.py'])
        
        elif choice == '9':
            print(Colorate.Horizontal(Colors.green_to_white, "Выход..."))
            break
        
        else:
            print(Colorate.Horizontal(Colors.green_to_white, f"Вы выбрали: {choice}"))
        
        input(Colorate.Horizontal(Colors.green_to_white, "\nНажмите Enter для возврата в меню..."))
        clear_console()

if __name__ == "__main__":
    main()
