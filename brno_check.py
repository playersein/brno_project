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
    
def process_business_numbers(csv_file, api_key, ouput_file):
    """
    CSV 파일에서 사업자번호 읽기
    """
    # CSV 파일에서 사업자번호 읽기
    data = pd.read_csv(csv_file)
    if "business_number" not in data.columns:
        raise ValueError("CSV 파일에 business_number 열이 필요합니다.")
    
    results = []
    for business_number in data["busniess_number"]:
        status = check_business_status(api_key, str(business_number))
        results.append({"business_number": business_number, "python": status})
        
    # 결과를 dataframe으로 변환
    results_df = pd.DataFrame(results)
    
    # 결과를 Excel 파일로 저장
    results_df.to_excel(ouput_file, index=False)
    print(f"결과가 {ouput_file}에 저장되었습니다.")
    

if __name__=="__main__":
    API_KEY = f"hMT5bvJkHQNNiHWuh1rE3Bb1xHtOE6vdjpe%2FJEpLO7OoHq3KMU1lBQ8uYTMOjf3mRhx2IOwQyYwqueG60eEcVQ%3D%3D"
    INPUT_CSV ="/Users/seinmyeong/Desktop/data/business_numbers.csv"
    OUTPUT_EXCEL = "business_status_results.xlsx"
    
    process_business_numbers(INPUT_CSV, API_KEY, OUTPUT_EXCEL)