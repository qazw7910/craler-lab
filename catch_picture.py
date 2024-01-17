from selenium import webdriver
import requests
from PIL import Image
from io import BytesIO

# 啟動 WebDriver
driver = webdriver.Chrome()

# 導航到目標網頁
driver.get("http://example.com")

# 定位圖片元素
image_element = driver.find_element_by_xpath("//img[@id='target-image']")

# 獲取圖片的 URL
image_url = image_element.get_attribute('src')

# 使用 requests 下載圖片
response = requests.get(image_url)

# 檢查請求是否成功
if response.status_code == 200:
    # 使用 PIL 庫打開圖片
    image = Image.open(BytesIO(response.content))
    # 保存圖片
    image.save("downloaded_image.jpg")

# 關閉瀏覽器
driver.quit()