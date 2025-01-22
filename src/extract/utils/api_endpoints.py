from config.constants import *


def build_auction_api_url(auction_type: str, auction_code: int):
    """
    경매에 출품하는 작품수 체크를 위한 경매 API URL 생성
    Generate an auction API URL to check the number of works submitted to the auction.

    Args:
        auction_type (str): The type of the auction.
        auction_code (int): The code of the auction.

    Returns:
        str: The constructed URL for the auction.
    """
    return f"{SEOUL_BASE_API_URI}{SEOUL_ENDPOINTS_TEMP.format(auction_type=auction_type, auction_code=auction_code)}{SEOUL_CARD_PARMAS}"


def build_api_url_with_size(auction_code: int, auction_type: str, size: int):
    """
    경매에 출품되는 작품정보 수집을 위한 상세한 경매 API URL 생성
    Generates a detailed auction API URL for collecting information on auctioned artworks.

    Args:
        auction_type (str): The type of the auction.
        auction_code (int): The code of the auction.
        size (int): The number of artworks to load on an auction site.
    Returns:
        str: The constructed URL for the auction.
    """
    return f"{SEOUL_BASE_API_URI}{SEOUL_ENDPOINTS_TEMP.format(auction_type=auction_type, auction_code=auction_code)}{SEOUL_CARD_PARMS_TEMP.format(size=size)}"


def build_details_url(auction_code: int, lot: int):
    """
    로트 상세 정보 API URL 생성
    Args:
        lot (int): 로트 번호
    Returns:
        str: 완성된 API URL
    """
    return f"{SEOUL_BASE_API_URI}{SEOUL_ENDPOINTS_TEMP.format(auction_code=auction_code)}{SEOUL_DETAIL_PARAMS_TEMP.format(lot=lot)}"