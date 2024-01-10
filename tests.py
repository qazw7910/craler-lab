from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Correct the path if necessary and make sure the executable is in the specified directory.
chrome_path = './chromedriver.exe'

# Create a Service object using the path to the chromedriver
service = Service(executable_path=chrome_path)

# Pass the service object to the driver
driver = webdriver.Chrome(service=service)

driver.get('https://www.cathaybk.com.tw/cathaybk/')

sleep(3)

# Include the file extension .png for the screenshot
driver.save_screenshot('1.png')

driver.quit()
