from models.movie import Movie
from datetime import datetime
from models.director import Director
from config.database_injectable import DatabaseInjectable
from models.director import DirectorManager
from models.movie import MovieManager

class CsvParser(DatabaseInjectable):
    
    movie_manager: MovieManager = None
    director_manager: DirectorManager = None
    
    @classmethod
    def set_Manager(cls, movie_manager: MovieManager, dir_manager: DirectorManager):
        cls.movie_manager = movie_manager 
        cls.director_manager = dir_manager

    @staticmethod
    def process_line(line):
        director = line[9]
        director_id = CsvParser.process_director(director)
        print(f"Director ID: {director_id}")
        CsvParser.process_movie(line, director_id)
        
    @staticmethod
    def process_director(director_str) -> Director:
        print(f"Processing director: {director_str}")
        director = Director(director_str)
        
        existing_dir = CsvParser.director_manager.get_by_name(director.name)
        if existing_dir is None:
            return CsvParser.director_manager.save(director).inserted_id
            
        return existing_dir["_id"]
            
        
    @staticmethod
    def process_movie(line, director_id: str):
        cast_list_str: str = line[11]
        cast_list = cast_list_str.split("|") 
        movie = Movie(
            title=line[0],
            year=int(line[1]),
            summary=line[2],
            short_summary=line[3],
            imdb_id=line[4],
            run_time=int(line[5]),
            youtube_trailer=line[6],
            rating=float(line[7]),
            movie_poster=line[8],
            director=director_id,
            writers=line[10],
            cast=cast_list
        )
        
        if CsvParser.movie_manager.get_by_title(movie.title) is None:
            CsvParser.movie_manager.save(movie)
        
        
        
        
    @staticmethod
    def log_error(error):   
        try:
            with open('logs/error.log', 'a') as file:
                file.write(f"{datetime.now()} - {error}\n")
        except Exception as e:
            print(f"Failed to log error: {e}")