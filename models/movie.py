from dataclasses import dataclass
from typing import List

from utils.AbstractManager import AbstractManager

class MovieManager(AbstractManager):
    def __init__(self, db):
        super().__init__("movie", db)
        
    def get_by_title(self, title: str):
        return self.collection.find_one({"title": title})

@dataclass
class Movie():
    title: str = None
    year: int = None
    summary: str = None
    short_summary: str = None
    imdb_id: str = None
    run_time: int = None
    youtube_trailer: str = None
    rating: float = None
    movie_poster: str = None
    director: str = None
    writers: List[str] = None
    cast: List[str] = None
    
    @staticmethod
    def movies_validator() -> dict:
        return {
            "$jsonSchema": {
                "bsonType": "object",
                "required": ["title", "year", "summary", "short_summary", "imdb_id", "run_time", "youtube_trailer", "rating", "movie_poster", "director", "writers", "cast"],
                "properties": {
                    "title": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                    },
                    "year": {
                        "bsonType": "int",
                        "description": "must be an int and is required"
                    },
                    "summary": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                    },
                    "short_summary": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                    },
                    "imdb_id": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                    },
                    "run_time": {
                        "bsonType": "int",
                        "description": "must be an integer and is required"
                    },
                    "youtube_trailer": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                    },
                    "rating": {
                        "bsonType": "double",
                        "description": "must be a double and is required"
                    },
                    "movie_poster": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                    },
                     "director": {
                        "bsonType": "objectId",  
                        "description": "must be an ObjectId and is required"
                    },
                    "writers": {
                        "bsonType": "string",
                        "description": "must be an array of strings and is required"
                    },
                    "cast": {
                        "bsonType": "array",
                        "items": {
                            "bsonType": "string"
                        },
                        "description": "must be an array of strings and is required"
                    }
                }
            }
        }
        
    