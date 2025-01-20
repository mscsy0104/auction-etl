from config.constants import *


def get_online_url(auction_code: int):
    """
    Constructs the online URL for a given auction code.

    Args:
        auction_code (int): The code of the auction.

    Returns:
        str: The constructed URL for the online auction.
    """
    return f"{SEOUL_BASE_API_URI}{SEOUL_ONLINE_PATH_TEMP.format(auction_code=auction_code)}{SEOUL_CARD_PARMAS}"


def get_major_url(auction_code: int):
    """
    Constructs the online URL for a given auction code.

    Args:
        auction_code (int): The code of the auction.

    Returns:
        str: The constructed URL for the online auction.
    """
    return f"{SEOUL_BASE_API_URI}{SEOUL_MAJOR_PATH_TEMP.format(auction_code=auction_code)}{SEOUL_CARD_PARMAS}"


def get_online_url_with_size(auction_code: int, size: int):
    """
    온라인 세일즈 API URL 생성
    Args:
        code (int): 세일즈 코드
        size (int): load하는 사이즈 기준
    Returns:
        str: 완성된 API URL
    """
    return f"{SEOUL_BASE_API_URI}{SEOUL_ONLINE_PATH_TEMP.format(auction_code=auction_code)}{SEOUL_CARD_PARMS_TEMP.format(size=size)}"


def get_major_url_with_size(auction_code: int, size: int):
    """
    메이저 세일즈 API URL 생성
    Args:
        code (int): 세일즈 코드
        size (int): load하는 사이즈 기준
    Returns:
        str: 완성된 API URL
    """
    return f"{SEOUL_BASE_API_URI}{SEOUL_MAJOR_PATH_TEMP.format(auction_code=auction_code)}{SEOUL_CARD_PARMS_TEMP.format(size=size)}"


def get_details_url(auction_code: int, lot: int):
    """
    로트 상세 정보 API URL 생성
    Args:
        lot (int): 로트 번호
    Returns:
        str: 완성된 API URL
    """
    return f"{SEOUL_BASE_API_URI}{SEOUL_ONLINE_PATH_TEMP.format(auction_code=auction_code)}{SEOUL_DETAIL_PARAMS_TEMP.format(lot=lot)}"