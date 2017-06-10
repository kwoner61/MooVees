from src import media
from src import fresh_tomatoes

# media.Movie( title, story_line, post_url, trailer_url )

chappie = media.Movie(
    "Chappie",
    "In the near future, crime is patrolled by a mechanized police force. "
    "When one police droid, Chappie, is stolen and given new programming, he "
    "becomes the first robot with the ability to think and feel for himself.",
    "https://images-na.ssl-images-amazon.com/images/M/"
    "MV5BMTUyNTI4NTIwNl5BMl5BanBnXkFtZTgwMjQ4MTI0NDE@."
    "_V1_SY1000_CR0,0,674,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=lyy7y0QOK-0")

interstellar = media.Movie(
    "Interstellar",
    "A team of explorers travel through a wormhole in space in an attempt "
    "to ensure humanity's survival.",
    "https://images-na.ssl-images-amazon.com/images/M/"
    "MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@."
    "_V1_SY1000_CR0,0,640,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=Lm8p5rlrSkY")

inception = media.Movie(
    "Inception",
    "A thief, who steals corporate secrets through use of dream-sharing "
    "technology, is given the inverse task of planting an idea into the "
    "mind of a CEO.",
    "https://images-na.ssl-images-amazon.com/images/M/"
    "MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@."
    "_V1_SY1000_CR0,0,675,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=8BfMivMDOBI")

walle = media.Movie(
    "WALL-E",
    "In the distant future, a small waste-collecting robot inadvertently "
    "embarks on a space journey that will ultimately decide the fate of "
    "mankind.",
    "https://images-na.ssl-images-amazon.com/images/M/"
    "MV5BMjExMTg5OTU0NF5BMl5BanBnXkFtZTcwMjMxMzMzMw@@."
    "_V1_SY1000_CR0,0,674,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=8-_9n5DtKOc")

ex_machina = media.Movie(
    "Ex Machina",
    "A young programmer is selected to participate in a ground-breaking "
    "experiment in synthetic intelligence by evaluating the human qualities"
    " of a breath-taking humanoid A.I.",
    "https://images-na.ssl-images-amazon.com/images/M/"
    "MV5BMTUxNzc0OTIxMV5BMl5BanBnXkFtZTgwNDI3NzU2NDE@."
    "_V1_SY1000_CR0,0,674,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=EoQuVnKhxaM")

martian = media.Movie(
    "The Martian",
    "An astronaut becomes stranded on Mars after his team assume him dead, "
    "and must rely on his ingenuity to find a way to signal to Earth that "
    "he is alive.",
    "https://images-na.ssl-images-amazon.com/images/M/"
    "MV5BMTc2MTQ3MDA1Nl5BMl5BanBnXkFtZTgwODA3OTI4NjE@."
    "_V1_SY1000_CR0,0,675,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=ej3ioOneTy8")

ai = media.Movie(
    "A.I. Artificial Intelligence",
    "A highly advanced robotic boy longs to become 'real' so that he can "
    "regain the love of his human mother.",
    "https://images-na.ssl-images-amazon.com/images/M/"
    "MV5BNWU2NzEyMDYtM2MyOS00OGM3LWFkNzAtMzRiNzE2ZjU5Z"
    "TljXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,"
    "666,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=_19pRsZRiz4")

gravity = media.Movie(
    "Gravity",
    "Two astronauts work together to survive after an "
    "accident which leaves them alone in space.",
    "https://images-na.ssl-images-amazon.com/images/M/"
    "MV5BNjE5MzYwMzYxMF5BMl5BanBnXkFtZTcwOTk4MTk0OQ@@."
    "_V1_SY1000_CR0,0,675,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=_KJHRF6RlTQ")

movies = [chappie, inception, interstellar, 
          walle, ex_machina, martian, ai, gravity]

fresh_tomatoes.open_movies_page(movies)
