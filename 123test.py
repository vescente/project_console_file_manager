import sys
import os

# Добавляем путь к родительской директории проекта
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bank_account.main import view_bank_account