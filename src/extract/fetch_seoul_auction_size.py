import requests as req
import json
from .utils.api_endpoints import get_online_url, get_major_url


def main(auction_code: int, auction_type='online'):
    if auction_type == 'online':
        url = get_online_url(auction_code=auction_code)
    elif auction_type == 'major':
        url = get_major_url(auction_code=auction_code)

    res = req.get(url)
    count = json.loads(res.text)['data']['cnt']
    if count:
        result = {
            "SALE_NO": auction_code,
            "SALE_KIND_CD": auction_type,
            "cnt": int(count)
        }
        return result