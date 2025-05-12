from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 60)

driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#delay')))

delay = driver.find_element(By.CSS_SELECTOR, '#delay')
delay.clear()
delay.send_keys("45")

driver.find_element(By.XPATH, "//span[text() = '7']").click()
driver.find_element(By.XPATH, "//span[text() = '+']").click()
driver.find_element(By.XPATH, "//span[text() = '8']").click()
driver.find_element(By.XPATH, "//span[text() = '=']").click()

try:
    result = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#result')))
    res_text = result.text

    assert res_text == '15', f"Ожидаемый результат должен быть '15', но получилось '{res_text}'"
except Exception as e:
    print(f"Произошла ошибка: {e}")

driver.quit()
