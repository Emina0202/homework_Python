from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/login")

username_input = driver.find_element(By.ID, "username")
password_input = driver.find_element(By.ID, "password")

username_input.send_keys("tomsmith")
password_input.send_keys("SuperSecretPassword!")

login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

success_message = driver.find_element(By.CLASS_NAME, "flash.success").text.strip()
print(f"Текст с зеленой плашки: {success_message}")

driver.quit()
