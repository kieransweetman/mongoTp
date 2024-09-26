pipeline_top_rated_directors = [
    {
        "$lookup": {
            "from": "movie",
            "localField": "_id",
            "foreignField": "director",
            "as": "movies"
        }
    },
    {
        "$unwind": "$movies"
    },
    {
        "$group": {
            "_id": "$_id",
            "name": { "$first": "$name" },
            "average_rating": { "$avg": "$movies.rating" },
        }
    },
    {
        "$sort": { "average_rating": -1 }
    },
    {
        "$limit": 5
    }
]

pipeline_longest_movies_directors = [
    {
        "$lookup": {
            "from": "movie",
            "localField": "_id",
            "foreignField": "director",
            "as": "movies"
    }
    },
    {
        "$unwind": "$movies"
    },
    {
        "$group": {
            "_id": "$_id",
            "name": { "$first": "$name" },
            "average_duration": { "$avg": "$movies.run_time" }
        }
    },
    {
        "$sort": { "average_duration": -1 }
    },
    {
        "$limit": 5
    }
]


pipeline_most_movies_directors = [
    {
        "$lookup": {
            "from": "movie",
            "localField": "_id",
            "foreignField": "director",
            "as": "movies"
        }
    },
    {
        "$unwind": "$movies"
    },
    {
        "$group": {
            "_id": "$_id",
            "name": { "$first": "$name" },
            "movie_count": { "$sum": 1 }
        }
    },
    {
        "$sort": { "movie_count": -1 }
    },
    {
        "$limit": 5
    }
]


pipeline_top_actors = [
    {
        "$unwind": "$cast"
    },
     {
        "$group": {
            "_id": "$cast",
            "movie_count": { "$sum": 1 },
            "movies": { "$push": "$title" }
        }
    },
    {
        "$sort": { "movie_count": -1 }
    },
    {
        "$limit": 5
    }
]

