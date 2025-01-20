from dotenv import load_dotenv
import os
from db.mongodb.connection import MongoDBConnection
from db.mongodb.operations import *
import logging
import traceback

logger = logging.getLogger(__name__)

def main(upsert_data: list, collection_name="seoul_auction", upsert="insert"):
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
        collection = db[collection_name]
        
        # update할 SALE_NO 추리기
        existed_sale_nums = [doc["SALE_NO"] for doc in documents]
        for number in sale_numbers:
            if number in existed_sale_nums:
                sale_nums_to_update.append(number)
        # insert할 SALE_NO 추리기
        sale_nums_to_insert = [num for num in sale_numbers if num not in sale_nums_to_update]

        # update, insert할 docs 추리기
        docs_to_insert = [doc for doc in upsert_data if doc["SALE_NO"] in sale_nums_to_insert]
        # docs_to_update = [doc for doc in upsert_data if doc["SALE_NO"] in sale_nums_to_update]
        docs_to_update_dict = {doc["SALE_NO"]: doc for doc in upsert_data if doc["SALE_NO"] in sale_nums_to_update}
        filters_to_update_dict = {doc["SALE_NO"]: {"SALE_NO": doc["SALE_NO"]} for doc in upsert_data if doc["SALE_NO"] in sale_nums_to_update}
        # update_filters = [{"SALE_NO":num} for num in sale_nums_to_update]

        updated_ids = update_documents(collection=collection, filters=filters_to_update_dict, documents=docs_to_update_dict)
        # updated_ids = update_documents(collection=collection, filters=update_filters, documents=docs_to_update)
        if docs_to_insert != []:
            inserted_ids = insert_documents(collection=collection, documents=docs_to_insert)

        # 로깅 메시지 템플릿
        log_template = """
        {separator}
        Inserted IDs(count: {inserted_ids_count}): {inserted_ids}
        Updated IDs(count: {updated_ids_count}): {updated_ids}
        Inserted SALE_NO(count: {inserted_salenums_count}): {sale_nums_to_insert}
        Updated SALE_NO(count: {updated_salenums_count}): {sale_nums_to_update}
        {separator}
        Upserted Well!
        {separator}
        """

        # 로깅 출력
        logger.info(log_template.format(
            separator="-" * 50,
            inserted_ids=inserted_ids,
            inserted_ids_count = len(inserted_ids),
            updated_ids=updated_ids,
            updated_ids_count=len(updated_ids),
            sale_nums_to_insert=sale_nums_to_insert,
            inserted_salenums_count=len(sale_nums_to_insert),
            sale_nums_to_update=sale_nums_to_update,
            updated_salenums_count=len(sale_nums_to_update),
        ))

        # logger.info(f"Upserted ID: {upserted_id}")
    except Exception as e:
        logger.info(f"Error: {traceback.format_exc()}")
    finally:
        connection.close()