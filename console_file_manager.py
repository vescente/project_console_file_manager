from file_operations import create_folder, delete_file_or_folder, copy_file_or_folder, view_directory_contents, view_folders, view_files
from system_info import view_os_info, change_working_directory
from play_quiz import play_quiz
from bank_account import view_bank_account
from creator_info import view_creator_info


def main():
    while True:
        print("1. Создать папку")
        print("2. Удалить (файл/папку)")
        print("3. Копировать (файл/папку)")
        print("4. Просмотр содержимого рабочей директории")
        print("5. Посмотреть только папки")
        print("6. Посмотреть только файлы")
        print("7. Просмотр информации об операционной системе")
        print("8. Создатель программы")
        print("9. Играть в викторину")
        print("10. Мой банковский счет")
        print("11. Смена рабочей директории")
        print("12. Выход")

        choice = input("Выберите пункт меню: ")

        if choice == "1":
            create_folder()
        elif choice == "2":
            delete_file_or_folder()
        elif choice == "3":
            copy_file_or_folder()
        elif choice == "4":
            view_directory_contents()
        elif choice == "5":
            view_folders()
        elif choice == "6":
            view_files()
        elif choice == "7":
            view_os_info()
        elif choice == "8":
            view_creator_info()
        elif choice == "9":
            play_quiz()
        elif choice == "10":
            view_bank_account()
        elif choice == "11":
            change_working_directory()
        elif choice == "12":
            print("До свидания!")
            break
        else:
            print("Неверный пункт меню. Попробуйте еще раз.")


if __name__ == "__main__":
    main()
