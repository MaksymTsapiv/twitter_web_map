"""twitter web map"""

import pprint
import codecs
import tweepy
import folium
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from fastapi import FastAPI

auth = tweepy.OAuthHandler("IEbNhizj7mgN1VJsdZOhJTHmx", "NXp7UqqY0dJxyIhb1tQNdlYp0Q9NE7nWe9LOWWVXczoCSGKS6z")
auth.set_access_token("1362066443970445313-PbZn509eMRsHvI9tmQqmVdhKz0Eflq", "cqZRhpZRLgbW86GmQ95WZvndoGKHxhi9SGZGZkHuJ1yI9")
api = tweepy.API(auth)

# def input_keys():
#     # consumer_key = 'IEbNhizj7mgN1VJsdZOhJTHmx'#input("Consumer_key: ")
#     # consumer_secret = 'NXp7UqqY0dJxyIhb1tQNdlYp0Q9NE7nWe9LOWWVXczoCSGKS6z'#input("Consumer_secret: ")
#     # access_token = '1362066443970445313-PbZn509eMRsHvI9tmQqmVdhKz0Eflq'#input("Access_token: ")
#     # access_token_secret = 'cqZRhpZRLgbW86GmQ95WZvndoGKHxhi9SGZGZkHuJ1yI9'#input("Access_token_secret: ")
#     name = 'elonmusk'#input("Name: ")
#     return consumer_key, consumer_secret, access_token, access_token_secret, name


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
    map.save('templates/index.html')
    return map

def main():
    """

    :return:
    """
    name = ''
    locations = list(friends_coordinates(friends_name_loc(name)))
    map_generator(locations)





if __name__ == '__main__':
    main()
    # inp = input_keys()
    # print(friend_names(inp[:-1], inp[-1]))
    # print(friends_id(inp[:-1], inp[-1]))
    # print(friend_location(inp[:-1], 44196397))
    # print(list(friends_coordinates(map(lambda x: x[0], friends_name_loc('elonmusk')))))