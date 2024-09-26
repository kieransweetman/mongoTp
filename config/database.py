from pymongo import MongoClient 
from typing import Optional
from pymongo.database import Database as MongoDatabase
from models.movie import Movie
from models.director import Director


class Database:
    instance: Optional['Database'] = None
    connection: Optional[MongoClient] = None
    db: Optional[MongoDatabase] = None
    
    def __new__(cls) -> 'Database':
        if not cls.instance:
            cls.instance = super(Database, cls).__new__(cls)
        return cls.instance
    
    def __init__(self) -> None:
        if self.connection is None:
            self.connect()
            self.run_initialization_script()
            
    def run_initialization_script(self) -> None:
        
        if self.db.list_collection_names() == []:
            print("Running initialization script...")
            self.db.create_collection('movie', validator=Movie.movies_validator())
            self.db.create_collection('director', validator=Director.director_validator())
            
        
        print("Db already initialized")

    
    def connect(self) -> None:
        try:
            self.connection = MongoClient('localhost', 27017)
            self.db = self.connection['cinema_SWETMAN_kieran']
        except Exception:
            print('Connection error, ' + Exception)
            
       
    def get_db(self) -> Optional[MongoDatabase]:
        return self.db
    
    def close(self) -> None:
        self.db.drop_collection('movie')
        self.db.drop_collection('director')
        self.connection.close()

        
       