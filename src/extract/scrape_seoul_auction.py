import pandas as pd
import requests as req
import json
import os
from dotenv import load_dotenv

load_dotenv()
API_URL = os.getenv("SEOUL_API_URL")

res = req.get(API_URL)
data = json.loads(res.text)['data'][0]
from pprint import pprint
pprint(data)

