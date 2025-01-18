from load.load_calendar_to_mongodb import main as load_calendar_to_mongodb
from extract.scrape_seoul_auction_calendar import main as scrape_seoul_auction_calendar
# import sys
# import os
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

calendar_data = scrape_seoul_auction_calendar()
load_calendar_to_mongodb(upsert_data=calendar_data)
