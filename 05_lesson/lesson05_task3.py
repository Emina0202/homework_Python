from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


driver.get("http://the-internet.herokuapp.com/inputs")

input_field = driver.find_element("tag name", "input")
input_field.send_keys("Sky")
input_field.clear()
input_field.send_keys("Pro")

driver.quit()
