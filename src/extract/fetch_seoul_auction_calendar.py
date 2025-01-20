import requests as req
import json
from config.constants import SEOUL_CALENDAR_API_URL


def main():
    res = req.get(SEOUL_CALENDAR_API_URL)
    calendar_data = json.loads(res.text)['data']
    return calendar_data