from models.document import Document
from dataclasses import dataclass
from typing import List

from config.database_injectable import DatabaseInjectable
from typing import List, Optional
from pymongo.collection import Collection
from config.database_injectable import DatabaseInjectable
from pymongo.results import InsertOneResult
from utils.AbstractManager import AbstractManager
from models.movie import MovieManager
from pymongo.database import Database as MongoDatabase




class Director():
    name: str = None
    
    def __init__(self, name: str):
        self.name = name
        
    @staticmethod
    def director_validator() -> dict:
        return {
            "$jsonSchema": {
                "bsonType": "object",
                "required": ["name"],
                "properties": {
                    "name": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                    }
                }
            }
        }
     
    def get_movies(self, movie_manager: MovieManager, id):
       return  movie_manager.collection.find({"director": id}).to_list()
        
    def avg_rating(self, movie_manager: MovieManager, id):
        return movie_manager.collection.aggregate([
            {"$match": {"director": id}},
            {"$group": {"_id": id, "avg": {"$avg": "$rating"}}}
        ]).to_list()




class DirectorManager(AbstractManager):
    def __init__(self, db: MongoDatabase):
        super().__init__("director", db)
        
    def get_by_name(self, name: str) -> Director:
        return self.collection.find_one({"name": name}) 
    
    