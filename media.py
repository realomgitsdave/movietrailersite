import webbrowser


class Movie():

    def __init__(self, title, storyline, poster_url, trailer_url):

        """ Initialize a movie object
        Args:
        title = title of the movie
        storyline = brief summary of the movie
        poster_url = url to movie's poster image
        trailer_url = url to movie's trailer on YouTube
        """
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_url
        self.trailer_youtube_url = trailer_url

    def show_trailer(self):
        """ Open YouTube trailer in web browser """
        webbrowser.open(self.trailer_url)
