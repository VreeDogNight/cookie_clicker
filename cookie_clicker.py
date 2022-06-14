import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service

driver_path = Service('./geckodriver.exe')
driver = webdriver.Firefox(service=driver_path)
wait = WebDriverWait(driver, 60)
driver.get('https://orteil.dashnet.org/cookieclicker/')

element = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '#langSelect-EN'))
)
element.click()

wait.until(
    EC.invisibility_of_element_located((By.ID, 'offGameMessage'))
)
cookie = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '#bigCookie'))
)
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '.cc_btn').click()
cookie_count = driver.find_element(By.CSS_SELECTOR, '#cookies')
items = [driver.find_element(By.CSS_SELECTOR, f'#product{i}') for i in range(18, -1, -1)]

for i in range(500):
    cookie.click()
    count = int(cookie_count.text.split(' ')[0].replace(',', ''))
    if driver.find_elements(By.CSS_SELECTOR, 'div[class="crate upgrade enabled"]'):
        driver.find_element(By.CSS_SELECTOR, 'div[class="crate upgrade enabled"]').click()
        continue
    for item in items:
        if item.get_attribute('class') != 'product locked disabled toggledOff':
            value = int(item.text.split('\n')[1].replace(',', ''))
            if value <= count:
                item.click()
    time.sleep(0.25)
