from typing import ClassVar, Optional
from dataclasses import dataclass
from pymongo.collection import Collection
from pymongo.database import Database as MongoDatabase
from config.database_injectable import DatabaseInjectable
    

@dataclass  
class Document():
    _id: Optional[str] = None
   
    