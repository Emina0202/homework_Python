import pytest
from string_utils import StringUtils


@pytest.fixture
def string_utils():
    return StringUtils()


# Положительные тесты
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("123", "123"),       # Числовые значения
    ("04 апреля 2023", "04 Апреля 2023")  # Дата
])
def test_capitalize_positive(string_utils, input_str, expected):
    result = string_utils.capitalize(input_str)
    assert result == expected


# Отрицательные тесты
@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("   ", "   "),     # Только пробелы
    ("", ""),           # Пустая строка
    (None, TypeError),  # Передача None
    ([], TypeError)     # Неправильный тип данных
])
def test_capitalize_negative(string_utils, input_str, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            string_utils.capitalize(input_str)
    else:
        result = string_utils.capitalize(input_str)
        assert result == expected
