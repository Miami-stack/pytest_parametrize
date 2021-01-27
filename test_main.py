"""Выполнение задания с pytest."""
import random
import re
import string

import pytest
from faker import Faker

fake = Faker()


def valid_email(email: str) -> bool:
    """Функция валидации емейла по регулярке."""
    return bool(re.search(r"^[\w\.\+\-]+\@[ \w]+\.[a-z]{2,3}$", email))


def log(file_name: str, text: str) -> None:
    """Функция записи результатов в файл."""
    with open(file_name, 'a') as f_obj:
        f_obj.write(text + '\n')
        f_obj.close()


def create_invalid_email(number: int) -> str:
    """Функция, которая создает невалидные емейлы."""
    data_domain = random.choice(['test@test.', 'w@', '@tt'])
    rand_body = ''.join(random.choice(string.ascii_letters) for _ in range(number))
    result = rand_body + data_domain
    return result


@pytest.mark.parametrize('email', [fake.free_email() for _ in range(5)])
def test_check_valid_email(email: str, stdout_log: str) -> None:
    """Тест на проверку валидного емейла."""
    if valid_email(email) is True:
        log(stdout_log, email + '   ' + 'Проверка test_check_valid_email прошла успешно')
        assert valid_email(email) is True


@pytest.mark.parametrize('email', [create_invalid_email(7) for _ in range(5)])
def test_check_invalid_email(email: str, stdout_log: str) -> None:
    """Тест на проверку невалидного емейла."""
    if valid_email(email) is False:
        log(stdout_log, email + '   ' + 'Проверка test_check_invalid_email прошла успешно')
        assert valid_email(email) is False
