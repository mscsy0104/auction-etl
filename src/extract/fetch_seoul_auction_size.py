import requests as req
import json
from .utils.api_endpoints import get_auction_api_url
import logging

logger = logging.getLogger(__name__)

def main(auction_type: str, auction_code: int):
    try:
        api_url = get_auction_api_url(auction_type=auction_type, auction_code=auction_code)
    except Exception as e:
        logger.error(f"Failed to get auction API URL for auction_code: {auction_code}, auction_type: {auction_type}. Error: {e}")
        
    res = req.get(api_url)
    count = json.loads(res.text)['data']['cnt']
    if not count:
        return 0
    return count
