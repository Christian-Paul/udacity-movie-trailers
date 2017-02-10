import media
import fresh_tomatoes
import urllib2
import json
from urllib import quote
from pprint import pprint

TMDB_KEY = '3518f2d994fd6bbbd7456eeaa1fd396d'
movies_to_search = ['gladiator', 'the grey', 'mr. nobody',
                    'django unchained', 'apocalypse now', 'inside out']
movies = []

# iterate through each movie and get title, poster art, and video url
# create an instance of the Movie class each time and append it to the final movie array
for movie_query in movies_to_search:

    # make movie query url friendly
    qs = quote(movie_query)

    # send request for movie details and poster art
    details_request = 'https://api.themoviedb.org/3/search/movie?api_key='+TMDB_KEY+'&query='+qs
    details_response = urllib2.urlopen(details_request).read()
    parsed_details_response = json.loads(details_response)

    # get movie id, which is used to search for video url
    movie_id = parsed_details_response['results'][0]['id']

    # search for video url
    video_request = 'https://api.themoviedb.org/3/movie/'+str(movie_id)+'/videos?api_key=3518f2d994fd6bbbd7456eeaa1fd396d&language=en-US'
    video_response = urllib2.urlopen(video_request).read()
    parsed_video_response = json.loads(video_response)

    # define title, image url, and video
    title = parsed_details_response['results'][0]['title']
    image_url = 'http://image.tmdb.org/t/p/w342//' + parsed_details_response['results'][0]['poster_path']
    video_url = 'https://www.youtube.com/watch?v=' + parsed_video_response['results'][0]['key']

    # create Movie instance and append it to final movies array
    movies.append(media.Movie(title, image_url, video_url))

# use movies to create webpage
fresh_tomatoes.open_movies_page(movies)
