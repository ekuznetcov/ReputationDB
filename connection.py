from pymongo import MongoClient
from typing import Optional, Mapping

class MongoDB(object):
    def __init__(self, host: str = 'localhost', 
                 port: int = 27017,
                 db_name:str = None,
                 collection: str = None):
        self._client = MongoClient(f'mongodb://{host}:{port}')
        self._collection = self._client[db_name][collection]
        
        