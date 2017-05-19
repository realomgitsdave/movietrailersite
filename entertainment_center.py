import media
import fresh_tomatoes

# Instantiate a media.Movie object for each movie
# Declare title, storyline, poster image, and trailer url for each movie

super_troopers = media.Movie("Super Troopers",
                        "Five Vermont state troopers, avid pranksters with a knack for screwing up,"
                        " try to save their jobs and out-do the local police department by solving a crime.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BYzAyOTZjZDItZjNiYy00YTA3LWEyYWMtZTA0NmUzYjZhNjg0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg",
                        "https://www.youtube.com/watch?v=MPhWl_S8ies")

unforgiven = media.Movie("Unforgiven",
                        "Retired Old West gunslinger William Munny reluctantly"
                        " takes on one last job, with the help of his old partner and a young man.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BODM3YWY4NmQtN2Y3Ni00OTg0LWFhZGQtZWE3ZWY4MTJlOWU4XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,665,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=ftTX4FoBWlE")
#unforgiven.show_trailer()

dirty_rotten_scoundrels = media.Movie("Dirty Rotten Scoundrels",
                                    "Two con men try to settle their rivalry by betting on who"
                                    " can swindle a young American heiress out of $50,000 first.",
                                    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYyNDk2NDE0OV5BMl5BanBnXkFtZTcwNjQ0NzQzNA@@._V1_SY1000_CR0,0,666,1000_AL_.jpg",
                                    "https://www.youtube.com/watch?v=0ke-v0e3Cd4")

the_matrix = media.Movie("The Matrix",
                        "A computer hacker learns from mysterious rebels about the true nature"
                        " of his reality and his role in the war against its controllers.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,665,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=m8e-FF8MsqU")

i_love_you_man = media.Movie("I Love You, Man",
                            "Friendless Peter Klaven goes on a series of man-dates to find a Best Man for his wedding."
                            " But, when his insta-bond with his new B.F.F. puts a strain on his relationship"
                            " with his fiancée, can the trio learn to live happily ever after?",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BMTU4MjI5NTEyNV5BMl5BanBnXkFtZTcwNjQ1NTMzMg@@._V1_.jpg",
                            "https://www.youtube.com/watch?v=um5DuTLzw-I")

office_space = media.Movie("Office Space",
                            "Three company workers who hate their jobs decide to rebel against their greedy boss.",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BOTA5MzQ3MzI1NV5BMl5BanBnXkFtZTgwNTcxNTYxMTE@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                            "https://www.youtube.com/watch?v=dMIrlP61Z9s")

# Add all movies to the movies list
movies = [dirty_rotten_scoundrels, i_love_you_man, the_matrix, office_space, super_troopers, unforgiven]

# Pass the movies list to fresh_tomatoes.py to render the web page
fresh_tomatoes.open_movies_page(movies)