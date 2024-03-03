# create_request.py

def create_first_outgoing_message(user_id: str):
    """根據提供的ID生成第一個API的上行電文"""
    request_data = {
        "url": "https://api.yourfirst.com/userinfo",
        "header": {
            "contentType": "application/json",
            "method": "POST",
            "authorization": "Bearer your_access_token_here"
        },
        "body": {
            "ID": user_id
        }
    }
    return request_data


def create_second_outgoing_message(user_id: str, user_account: str):
    request_data = {
        "url": "https://api.yoursecond.com/userinfo",
        "header": {
            "contentType": "application/json",
            "method": "POST",
            "authorization": "Bearer another_access_token_here"
        },
        "body": {
            "ID": user_id,
            "userAccount": user_account
        }
    }
    return request_data


if __name__ == '__main__':
    print(create_first_outgoing_message('qazw7910'))
