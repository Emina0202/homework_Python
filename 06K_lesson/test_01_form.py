from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

driver.find_element(By.CSS_SELECTOR, "First-name").send_keys("Иван")
driver.find_element(By.CSS_SELECTOR, "Last name").send_keys("Петров")
driver.find_element(By.CSS_SELECTOR, "Address").send_keys("Ленина 55-3")
driver.find_element(By.CSS_SELECTOR, "Email").send_keys("test@skypro.com")
driver.find_element(By.CSS_SELECTOR, "Phone number").send_keys("+7985899998787")
driver.find_element(By.CSS_SELECTOR, "Zip code").send_keys("")
driver.find_element(By.CSS_SELECTOR, "City").send_keys("Москва")
driver.find_element(By.CSS_SELECTOR, "Country").send_keys("Россия")
driver.find_element(By.CSS_SELECTOR, "Job position").send_keys("QA")
driver.find_element(By.CSS_SELECTOR, "Company").send_keys("SkyPro")

submit_button = edge_driver.find_element(By.CSS_SELECTOR, "submit-button").click()

wait = WebDriverWait(edge_driver, 10)
wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "form-control")))

filled_fields = [
        input_field for input_field in form_inputs
        if input_field.get_attribute("name") != "zipCode"
    ]

zip_code_field = next(field for field in form_inputs if field.get_attribute("name") == "zipCode")
assert "is-invalid" in zip_code_field.get_attribute("class"), "Поле ZIP code не подсветилось красным."


for field in filled_fields:
 assert "is-valid" in field.get_attribute("class"), f"Поле '{field.get_attribute('name')}' не подсветилось зеленым."

driver.quit()
