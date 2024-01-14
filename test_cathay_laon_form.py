from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_path = './chromedriver.exe'

options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--disable-application-cache')
options.add_argument('--disable-extensions')

service = Service(executable_path=chrome_path)

driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.cathaybk.com.tw/cathaybk/personal/loan/calculator/mortgage-monthly-payments/")

# 查找元素
element_ids = ["reset", "formSubmitBtn", "navigationDetial","periodrate1"]

reset = [(By.ID, 'reset'), (By.XPATH, '//*[@id="reset"]')]
formSubmitBtn = [(By.ID, 'formSubmitBtn'), (By.XPATH, '//*[@id="formSubmitBtn"]')]
navigationDetial = [(By.ID, 'navigationDetial'), (By.XPATH, '//*[@id="navigationDetial"]')]

amount = [(By.ID, 'amount'), (By.XPATH, '//*[@id="amount"]')]
Fee = [(By.ID, 'Fee'), (By.XPATH, '//*[@id="Fee"]')]
periodrate1 = [(By.ID, 'periodrate1'), (By.XPATH, '//*[@id="periodrate1"]')]



element = driver.find_element(By.ID, 'amount')
element.clear()
element.send_keys(1000)

print(element)

driver.quit()
