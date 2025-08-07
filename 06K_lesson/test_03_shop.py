from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture
def browser():
    # Используем Firefox как указано в задании
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_shopping_cart_total(browser):
    # 1. Открыть сайт магазина
    browser.get("https://www.saucedemo.com/")

    # 2. Авторизоваться как standard_user
    username = browser.find_element(By.ID, "user-name")
    password = browser.find_element(By.ID, "password")
    login_button = browser.find_element(By.ID, "login-button")

    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()

    # 3. Добавить товары в корзину
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.ID, "add-to-cart-sauce-labs-backpack")
            )
    ).click()

    browser.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    browser.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    # 4. Перейти в корзину
    browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # 5. Нажать Checkout
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "checkout"))
    ).click()

    # 6. Заполнить форму данными
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "first-name"))
    ).send_keys("Иван")

    browser.find_element(By.ID, "last-name").send_keys("Петров")
    browser.find_element(By.ID, "postal-code").send_keys("123456")

    # 7. Нажать Continue
    browser.find_element(By.ID, "continue").click()

    # 8. Прочитать итоговую стоимость
    total_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )
    total_text = total_element.text

    # 9. Проверить, что итоговая сумма равна $58.29
    assert "Total: $58.29" in total_text, \
        f"Итоговая сумма должна быть $58.29, а получилось {total_text}"
