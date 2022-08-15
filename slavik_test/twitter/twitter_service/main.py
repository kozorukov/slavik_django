import re

from twython import Twython
from typing import List

from twitter.twitter_service.models.twitter_user import TwitterUser

APP_KEY = 'J7oizhk4hRPxbCfgxbbrwe7FC'
APP_SECRET = 'S8WJtYPW2jwsAXba5NZOHR4s96VfhppD2F0VpuH6VF9SDuwOrS'


def get_twitters_information(str_twitters) -> List[TwitterUser]:
    usernames = re.findall('.com/(.+?)\n', str_twitters)
    return [get_user_information(x) for x in usernames]


def get_user_information(username: str) -> TwitterUser:
    twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
    ACCESS_TOKEN = twitter.obtain_access_token()

    twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

    user_info = twitter.show_user(screen_name=username)

    return TwitterUser(
        user_info['followers_count'],
        user_info['friends_count'],
        user_info['description'],
        user_info['screen_name']
    )
