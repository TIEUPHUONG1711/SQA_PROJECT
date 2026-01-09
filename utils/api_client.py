   # gọi API 
   
import requests
import time 
import pandas as pd

def get_users(url):
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return response, elapsed_time   
 

def save_users_to_csv(data, path):
    df = pd.DataFrame(data)
    df.to_csv(path, index=False)
#đoạn code trên để gọi API lấy dữ liệu người dùng, thời gian trả lời của api và lưu vào file CSV    