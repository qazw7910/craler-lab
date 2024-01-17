from selenium import webdriver

# 啟動 WebDriver
driver = webdriver.Chrome()

# 導航到包含文件上傳功能的網頁
driver.get("http://example.com/upload")

# 定位到文件上傳元素
file_input = driver.find_element_by_xpath("//input[@type='file']")

# 提供圖片文件的路徑（請確保路徑正確）
file_path = "/path/to/your/image.jpg"
file_input.send_keys(file_path)

# 如果需要，可以找到並點擊提交按鈕
submit_button = driver.find_element_by_xpath("//button[@id='submit']")
submit_button.click()

# 關閉瀏覽器
driver.quit()