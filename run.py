from vkinder.params_for_search import SearchParams, StringField, ListField
from vkinder.vk import search, MALE, get_photos
from vkinder.main import data_process, sort_data
import time


def _main():
    vk_login = ''
    vk_pw = ''
    age_min = 20
    age_max = 40

    params = SearchParams([
        StringField(name='city', value='Москва', weight=50),
        ListField(name='books', value=['Кинг'], weight=100),
        ListField(name='movies', value=['Гарри Поттер'], weight=200),
        ListField(name='interests', value=['музыка'], weight=150),
    ])

    candidates = search(
        login=vk_login,
        password=vk_pw,
        fields=list(params.registry),
        age_min=age_min,
        age_max=age_max,
        sex=MALE,
    )

    top_10_candidates = data_process(search_params=params, candidates=candidates)
    sorted_result = sort_data(top_10_candidates)
    sorted_top_10 = list(sorted_result)[0:10]

    for candidate in sorted_top_10:
        time.sleep(0.5)
        photos = get_photos(
            login=vk_login,
            password=vk_pw,
            owner_id=candidate,
        )
        photos_dict = dict()
        for photo in photos:
            likes = photo['likes']['count']
            for size in photo['sizes']:
                if size['type'] == 'x':
                    url = size['url']
            photos_dict[url] = likes
        top3_photos = sorted(photos_dict.items(), key=lambda x: x[1], reverse=True)[0:3]
        print('Топ 3 фото для кандидата', candidate, top3_photos)


if __name__ == '__main__':
    _main()
