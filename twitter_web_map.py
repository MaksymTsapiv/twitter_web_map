"""twitter web map"""

from os import path
import tweepy
import folium
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from keys import KEY1, KEY2, KEY3, KEY4

auth = tweepy.OAuthHandler(KEY1, KEY2)
auth.set_access_token(KEY3, KEY4)
api = tweepy.API(auth)

def friends_name_loc(name):
    """

    :param keys:
    :return:
    """

    return [(friend.name, friend.location) for friend in api.friends(name)]

def friends_coordinates(user):
    """

    :param location:
    :return:
    """
    geolocator = Nominatim(user_agent="twitter_web_map")
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
    for loc in user:
        location = geolocator.geocode(loc[1])
        if location:
            yield loc[0], (location.latitude, location.longitude)



def map_generator(locations):
    """

    :return:
    """
    map = folium.Map(location=[0, 0], zoom_start=3, tiles="Stamen Terrain")
    for name, coord in locations:
        folium.Marker([coord[0], coord[1]], popup=name).add_to(map)
    map.save(path.join("templates", "index.html"))
    return map

def main(name):
    """

    :return:
    """
    # name = ''
    locations = list(friends_coordinates(friends_name_loc(name)))
    map_generator(locations)