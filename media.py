import webbrowser


# Here we created a class called Movie
class Movie ():
    """ The class provides space to store movie related information """
# the following function initialize spaces to store information about
# a movie's title, storyline, poster_image and trailer URL
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        # below we store information about movies into 4 instance variables
        # such that every instance will have corresponding information.
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
