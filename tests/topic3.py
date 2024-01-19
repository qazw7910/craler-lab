from time import sleep
from ..random_generate.national_id import generate_id
from ..random_generate.phone import generate_phone
from ..module.external_data import ExternalData
from ..module.id_maker import IDMaker
import pytest
import pyautogui

import config

pytestmark = pytest.mark.insurance

external_data = ExternalData()

name = '陳柏志'
national_id = generate_id()
phone = generate_phone()
account = '0000014294875444'
id_image = IDMaker(phone)
id_image.id_image_maker()
id_image.id_barcode_maker()
id_font = IDMaker.path_return("result_image_1.png")
id_back = IDMaker.path_return("id_back_barcode_1.png")
financial_proof = IDMaker.path_return("financial_proof.jpg")
last_name = 'PO'
first_name = 'CHEN'
card_change_date = '1000217'
birth_date = '0850217'
company_name = '國泰'
company_address = '凱達格蘭大道3號'
registration_address = '凱達格蘭大道3號'
email = 'ojghoajg@gmail.com'


def test_wrong_verification_code_error(chrome_driver, screenshot_finalizer, credit_card_apply_page,
                                       credit_card_apply_page2, credit_card_apply_page3, credit_card_apply_page4,
                                       credit_card_apply_page5, credit_card_apply_page6, credit_card_apply_page7,
                                       credit_card_apply_page8, credit_card_apply_page9, credit_card_apply_page10):
    # ----------------------page 1 選擇卡類------------------------------
    chrome_driver.get(config.EndPoint.cube_card_apply.value)
    credit_card_apply_page.click_application_card_function_choose()
    credit_card_apply_page.click_application_card_function_select()
    credit_card_apply_page.click_application_card_apply_now()
    # ----------------------page 2 身分驗證------------------------------
    credit_card_apply_page2.set_national_id(national_id)
    credit_card_apply_page2.set_mobile_number(phone)
    sleep(5)
    credit_card_apply_page2.click_confirm()
    # ----------------------page 3 輸入opt碼------------------------------
    otp_code = external_data.get_otp(national_id)
    credit_card_apply_page3.set_otp_code(otp_code)
    credit_card_apply_page3.click_next()
    # ----------------------page 4 身分資料------------------------------
    credit_card_apply_page4.set_name(name)
    credit_card_apply_page4.click_confirm()
    # ----------------------page 5 選擇身分驗證方式------------------------------
    credit_card_apply_page5.click_next()
    # ----------------------page 6 身分驗證------------------------------
    credit_card_apply_page6.set_mobile_number(phone)
    credit_card_apply_page6.click_bank_code_field()
    credit_card_apply_page6.click_bank_code()
    credit_card_apply_page6.set_account_number(account)
    credit_card_apply_page6.click_next_1()
    credit_card_apply_page6.click_next_2()
    # ----------------------page 7 文件上傳------------------------------
    credit_card_apply_page7.click_closed_btn()
    credit_card_apply_page7.click_upload_id_front()
    pyautogui.typewrite(id_font)
    pyautogui.press('enter')
    credit_card_apply_page7.click_upload_id_back()
    pyautogui.typewrite(id_back)
    pyautogui.press('enter')
    credit_card_apply_page7.click_upload_financial_proof()
    pyautogui.typewrite(financial_proof)
    pyautogui.press('enter')
    credit_card_apply_page7.click_store_btn()
    credit_card_apply_page7.click_store_success_return_btn()
    credit_card_apply_page7.click_store_skip()
    # ----------------------page 8 基本資料------------------------------
    credit_card_apply_page8.set_last_name(last_name)
    credit_card_apply_page8.set_first_name(first_name)
    credit_card_apply_page8.set_id_card_change_date(card_change_date)
    credit_card_apply_page8.click_id_card_change_palace_choose()
    credit_card_apply_page8.click_id_card_change_palace_select()
    credit_card_apply_page8.click_id_card_change_status_choose()
    credit_card_apply_page8.click_id_card_change_status_select()
    credit_card_apply_page8.set_birth_date(birth_date)
    credit_card_apply_page8.click_marital_status_choose()
    credit_card_apply_page8.click_marital_status_select()
    credit_card_apply_page8.click_highest_education_choose()
    credit_card_apply_page8.click_highest_education_select()
    credit_card_apply_page8.click_current_industry_choose()
    credit_card_apply_page8.click_current_industry_select()
    credit_card_apply_page8.click_industry_category_choose()
    credit_card_apply_page8.click_industry_category_select()
    credit_card_apply_page8.click_job_title_choose()
    credit_card_apply_page8.click_job_title_select()
    credit_card_apply_page8.set_company_name(company_name)
    credit_card_apply_page8.click_company_city_choose()
    credit_card_apply_page8.click_company_city_select()
    credit_card_apply_page8.click_company_region_choose()
    credit_card_apply_page8.click_company_region_select()
    credit_card_apply_page8.set_company_address(company_address)
    credit_card_apply_page8.click_current_job_exp_choose()
    credit_card_apply_page8.click_current_job_exp_select()
    credit_card_apply_page8.click_repayment_resource_checkbox()
    credit_card_apply_page8.click_registration_city_choose()
    credit_card_apply_page8.click_registration_city_select()
    credit_card_apply_page8.click_registration_region_choose()
    credit_card_apply_page8.click_registration_region_select()
    credit_card_apply_page8.set_registration_address(registration_address)
    credit_card_apply_page8.click_current_live_address_checkbox()
    credit_card_apply_page8.click_house_ownership_choose()
    credit_card_apply_page8.click_house_ownership_select()
    credit_card_apply_page8.set_email_address(email)
    credit_card_apply_page8.click_agree_rule_checkbox()
    credit_card_apply_page8.click_card_receive_address_choose()
    credit_card_apply_page8.click_card_receive_address_select()
    credit_card_apply_page8.set_verification_email(email)
    credit_card_apply_page8.click_email_verification_btn()
    # email_otp 獲取
    email_otp_code = external_data.get_otp(national_id)
    credit_card_apply_page8.set_email_verification_code(email_otp_code)
    credit_card_apply_page8.click_email_verification_code_confirm()
    credit_card_apply_page8.click_personal_info_store()
    credit_card_apply_page8.click_after_store_return()
    credit_card_apply_page8.click_next_step()
    credit_card_apply_page8.click_info_double_check()
    # ----------------------page 9 加值服務------------------------------
    credit_card_apply_page9.click_next_step_10()
    # ----------------------page 10 資料確認------------------------------
    credit_card_apply_page10.click_agree_rule_checkbox_1()
    credit_card_apply_page10.click_agree_rule_checkbox_2()
    credit_card_apply_page10.click_store()
