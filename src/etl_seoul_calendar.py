from load.load_calendar_to_mongodb import main as load_calendar_to_mongodb
from extract.scrape_seoul_auction_calendar import main as scrape_seoul_auction_calendar
from logging_config import setup_logging
import logging

setup_logging()
logger = logging.getLogger(__name__)

calendar_data = scrape_seoul_auction_calendar()
load_calendar_to_mongodb(upsert_data=calendar_data)
