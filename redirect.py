from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch()  # 或使用 .firefox 或 .webkit
    context = browser.new_context()

    # 监听响应事件
    def handle_response(response):
        if response.status == 302:  # 检查状态码是否为 302
            location_header = response.headers.get('location')  # 获取 Location 头的值
            print(f"捕获到重定向: {location_header}")

    context.on("response", handle_response)

    page = context.new_page()
    page.goto("https://example.com")  # 替换为你的目标 URL
    # 执行其他操作...

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
