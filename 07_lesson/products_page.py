from selenium.webdriver.common.by import By


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_button = (By.CLASS_NAME, "shopping_cart_link")

    def add_to_cart(self, product_name):
        item_id = product_name.lower().replace(" ", "-")
        self.driver.find_element(
            By.ID, f"add-to-cart-sauce-labs-{item_id}"
            ).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_button).click()
