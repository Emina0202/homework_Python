import pytest
from selenium import webdriver
from login_page import LoginPage
from products_page import ProductsPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@pytest.fixture
def browser():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_shopping_flow(browser):
    # Инициализация страниц
    login_page = LoginPage(browser)
    products_page = ProductsPage(browser)
    cart_page = CartPage(browser)
    checkout_page = CheckoutPage(browser)

    # Шаг 1: Открыть сайт и авторизоваться
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Шаг 2: Добавить товары в корзину
    products_page.add_to_cart("Backpack")
    products_page.add_to_cart("Bolt T-Shirt")
    products_page.add_to_cart("Onesie")

    # Шаг 3: Перейти в корзину и начать оформление
    products_page.go_to_cart()
    cart_page.proceed_to_checkout()

    # Шаг 4: Заполнить данные для доставки
    checkout_page.fill_shipping_info("Иван", "Петров", "123456")

    # Шаг 5: Проверить итоговую сумму
    total_text = checkout_page.get_total_amount()
    assert "Total: $58.29" in total_text, (
        f"Ожидалась сумма $58.29, получено {total_text}"
        )
