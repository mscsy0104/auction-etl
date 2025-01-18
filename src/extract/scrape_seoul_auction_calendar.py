import requests as req
import json
import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    API_URL = os.getenv("SEOUL_CALENDAR_API_URL")

    res = req.get(API_URL)
    calendar_data = json.loads(res.text)['data']
    return calendar_data