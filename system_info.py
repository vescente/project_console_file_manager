import os
import platform


def view_os_info():
    print("Информация об операционной системе:")
    print(f"Система: {platform.system()}")
    print(f"Версия: {platform.version()}")
    print(f"Платформа: {platform.platform()}")


def change_working_directory():
    new_path = input("Введите новый путь: ")
    os.chdir(new_path)
    print(f"Рабочая директория изменена на: {os.getcwd()}")
