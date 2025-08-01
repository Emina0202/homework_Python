from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
    )

driver.get('http://uitestingplayground.com/classattr')


blue_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
blue_button.click()

input("Нажмите Enter для закрытия браузера...")
driver.quit()
