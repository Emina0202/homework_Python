from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
waiter = WebDriverWait(driver, 120)
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    )

WebDriverWait(driver, 120).until(lambda d: all(d.find_element(
    By.ID, img_id).get_attribute("src")
    for img_id in ["compass", "calendar", "award", "landscape"]))

waiter.until(
    EC.presence_of_all_elements_located((By.TAG_NAME, "img"))
    )
image = driver.find_element(By.ID, "award")
image_src = image.get_attribute("src")
print(f"Атрибут src 3-й картинки: {image_src}")

driver.save_screenshot('./java_.png')
driver.quit()
