import requests
import pytest
from create_request import create_first_outgoing_message, create_second_outgoing_message


class InvalidResponseError(Exception):
    pass


def get_user_account(user_id: str):
    """根據ID向第一個API發送請求並獲得userAccount"""
    request_data = create_first_outgoing_message(user_id)

    response = requests.post(url=request_data['url'], json=request_data, headers=request_data['headers'],
                             timeout=10)
    response.raise_for_status()  # 檢查回應狀態碼
    data = response.json()
    if 'body' not in data or 'user_account' not in data['body']:
        raise InvalidResponseError
    assert response.status_code == 200
    return response.json()["body"]["userAccount"]


def get_account_balance(user_id, user_account):
    """使用ID和userAccount向第二個API發送請求並獲得accountBalance"""
    request_data = create_second_outgoing_message(user_id, user_account)

    response = requests.post(url=request_data['url'], json=request_data, headers=request_data['headers'],
                             timeout=10)
    response.raise_for_status()  # 檢查回應狀態碼
    assert response.status_code == 200
    return response.json()["body"]["accountBalance"]


def test_account_balance(user_id):
    """驗證accountBalance是否等於10000"""
    user_account = get_user_account(user_id)
    account_balance = get_account_balance(user_id, user_account)
    assert account_balance == 10000, f"accountBalance應該為10000，實際上為{account_balance}"


if __name__ == "__main__":
    pytest.main()
