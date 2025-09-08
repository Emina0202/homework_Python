import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure  # Импортируем модуль allure


@allure.tag("Calculator")
@allure.description("Тестируем покупку в онлайн магазине")
@allure.epic("Калькулятор")
@pytest.fixture(scope='module')
@allure.title("Инициализация веб-драйвера Chrome")  # Аннотация заголовка теста
def chrome_driver():
    """
    Фикстура инициализации драйвера браузера Chrome
    """
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@allure.feature("Тест калькулятора с задержкой")
@allure.story("Проверка функционала медленного калькулятора")
@allure.severity(allure.severity_level.NORMAL)  # Уровень важности теста
def test_calculator_with_delay(chrome_driver):
    """
    Автотест калькулятора с задержкой вычисления
    """
    with allure.step("Открываем страницу"):  # Шаг: открытие страницы
        chrome_driver.get(
            'https://bonigarcia.dev/'
            'selenium-webdriver-java/slow-calculator.html')

    with allure.step("Устанавливаем задержку на 45 секунд"):
        delay_input = chrome_driver.find_element(
            By.ID, 'delay')  # Элемент ввода задержки
        delay_input.clear()
        delay_input.send_keys('45')

    with allure.step("Нажимаем кнопки 7 + 8 ="):
        buttons_to_click = ['7', '+', '8', '=']
        for button_text in buttons_to_click:
            xpath_selector = f'//span[contains(text(), "{button_text}")]'
            button = chrome_driver.find_element(By.XPATH, xpath_selector)
            button.click()

    with allure.step("Ждем появления результата 15"):
        WebDriverWait(chrome_driver, 50).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"
                                             ))

    result_text = chrome_driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert "15" in result_text, f"Ожидался результат 15, получено: {
        result_text}"