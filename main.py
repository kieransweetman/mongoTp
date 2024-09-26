from config.database import Database
import csv
import json
from utils.csv_parser import CsvParser
from models.movie import MovieManager
from models.director import DirectorManager
from models.director import Director
from aggregates.pipelines import pipeline_longest_movies_directors, pipeline_most_movies_directors, pipeline_top_actors, pipeline_top_rated_directors 

def main():
    # db init
    db_instance = Database()
    db_instance.connect()
    db = db_instance.get_db()
    
    dir_manager = DirectorManager(db)
    movie_manager = MovieManager(db)
    
    # inject db as dependency
    CsvParser.inject_db(db)  # Inject the database into CsvParser
    CsvParser.set_Manager(movie_manager, dir_manager)  # Inject the MovieManager into CsvParser
    
    
    ############
    # TP #######
    ############
    
    try:
       with open('data/movies.csv', 'r') as file:
           reader = csv.reader(file)
           
           # skip header
           next(reader)
           
           # process lines in csv
           for line in reader:
                print("\n")
                CsvParser.process_line(line)

    except Exception as e:
       CsvParser.log_error(e)
       
    model = dir_manager.get_by_name("Wes Ball")
    d: Director = Director(model['name'])
    print(f"{d.name}: {d.get_movies(movie_manager, model['_id'])}")
    print("avg: ", d.avg_rating(movie_manager, model['_id']))
    print("####\n####")
    
    ## Aggregate results are writtin in the `./aggregates/results.json`##
    
    results = {
        "top_rated_directors": dir_manager.collection.aggregate(pipeline_top_rated_directors).to_list(),
        "longest_movies_directors": dir_manager.collection.aggregate(pipeline_longest_movies_directors).to_list(),
        "most_movies_directors": dir_manager.collection.aggregate(pipeline_most_movies_directors).to_list(),
        "top_actors": movie_manager.collection.aggregate(pipeline_top_actors).to_list()
    }
    
    for key in results:
        for document in results[key]:
            if '_id' in document:
                del document['_id']
    
    with open('aggregates/results.json', 'w') as file:
        json.dump(results, file, indent=4)
    
    

    
    ## end aggregates ##
    
    
    ############
    # End TP ###
    ############
    
    # reset db and close connection
    print('resetting db')  

    # db_instance.close()

if __name__ == '__main__':
    main()