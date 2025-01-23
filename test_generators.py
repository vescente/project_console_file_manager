import os
import pytest
from unittest.mock import patch, mock_open
from file_operations import view_files, save_directory_components


def test_view_files_non_existing_directory(monkeypatch):
    with patch('builtins.input', return_value='non_existing_dir'):
        with patch('os.path.isdir', return_value=False):
            with patch('builtins.print') as mock_print:
                view_files()
                mock_print.assert_called_once_with('Указанный путь не является директорией.')

def test_save_directory_components():
    with patch('os.listdir', return_value=['file1.txt', 'dir1']):
        with patch('os.path.isfile', side_effect=lambda x: x == 'file1.txt'):
            with patch('os.path.isdir', side_effect=lambda x: x == 'dir1'):
                m = mock_open()
                with patch('builtins.open', m):
                    save_directory_components()
                    m().write.assert_any_call("files: file1.txt\n")
                    m().write.assert_any_call("dirs: dir1\n")

def test_save_directory_components_file_not_found():
    with patch('os.listdir', side_effect=FileNotFoundError):
        with patch('builtins.print') as mock_print:
            save_directory_components()
            mock_print.assert_called_once_with("Файл не найден.")

def test_save_directory_components_permission_error():
    with patch('os.listdir', side_effect=PermissionError):
        with patch('builtins.print') as mock_print:
            save_directory_components()
            mock_print.assert_called_once_with("Нет доступа к файлу.")
