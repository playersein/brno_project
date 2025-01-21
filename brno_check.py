import requests
import pandas as pd

def check_business_status(api_key, business_number):
    """
    API를 통해 사업자등록번호의 상태를 조회한다.
    """
    url = "https://infuser.odcloud.kr/api/stages/28493/api-docs?1728017570963"
    payload = {
        "businessNumber": business_number,
        "apiKey": api_key
    }

    try:
        response = requests.post(url, json= payload)
        if response.status_code == 200:
            result = response.json()
            return result.get("status", "unknown")
        else:
            return f"Error {response.status_code}"
    except Exception as e:
        return f"Error{str(e)}"