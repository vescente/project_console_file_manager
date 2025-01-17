import os
import shutil


def create_folder():
    folder_name = input("Введите имя папки: ")
    os.makedirs(folder_name, exist_ok=True)
    print(f"Папка '{folder_name}' создана.")


def delete_file_or_folder():
    path = input("Введите путь к файлу или папке: ")
    if os.path.isdir(path):
        shutil.rmtree(path)
        print(f"Папка '{path}' удалена.")
    elif os.path.isfile(path):
        os.remove(path)
        print(f"Файл '{path}' удален.")
    else:
        print("Указанный путь не существует.")


def copy_file_or_folder():
    source = input("Введите путь к исходному файлу или папке: ")
    destination = input("Введите путь к месту назначения: ")
    if os.path.isdir(source):
        shutil.copytree(source, destination)
        print(f"Папка '{source}' скопирована в '{destination}'.")
    elif os.path.isfile(source):
        shutil.copy2(source, destination)
        print(f"Файл '{source}' скопирован в '{destination}'.")
    else:
        print("Указанный путь не существует.")


def view_directory_contents():
    path = input("Введите путь к директории: ")
    if os.path.isdir(path):
        print("Содержимое директории:")
        for item in os.listdir(path):
            print(item)
    else:
        print("Указанный путь не является директорией.")


def view_folders():
    path = input("Введите путь к директории: ")
    if os.path.isdir(path):
        print("Папки в директории:")
        for item in os.listdir(path):
            if os.path.isdir(os.path.join(path, item)):
                print(item)
    else:
        print("Указанный путь не является директорией.")


def view_files():
    path = input("Введите путь к директории: ")
    if os.path.isdir(path):
        print("Файлы в директории:")
        for item in os.listdir(path):
            if os.path.isfile(os.path.join(path, item)):
                print(item)
    else:
        print("Указанный путь не является директорией.")
