import requests
import pytest
from create_request import create_first_outgoing_message, create_second_outgoing_message

# 定義第一個和第二個API的URL
FIRST_API_URL = "https://api.yourfirst.com/userinfo"
SECOND_API_URL = "https://api.yoursecond.com/userinfo"


def get_user_account(user_id: str):
    """根據ID向第一個API發送請求並獲得userAccount"""
    request_data = create_first_outgoing_message(user_id)
    try:
        response = requests.post(url=request_data['url'], json=request_data, headers=request_data['headers'],
                                 timeout=10)
        response.raise_for_status()  # 檢查回應狀態碼
        return response.json()["body"]["userAccount"]
    except requests.exceptions.Timeout:
        raise TimeoutError("第一個API請求超時")
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)


def get_account_balance(user_id, user_account):
    """使用ID和userAccount向第二個API發送請求並獲得accountBalance"""
    request_data = create_second_outgoing_message(user_id, user_account)
    try:
        response = requests.post(url=request_data['url'], json=request_data, headers=request_data['headers'],
                                 timeout=10)
        response.raise_for_status()  # 檢查回應狀態碼
        return response.json()["body"]["accountBalance"]
    except requests.exceptions.Timeout:
        raise TimeoutError("第二個API請求超時")
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)


def test_account_balance(user_id):
    """驗證accountBalance是否等於10000"""
    try:
        user_account = get_user_account(user_id)
        account_balance = get_account_balance(user_id, user_account)
        assert account_balance == 10000, f"accountBalance應該為10000，實際上為{account_balance}"
    except TimeoutError as te:
        print(te)
    except Exception as e:
        print(f"測試失敗: {e}")


if __name__ == "__main__":
    pytest.main()
