from load.load_metadata_to_mongodb import main as load_metadata_to_mongodb
from load.load_auctions_to_mongodb import main as load_auctions_to_mongodb
from extract.fetch_seoul_auction import main as fetch_seoul_auction
from extract.fetch_seoul_auction_calendar import main as fetch_seoul_auction_calendar
from extract.fetch_seoul_auction_size import main as fetch_seoul_auction_size
from logging_config import setup_logging
import logging

setup_logging()
logger = logging.getLogger(__name__)

calendar_data = fetch_seoul_auction_calendar()
load_metadata_to_mongodb(upsert_data=calendar_data, collection_name="seoul_auction_calendar")

auction_codes = [datum["SALE_NO"] for datum in calendar_data]
auction_types = [datum["SALE_KIND_CD"] for datum in calendar_data]
auction_code_type_and_sizes = []
for code, type in zip(auction_codes, auction_types):
    auction_code_type_size_mapping = fetch_seoul_auction_size(auction_code=code, auction_type=type)
    if auction_code_type_size_mapping:
        auction_code_type_and_sizes.append(auction_code_type_size_mapping)

load_metadata_to_mongodb(upsert_data=auction_code_type_and_sizes, collection_name="seoul_auction_size")