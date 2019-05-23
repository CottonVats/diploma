import vk


APP_ID = 6994905
VERSION = 5.95
FEMALE = 1
MALE = 2
TOKEN = "4bbe1f18729bbc853fd9704833d791e0cb5278d0bdbbaa71aee37cf7edc1c4a1ecb28d2ec0f1e0479df0a"


def search(login, password, fields, age_min, age_max, sex) -> list:
    session = vk.AuthSession(app_id=APP_ID,
                             user_login=login,
                             user_password=password
                             )

    vkapi = vk.API(session)

    return vkapi.users.search(
        v=VERSION,
        count=1000,
        sex=sex,
        age_from=age_min,
        fields=','.join(fields),
        age_to=age_max,
        access_token=TOKEN
    )['items']


def get_photos(login, password, owner_id) -> list:
    session = vk.AuthSession(app_id=APP_ID,
                             user_login=login,
                             user_password=password,
                             access_token=TOKEN
                             )

    vkapi = vk.API(session)

    photos_response = vkapi.photos.get(
        v=VERSION,
        count=1000,
        album_id='profile',
        extended=1,
        owner_id=owner_id,
        access_token=TOKEN
    )['items']

    return photos_response
