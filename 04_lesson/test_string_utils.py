import pytest
from string_utils import StringUtils


@pytest.fixture
def utils():
    return StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("123", "123"),
    ("тест", "Тест"),
    ("04 апреля 2023", "04 апреля 2023"),
    ("", ""),
    (" ", " "),
])
def test_capitalize_positive(utils, input_str, expected):
    assert utils.capitalize(input_str) == expected


@pytest.mark.negative
def test_capitalize_negative(utils):
    with pytest.raises(TypeError):
        utils.capitalize(None)
    with pytest.raises(TypeError):
        utils.capitalize([])


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("  test  ", "test  "),
    ("", ""),
    (" ", ""),
])
def test_trim(utils, input_str, expected):
    assert utils.trim(input_str) == expected


@pytest.mark.negative
def test_trim_negative(utils):
    with pytest.raises(TypeError):
        utils.trim(123)


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "U", False),
    ("", "", True),
    (" ", " ", True),
    ("123", "2", True),
])
def test_contains(utils, string, symbol, expected):
    assert utils.contains(string, symbol) == expected


@pytest.mark.negative
def test_contains_negative(utils):
    with pytest.raises(TypeError):
        utils.contains(None, "a")
    with pytest.raises(TypeError):
        utils.contains("text", 123)


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("", "a", ""),
    ("   ", " ", ""),
    ("aabbcc", "b", "aacc"),
])
def test_delete_symbol(utils, string, symbol, expected):
    assert utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
def test_delete_symbol_negative(utils):
    with pytest.raises(TypeError):
        utils.delete_symbol([], "a")
    with pytest.raises(TypeError):
        utils.delete_symbol("text", 123)
