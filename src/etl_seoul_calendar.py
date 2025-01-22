
"""
목적: 서울옥션의 캘린더 데이터 수집을 한 뒤, 해당 데이터를 통해 옥션에 출품되는 작품수를 fetch하고, 최종 metadata를 만드는 것이 목적
이유: 각 옥션의 작품데이터를 수집하기 위한 API URL을 만들기 위해 필요한 사전작업이다.
Purpose: To collect calendar data from Seoul Auction, fetch the number of artworks for each auction, and build the final metadata.
Reason: This is a preliminary task necessary to create the API URL required to collect artwork data for each auction.

Functions:
    get_metadata_from_calendar_data(calendar_data):
        Extracts auction details (codes, types, statuses) from calendar data.

    build_auction_metadata(metadata_from_calendar_data):
        Fetches and collects auction details with sizes.

    main():
        Main function to load calendar data into MongoDB, build metadata, and load metadata into MongoDB.
"""

from load.load_metadata_to_mongodb import main as load_metadata_to_mongodb
from extract.fetch_seoul_auction_calendar import main as fetch_seoul_auction_calendar
from extract.fetch_seoul_auction_size import main as fetch_seoul_auction_size
from logging_config import setup_logging
import logging

setup_logging()
logger = logging.getLogger(__name__)


def get_metadata_from_calendar_data(calendar_data):
    """Extracts auction details (codes, types, statuses) from calendar data."""
    return [(data["SALE_NO"], data["SALE_KIND_CD"], data["STAT_CD"]) for data in calendar_data]

def build_auction_metadata(metadata_from_calendar_data):
    """Fetches and collects auction details with sizes."""
    metadata_with_sizes = []
    for code, auction_type, status in metadata_from_calendar_data:
        if status == 'open':
            size = fetch_seoul_auction_size(auction_code=code, auction_type=auction_type)
            result = {
                    "SALE_KIND_CD": auction_type,
                    "SALE_NO": code,
                    "STAT_CD": status,
                    "cnt": int(size)
                }
            if result:
                metadata_with_sizes.append(result)

    return metadata_with_sizes


def main():
    # Load calendar data into mongodb
    calendar_data = fetch_seoul_auction_calendar()
    load_metadata_to_mongodb(upsert_data=calendar_data, collection_name="seoul_auction_calendar")

    # Build metadata
    metadata_from_calendar_data = get_metadata_from_calendar_data(calendar_data) # tuples in list(LOT)
    auction_metadata = build_auction_metadata(metadata_from_calendar_data) # dictionaries in list(LOD)

    load_metadata_to_mongodb(upsert_data=auction_metadata, collection_name="seoul_auction_metadata")


if __name__ == "__main__":
    main()