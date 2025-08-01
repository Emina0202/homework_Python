from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/textinput")
    
wait = WebDriverWait(driver, 10)
input_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input.form-control')))
    
input_field.send_keys('SkyPro')
    
blue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn-primary')))
blue_button.click()
    
new_text = blue_button.text
print(new_text)

driver.quit()
