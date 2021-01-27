"""Фикстура создания файла."""
from typing import Any

import pytest


@pytest.fixture()
def stdout_log(request: Any) -> None:
    """Фикстура."""
    file_name = request.config.getini('file_name')
    return file_name


def pytest_addoption(parser: Any) -> None:
    """Опция для фикстуры."""
    parser.addini('file_name', help="file", default="log.txt")
