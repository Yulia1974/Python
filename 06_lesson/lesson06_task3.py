from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    images = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.ID, "text"))
    )

    time.sleep(20)

    find= WebDriverWait(driver, 10)
    award_element = find.until(EC.presence_of_element_located((By.ID, "award")))
    src = award_element.get_attribute("src")
    print(src)

finally:
    driver.quit()
