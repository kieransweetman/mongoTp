from typing import Optional
from pymongo.collection import Collection
from config.database_injectable import DatabaseInjectable
from pymongo.results import InsertOneResult


class AbstractManager(DatabaseInjectable):
    
    collection: Optional[Collection] = None

    def __init__(self, name: str, db):
        AbstractManager.inject_db(db)
        self.collection = self.db[name]

    
    def get_by_id(self, id):
        return self.collection.find_one({"_id": id})
    
    def save(self, entry) -> InsertOneResult:
        return self.collection.insert_one(entry.__dict__)
