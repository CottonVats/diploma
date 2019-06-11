import vk
import json
from vkinder.field_adapters import get_cityname, split_string

APP_ID = 6994905
VERSION = 5.95
FEMALE = 1
MALE = 2
with open('token.json', 'r') as tokenfile:
    TOKEN = json.load(tokenfile)['token']


def get_user_info():
    session = vk.Session(access_token=TOKEN)
    vkapi = vk.API(session)
    info = vkapi.users.get(fields='city, books, movies, interests, sex', v=VERSION)[0]
    user_city = get_cityname(info['city'])
    user_books = split_string(info['books'])
    user_movies = split_string(info['movies'])
    user_interests = split_string(info['interests'])
    if info['sex'] == FEMALE:
        needed_sex = MALE
    elif info['sex'] == MALE:
        needed_sex = FEMALE
    return user_city, user_books, user_movies, user_interests, needed_sex




def search(fields, age_min, age_max, sex) -> list:
    session = vk.Session(access_token=TOKEN)

    vkapi = vk.API(session)

    return vkapi.users.search(
        v=VERSION,
        count=1000,
        sex=sex,
        age_from=age_min,
        fields=','.join(fields),
        age_to=age_max,
    )['items']


def get_photos(owner_id) -> list:
    session = vk.Session(access_token=TOKEN)

    vkapi = vk.API(session)

    photos_response = vkapi.photos.get(
        v=VERSION,
        count=1000,
        album_id='profile',
        extended=1,
        owner_id=owner_id,
    )['items']

    return photos_response
