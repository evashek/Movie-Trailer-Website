class Movie():
    """Defines movie class."""
    def __init__(self, movie_title, movie_year, star_rating,
                 movie_summary, actors_list, movie_poster, movie_trailer):
        self.title = movie_title
        self.stars = star_rating
        self.year = movie_year
        self.summary = movie_summary
        self.actors = actors_list
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer


class Actor():
    """Defines the actor class.
    Note: If an actor has appeared in more than one movie listed,
    the role variable would be an array rather than a string. This
    is not the case for this version of entertainment_center.py."""
    def __init__(self, actor_name, role_name, actor_picture):
        self.name = actor_name
        self.role = role_name
        self.picture_url = actor_picture
