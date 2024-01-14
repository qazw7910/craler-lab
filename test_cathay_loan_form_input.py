import pytest
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
# 測試函數
@pytest.mark.parametrize("loan_amount,related_costs,interest_rate", [(100, 10, 2.1)])
def test_mortgage_calculator(loan_amount, related_costs, interest_rate):
    # 初始化 WebDriver
    driver = webdriver.Chrome()  # 請替換為您的 WebDriver 路徑

    # 打開網頁
    driver.get("https://www.cathaybk.com.tw/cathaybk/personal/loan/calculator/mortgage-monthly-payments/")

    # 填入貸款金額
    loan_amount_element = driver.find_element(By.ID, "amt")
    loan_amount_element.clear()
    loan_amount_element.send_keys(str(loan_amount))

    # 填入相關費用
    related_costs_element = driver.find_element(By.ID, "fee")
    related_costs_element.clear()
    related_costs_element.send_keys(str(related_costs))

    # 填入利率
    interest_rate_element = driver.find_element(By.XPATH, '//*[@id="periodrate1"]')
    interest_rate_element.clear()
    interest_rate_element.send_keys(str(interest_rate))

    # 點擊開始試算按鈕
    calculate_button = driver.find_element(By.ID, "startcal")
    calculate_button.click()

    # 等待結果（這裡可能需要增加一些邏輯來等待計算結果的出現）

    # 關閉瀏覽器
    driver.quit()

# 這裡是主函數入口，用於執行測試
if __name__ == "__main__":
    pytest.main()
