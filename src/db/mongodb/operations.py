from pymongo.collection import Collection


def insert_document(collection: Collection, document: dict):
    """
    Insert a single document into the collection.
    """
    try:
        result = collection.insert_one(document)
        return result.inserted_id
    except Exception as e:
        raise Exception(f"Error inserting document: {e}")
    

def insert_documents(collection: Collection, documents: list):
    """
    Insert multiple documents into the collection.
    """
    try:
        result = collection.insert_many(documents)
        return result.inserted_ids
    except Exception as e:
        raise Exception(f"Error inserting documents: {e}")
    

def update_document(collection: Collection, query: dict, update: dict):
    """
    Update a single document in the collection.
    """
    try:
        result = collection.update_one(query, {"$set": update})
        return result.modified_count
    except Exception as e:
        raise Exception(f"Error updating document: {e}")
    

def update_documents(collection: Collection, query: dict, update: dict):
    """
    Update a single document in the collection.
    """
    try:
        result = collection.update_many(query, {"$set": update})
        return result.modified_count
    except Exception as e:
        raise Exception(f"Error updating document: {e}")
    

def delete_document(collection: Collection, query: dict):
    """
    Delete a single document from the collection.
    """
    try:
        result = collection.delete_one(query)
        return result.deleted_count
    except Exception as e:
        raise Exception(f"Error deleting document: {e}")
    

def find_documents(collection: Collection, query: dict):
    """
    Find documents in the collection matching the query.
    """
    try:
        return list(collection.find(query))
    except Exception as e:
        raise Exception(f"Error finding documents: {e}")
    

def upsert_document(collection: Collection, query: dict, upsert_data: dict):
    """
    Insert or update a document in the collection.
    
    :param collection: MongoDB collection object
    :param query: Query to find the document
    :param upsert_data: Fields to update or insert
    :return: ID of the inserted or updated document
    """
    try:
        result = collection.update_one(query, {"$set": upsert_data}, upsert=True)
        
        if result.upserted_id:
            # Document was inserted
            return result.upserted_id
        else:
            # Document was updated, find its _id
            existing_document = collection.find_one(query)
            return existing_document["_id"] if existing_document else None
    except Exception as e:
        raise Exception(f"Error inserting or updating document: {e}")
