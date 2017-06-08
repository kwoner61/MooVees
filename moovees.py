from src import media
from src import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "Avatar story line",
                     "https://resizing.flixster.com/5x1smnlGnkJxJ2x5iRnCn7t1Y2k=/\
                     206x305/v1.bTsxMTE3Njc5MjtqOzE3NDA5OzEyMDA7ODAwOzEyMDA",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY"
                     )

movies = [toy_story,toy_story,toy_story,toy_story,toy_story,toy_story]

fresh_tomatoes.open_movies_page(movies)