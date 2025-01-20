from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure
import logging

logger = logging.getLogger(__name__)


class MongoDBConnection:
    def __init__(self, uri="mongodb://localhost:27017/"):
        """
        Initialize MongoDB client with the provided URI.
        """
        self.uri = uri
        self.client = None

    def connect(self):
        """
        Create a MongoDB client connection.
        """
        try:
            self.client = MongoClient(self.uri)
            # Test connection
            self.client.admin.command("ping")
            logger.info("MongoDB connection established successfully.")
        except ConnectionFailure as e:
            raise Exception(f"MongoDB connection failed: {e}")
        except OperationFailure as e:
            raise Exception(f"MongoDB operation failed: {e}")

    def get_database(self, db_name):
        """
        Return a database object.
        """
        if not self.client:
            raise Exception("No active MongoDB connection. Call connect() first.")
        return self.client[db_name]

    def close(self):
        """
        Close the MongoDB client connection.
        """
        if self.client:
            self.client.close()
            logger.info("MongoDB connection closed.")