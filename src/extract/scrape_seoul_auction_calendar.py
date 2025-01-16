import requests as req
import json
# 해당 파일에서 바로 테스트하고 싶을 때 다른 폴더의 모듈을 불러오기 전 아래 사항을 작성해준다.
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from db.mongodb.main import main as load_mongodb
from dotenv import load_dotenv

load_dotenv()
API_URL = os.getenv("SEOUL_CALENDAR_API_URL")

res = req.get(API_URL)
data = json.loads(res.text)['data'][0]
load_mongodb(upsert_data=data)
# from pprint import pprint
# pprint(data)

# df = pd.DataFrame(data)
# from datetime import datetime
# dtime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# filepath = f"./results/seoul_calendar_{dtime}.xlsx"
# df.to_excel(filepath)