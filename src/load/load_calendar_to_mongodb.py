from dotenv import load_dotenv
import os
from db.mongodb.connection import MongoDBConnection
from db.mongodb.operations import *
import logging
import traceback

logging.basicConfig(level=logging.INFO)

def main(upsert_data: list):
    try:
        # Initialize connection
        load_dotenv()
        uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
        connection = MongoDBConnection(uri)

        # Connect to MongoDB
        connection.connect()

        # Access database and collection
        db_name = os.getenv("MONGO_DB")
        db = connection.get_database(db_name)
        collection = db["seoul_auction_calendar"]

        sale_numbers = [datum["SALE_NO"] for datum in upsert_data]
        # data를 순회하면서 SALE_NO가 있으면 그거 업데이트
        #  없으면 insert 하는 걸로
        documents = list(collection.find({}, {"_id":-1, "SALE_NO":-1}))
        oid_salenum = {item['_id']: {'SALE_NO': item['SALE_NO']} for item in documents}
        inserted_ids = updated_ids = []
        if documents == []:
            inserted_ids = insert_documents(collection=collection, documents=upsert_data)

        else:
            existed_sale_nums = [doc["SALE_NO"] for doc in documents]

            update_sale_nums = []
            insert_sale_nums = []
            inserting_docs = updating_docs = []
            for number in sale_numbers:
                if number in existed_sale_nums:
                    update_sale_nums.append(number)
            
            insert_sale_nums = [num for num in sale_numbers if num not in update_sale_nums]

            inserting_docs = [doc for doc in upsert_data if doc["SALE_NO"] in insert_sale_nums]
            updating_docs = [doc for doc in upsert_data if doc["SALE_NO"] in update_sale_nums]


            update_filters = [{"SALE_NO":num} for num in update_sale_nums]
            updated_ids = update_documents(collection=collection, filters=update_filters, documents=updating_docs)
            if inserting_docs != []:
                inserted_ids = insert_documents(collection=collection, documents=inserting_docs)

        logging.info("-"*50)
        logging.info(f"Inserted IDs: {inserted_ids}")
        logging.info(f"Updated IDs: {updated_ids}")
        # logging.info(f"Inserted SALE_NO: {}")
        # logging.info(f"Updated SALE_NO: {}")

        logging.info("Upserted Well!")
        logging.info("-"*50)

        # logging.info(f"Upserted ID: {upserted_id}")
    except Exception as e:
        logging.info(f"Error: {traceback.format_exc()}")
    finally:
        connection.close()