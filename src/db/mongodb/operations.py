from pymongo.collection import Collection
from pymongo.database import Database
from datetime import datetime
import pytz


def make_timestamp():
    seoul_tz = pytz.timezone('Asia/Seoul')
    current_time = datetime.now(seoul_tz)
    return current_time

    
def find_document(collection: Collection, filter: dict):
    """
    Find a document in the collection matching the filter.
    """
    try:
        return collection.find_one(filter)
    except Exception as e:
        raise Exception(f"Error finding documents: {e}")
    

def find_documents(collection: Collection, filter: dict):
    """
    Find documents in the collection matching the filter.
    """
    try:
        return list(collection.find(filter))
    except Exception as e:
        raise Exception(f"Error finding documents: {e}")


def insert_document(collection: Collection, document: dict):
    """
    Insert a single document into the collection.
    """
    try:
        current_time = make_timestamp()
        document['created_at'] = current_time
        result = collection.insert_one(document)
        return result.inserted_id
    except Exception as e:
        raise Exception(f"Error inserting document: {e}")
    

def insert_documents(collection: Collection, documents: list):
    """
    Insert multiple documents into the collection.
    """
    try:
        current_time = make_timestamp()
        for document in documents:
            document['created_at'] = current_time
        result = collection.insert_many(documents)
        return result.inserted_ids
    except Exception as e:
        raise Exception(f"Error inserting documents: {e}")
    

def update_document(collection: Collection, filter: dict, document: dict):
    """
    Update a single document in the collection.
    """
    try:
        current_time = make_timestamp()
        document['updated_at'] = current_time
        result = collection.update_one(filter, {"$set": document})
        if result.modified_count > 0:
            doc_to_find = find_document(collection, filter)
            if doc_to_find:
                oid = doc_to_find["_id"]
                return oid
    except Exception as e:
        raise Exception(f"Error updating document: {e}")
    

def update_documents(collection: Collection, filters: dict, documents: dict):
    """
    Update many documents in the collection.
    """
    try:
        updated_ids = []
        keys = filters.keys()
        for key in keys:
            filter, doc = filters[key], documents[key]
            updated_id = update_document(collection, filter, doc)
            updated_ids.append(updated_id)
        return updated_ids
    except Exception as e:
        raise Exception(f"Error updating documents: {e}")


def update_matching_one(collection: Collection, filter: dict, document: dict):
    """
    Update a single document in the collection.
    """
    try:        
        current_time = make_timestamp()
        document['updated_at'] = current_time
        result = collection.update_many(filter, {"$set": document})
        oids = []
        if result.modified_count > 0:
            oids = find_documents(collection, filter)
        return oids
    except Exception as e:
        raise Exception(f"Error updating document: {e}")
    

def delete_document(collection: Collection, filter: dict):
    """
    Delete a single document from the collection.
    """
    try:
        result = collection.delete_one(filter)
        return result.deleted_count
    except Exception as e:
        raise Exception(f"Error deleting document: {e}")
    

def get_all_document_ids(collection: Collection):
    """
    Get all document IDs from the specified collection.
    """
    try:
        documents = collection.find({}, {"_id": 1})
        document_ids = [doc["_id"] for doc in documents]
        return document_ids
    except Exception as e:
        raise Exception(f"Error retrieving document IDs: {e}")
    

def get_collection_names(database: Database):
    """
    Get all document names from the specified collection.
    """
    try:
        collection_names = database.list_collection_names
        return collection_names
    except Exception as e:
        raise Exception(f"Error retrieving document names: {e}")