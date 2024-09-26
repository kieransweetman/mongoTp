from typing import Optional, ClassVar
from pymongo.database import Database as MongoDatabase


class DatabaseInjectable:
    _db: ClassVar[Optional[MongoDatabase]] = None

    @classmethod
    def inject_db(cls, db):
        cls._db = db
    
    @property
    def db(cls):
        return cls._db
   