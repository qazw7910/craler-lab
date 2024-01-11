import allure
import pytest
import config

pytestmark = pytest.mark.insurance


def test_wrong_verification_code_error(chrome_driver, screenshot_finalizer, e_bill_id_check_page):
    """
        Preconditions:
            1. open browser go to e-bill apply page
        Test steps:
            1. set national id
            2. set mobile
            3. set verification code 1234
            4. click confirm
        Expected result:
            1. error message 請輸入正確的驗證碼
    """
    chrome_driver.get(config.EndPoint.e_bill_id_check.value)
    e_bill_id_check_page.set_national_id('A123456789')
    e_bill_id_check_page.set_mobile_number('0910873180')
    e_bill_id_check_page.set_verification_code('1234')
    e_bill_id_check_page.click_confirm()
    assert e_bill_id_check_page.get_captcha_error_text() == '請輸入正確的驗證碼。'


'''
        Preconditions:
            1. open browser go to e-bill apply page
        Test steps:
            1. 網頁讀取完成
        Expected result:
            1. 網頁上取得文字 個人資料保護法告知內容
'''


# ============================================================
# @pytest.mark.P1
def test_get_content(chrome_driver, screenshot_finalizer, e_bill_id_check_page):
    '''
        Preconditions:
            1. open browser go to e-bill apply page
        Test steps:
            1. 網頁讀取完成
        Expected result:
            1. 網頁上取得文字 個人資料保護法告知內容
    '''
    chrome_driver.get(config.EndPoint.e_bill_id_check.value)
    assert e_bill_id_check_page.get_captcha_text() == '個人資料保護法告知內容'
    e_bill_id_check_page.click_confirm()


# @pytest.mark.P1
def test_get_error_message(chrome_driver, screenshot_finalizer, e_bill_id_check_page):
    '''

        Preconditions:
            1. open browser go to e-bill apply page
        Test steps:
            1. 點擊確認送出
        Expected result:
            1. error message 請輸入身分證字號
            1. error message 請輸入行動電話
            1. error message 請輸入驗證碼

    '''
    chrome_driver.get(config.EndPoint.e_bill_id_check.value)
    e_bill_id_check_page.click_confirm()
    assert e_bill_id_check_page.get_captcha_error_massage_input_national_id() == '請輸入身分證字號'
    assert e_bill_id_check_page.get_captcha_error_massage_input_national_mobile() == '請輸入行動電話'
    assert e_bill_id_check_page.get_captcha_error_text() == '請輸入驗證碼'


# @pytest.mark.P1
def test_get_refresh_verify_code(chrome_driver, screenshot_finalizer, e_bill_id_check_page):
    '''

        Preconditions:
            1. open browser go to e-bill apply page
        Test steps:
            1. 點擊重新整理
        Expected result:
            1. 驗證碼會刷新成功
    '''
    chrome_driver.get(config.EndPoint.e_bill_id_check.value)
    src1 = e_bill_id_check_page.get_attr_from_verify_src()
    from base_web import Page
    screenshot_name, screenshot_path = Page(chrome_driver).get_screenshot(method_name='src1')
    allure.attach.file(screenshot_path, screenshot_name, allure.attachment_type.PNG)
    e_bill_id_check_page.click_refresh_verify_code()
    src2 = e_bill_id_check_page.get_attr_from_verify_src()
    assert src1 != src2


@pytest.mark.P1
def test_get_file_is_pdf(chrome_driver, screenshot_finalizer, e_bill_id_check_page):
    '''
        Preconditions:
            1. open browser go to e-bill apply page
        Test steps:
            1. 點擊 個人資料保護法告知內容 超連結
        Expected result:
            1. 驗證點擊跳轉為pdf
    '''
    chrome_driver.get(config.EndPoint.e_bill_id_check.value)
    content = e_bill_id_check_page.get_attr_from_personal_info_href()
    assert '.pdf' in content
    e_bill_id_check_page.click_personal_info_href()
    from base_web import Page
    screenshot_name, screenshot_path = Page(chrome_driver).get_screenshot(method_name='src1')
    allure.attach.file(screenshot_path, screenshot_name, allure.attachment_type.PNG)
    assert content in chrome_driver.current_url
