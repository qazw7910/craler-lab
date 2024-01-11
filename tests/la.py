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
    e_bill_id_check_page.click_refresh_verify_code()
    src2 = e_bill_id_check_page.get_attr_from_verify_src()
    assert src1 != src2
