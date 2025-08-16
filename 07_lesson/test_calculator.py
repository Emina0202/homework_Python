import pytest
from selenium import webdriver
from calculator_page import CalculatorPage

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_calculator_with_delay(browser):
    calculator = CalculatorPage(browser)
    
    # Открыть страницу калькулятора
    calculator.open()
    
    # Установить задержку 45 секунд
    calculator.set_delay(45)
    
    # Выполнить операцию 7 + 8
    calculator.click_button("7")
    calculator.click_button("+")
    calculator.click_button("8")
    calculator.click_button("=")
    
    # Проверить результат
    assert calculator.get_result(), "Результат не равен 15 после ожидания"
