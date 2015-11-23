import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
            height: 450px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }

        .more-info {
            position: absolute;
            height: 100%;
            width: 100%;
            overflow-y: auto;
            top: 0;
            left: 0;
            text-align: left;
            padding: 20px;
            background-color: #EEE;
        }

        .more-info > img {
            float: right;
            position: relative;
            margin: 0 0 7px 7px;
        }

        .actors {
            margin: 15px 10px 5px 10px;
        }

        .actors .actor:not(:last-child) {
            margin-bottom: 5px;
        }

        .actor-pic {
            float: left;
        }

        .actor-pic img {
            display: block;
            margin-right: 10px;
        }

        .actor-role p:nth-of-type(1) {
            padding-top: 2px;
            margin-bottom: 0;
        }

        .actor-role p:nth-of-type(2) {
            font-style: italic;
            padding: 0 0 2px 50px;
            margin-bottom: 0;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });

          // hide the movie details
          $('.more-info').hide();

          $('.movie-tile').hover(
          function() {
            // show movie details of current tile
            $(this).children('.more-info').fadeIn();
          },
          function() {
            // hide details of current tile
            $(this).children('.more-info').fadeOut();
          });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Fresh Tomatoes Movie Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
        <div class="panel panel-default">
            <div class="panel-heading">
                <h3 class="panel-title">Welcome to Fresh Tomatoes!</h3>
            </div>
            <div class="panel-body">
                Hover over the movie panels to see more information about the movie.  The watch the trailer, click anywhere in the shaded area!
            </div>
        </div>
        {movie_tiles}
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
    <h2>{movie_title}</h2>
    <div class="more-info">
        <img src="{poster_image_url}" height="100">
        <h2 style="margin-top:5px">{movie_title} ({movie_year})</h2>
        <p><span style="background-color:#ffd700;padding:5px 10px;margin-right:5px">IMDB</span> {star_rating}</p>
        <p style="margin: 15px 0">{synopsis}</p>
        <div class="actors">{actors}</div>
    </div>
</div>
'''


# A single actor and role html template
movie_tile_actors_content = '''
<div class="actor">
    <div class="actor-pic"><img src="{actor_pic}" width="32" height="44"></div>
    <div class="actor-role"><p>{name}</p><p>as {character}</p></div>
</div>
'''


# Assembles all the formatted movie tiles
def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Create the formatted list of actors for current movie
        actors_content = create_actors_list(movie.actors)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            movie_year=movie.year,
            star_rating=movie.stars,
            synopsis=movie.summary,
            actors=actors_content,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


# Assembles a formatted list of actors, their pictures, and role for
# the respective movie
def create_actors_list(actors):
    actors_list = ''
    for actor in actors:
        actors_list += movie_tile_actors_content.format(
            actor_pic=actor.picture_url,
            name=actor.name,
            character=actor.role
        )
    return actors_list


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
