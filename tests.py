from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_path = './chromedriver.exe'

options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--disable-application-cache')
options.add_argument('--disable-extensions')

service = Service(executable_path=chrome_path)

driver = webdriver.Chrome(service=service, options=options)

driver.get('https://www.cathaybk.com.tw/cathaybk/')

search = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'searchBox'))
)

search.send_keys('信用卡')

search_button = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/main/section/div[3]/div[3]/div/div/div[1]/div/a[1]'))
)
search_button.click()


driver.save_screenshot('png/2.png')

driver.quit()
