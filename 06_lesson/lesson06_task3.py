from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
waiter = WebDriverWait(driver, 120)
driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')

waiter.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#image-container")))

driver.save_screenshot('./java_.png')

driver.quit()
