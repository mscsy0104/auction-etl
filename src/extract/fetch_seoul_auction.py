import pandas as pd
import requests as req
import json
from .utils.api_endpoints import get_online_url_with_size, get_major_url_with_size


def main(auction_code: int, size: int, auction_type='online'):
    if auction_type == 'online':
        url_with_size = get_online_url_with_size(auction_code=auction_code, size=size)
    elif auction_type == 'major':
        url_with_size = get_major_url_with_size(auction_code=auction_code, size=size)
    
    res = req.get(url_with_size)
    data = json.loads(res.text)['data']['list']
    return data

