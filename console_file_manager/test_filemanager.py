import pytest
import random
from unittest.mock import patch

# Пример чистых функций
def test_get_random_person():
    from play_quiz import get_random_person
    FAMOUS_PEOPLE = {'Александр Сергеевич Пушкин': '26.06.1799', 'Михаил Юрьевич Лермонтов': '15.10.1814',
                     'Сергей Александрович Есенин': '03.10.1895', 'Владимир Семенович Высоцкий': '25.01.1938',
                     'Виктор Робертович Цой': '21.06.1962', 'Константин Эдуардович Циолковский': '17.09.1857',
                     'Сергей Павлович Королев': '12.01.1907', 'Валентин Петрович Глушко': '20.08.1908',
                     'Андрей Николаевич Туполев': '29.10.1888', 'Юрий Алексеевич Гагарин': '09.03.1934'}
    
    name, date = get_random_person()
    assert name in FAMOUS_PEOPLE
    assert date == FAMOUS_PEOPLE[name]

# Пример грязных функций
@patch('builtins.input', return_value='26.06.1799')
@patch('play_quiz.get_random_person', return_value=('Александр Сергеевич Пушкин', '26.06.1799'))
def test_play_quiz_correct(mock_get_random_person, mock_input, capsys):
    from play_quiz import play_quiz
    play_quiz()
    captured = capsys.readouterr()
    assert 'Верно' in captured.out

@patch('builtins.input', return_value='01.01.2000')
@patch('play_quiz.get_random_person', return_value=('Александр Сергеевич Пушкин', '26.06.1799'))
def test_play_quiz_incorrect(mock_get_random_person, mock_input, capsys):
    from play_quiz import play_quiz
    play_quiz()
    captured = capsys.readouterr()
    assert 'Неверно. Правильный ответ: 26.06.1799' in captured.out
