from load.load_auctions_to_mongodb import main as load_auctions_to_mongodb
from extract.fetch_seoul_auction import main as fetch_seoul_auction
from dotenv import load_dotenv
import os
from db.mongodb.connection import MongoDBConnection
from db.mongodb.operations import get_collection_names
from logging_config import setup_logging
import logging

setup_logging()
logger = logging.getLogger(__name__)


load_dotenv()
uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
connection = MongoDBConnection(uri)

connection.connect()

db_name = os.getenv("MONGO_DB")
db = connection.get_database(db_name)
collection = db["seoul_auction_size"]
documents = list(collection.find({}, {"_id": -1, "SALE_NO": -1}))

collection_names = get_collection_names(db)

for doc in documents:
    auction_code = doc["SALE_NO"]
    size = doc["cnt"]
    auction_type = doc["SALE_KIND_CD"]

    collection_name = f"seoul_auction_{auction_type}_{auction_code}"
    auction_data = fetch_seoul_auction(auction_code=auction_code, size=size, auction_type=auction_type)
    if collection_name not in collection_names:
        load_auctions_to_mongodb(upsert_data=auction_data, collection_name=collection_name, upsert=insert)
    else:
        load_auctions_to_mongodb(upsert_data=auction_data, collection_name=collection_name, upsert=update)
