from dotenv import load_dotenv
import os
from .connection import MongoDBConnection
from .operations import insert_document, update_document, find_documents, upsert_document
import logging

logging.basicConfig(level=logging.INFO)

def main(upsert_data):
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
        match_field = input("Input matching field: ")
        match_value = input("Input matching value: ")
        query = dict({match_field:match_value})
        upserted_id = upsert_document(collection, query, upsert_data)
        logging.info(f"Upserted ID: {upserted_id}")

        # Example operations
        # Insert document
        # doc = {"name": "Alice", "age": 25}
        # inserted_id = insert_document(collection, doc)
        # logging.info(f"Inserted document ID: {inserted_id}")

        # # Update document
        # updated_count = update_document(collection, {"name": "Alice"}, {"age": 26})
        # logging.info(f"Number of documents updated: {updated_count}")

        # # Find documents
        # results = find_documents(collection, {"age": 26})
        # logging.info(f"Documents found: {results}")

    except Exception as e:
        logging.info(f"Error: {e}")
    finally:
        connection.close()