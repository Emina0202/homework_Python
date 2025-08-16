from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_screen = (By.CSS_SELECTOR, ".screen")
        self.button_locator = "//span[text()='{}']"

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, seconds):
        delay_field = self.driver.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(str(seconds))

    def click_button(self, button_text):
        button = self.driver.find_element(
            By.XPATH, self.button_locator.format(button_text))
        button.click()

    def get_result(self, timeout=46):
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.result_screen, "15")
        )
    