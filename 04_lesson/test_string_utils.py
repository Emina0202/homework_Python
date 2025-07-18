import pytest
from string_utils import StringUtils


@pytest.fixture
def string_utils():
    return StringUtils()


# Метод capitalize()
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("123", "123"),          # числовое значение
    ("04 апреля 2023", "04 Апреля 2023")  # дата
])
def test_capitalize_positive(string_utils, input_str, expected):
    """Позитивные тесты для метода capitalize"""
    result = string_utils.capitalize(input_str)
    assert result == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("   ", "   "),      # пустые пробелы
    ("", ""),            # пустая строка
    (None, TypeError),   # передача None
    ([], TypeError)      # неправильный тип данных
])
def test_capitalize_negative(string_utils, input_str, expected):
    """Негативные тесты для метода capitalize"""
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            string_utils.capitalize(input_str)
    else:
        result = string_utils.capitalize(input_str)
        assert result == expected


# Метод lower()
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("SKYPRO", "skypro"),
    ("Hello World", "hello world"),
    ("ÄÖÜß", "äöüß")    # символы Unicode
])
def test_lower_positive(string_utils, input_str, expected):
    """Позитивные тесты для метода lower"""
    result = string_utils.lower(input_str)
    assert result == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    (None, TypeError),
    (["list"], TypeError),
    ({"dict": True}, TypeError)
])
def test_lower_negative(string_utils, input_str, expected):
    """Негативные тесты для метода lower"""
    with pytest.raises(expected):
        string_utils.lower(input_str)


# Метод upper()
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "SKYPRO"),
    ("привет мир", "ПРИВЕТ МИР"),
    ("áéíóú", "ÁÉÍÓÚ")  # буквы с диакритическими знаками
])
def test_upper_positive(string_utils, input_str, expected):
    """Позитивные тесты для метода upper"""
    result = string_utils.upper(input_str)
    assert result == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    (True, TypeError),
    ({}, TypeError),
    (None, TypeError)
])
def test_upper_negative(string_utils, input_str, expected):
    """Негативные тесты для метода upper"""
    with pytest.raises(expected):
        string_utils.upper(input_str)


# Метод strip()
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" skypro ", "skypro"),
    ("\\n\\t\\n hello \\n\\t\\r", "hello"),
    ("123", "123")  # строка без пробелов
])
def test_strip_positive(string_utils, input_str, expected):
    """Позитивные тесты для метода strip"""
    result = string_utils.strip(input_str)
    assert result == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    (123, TypeError),     # число
    (None, TypeError),    # null-значение
    ([], TypeError)       # пустой список
])
def test_strip_negative(string_utils, input_str, expected):
    """Негативные тесты для метода strip"""
    with pytest.raises(expected):
        string_utils.strip(input_str)
