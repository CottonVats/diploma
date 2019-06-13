from vkinder.params_for_search import SearchParams, StringField, ListField
from vkinder.vk import search, get_photos, get_user_info, TOKEN
from vkinder.main import data_process, sort_data
import time

if __name__ == '__main__':
    params = get_user_info()
    user_city = params[0]
    user_books = params[1]
    user_movies = params[2]
    user_interests = params[3]
    needed_sex = params[4]


def _main():
    age_min = int(input("Минимальный возраст: "))
    age_max = int(input("Максимальный возраст: "))
    city_weight = int(input("Вес (число от 0 до 10) совпадения по городу: "))
    books_weight = int(input("Вес (число от 0 до 10) совпадения по любимым книгам: "))
    movies_weight = int(input("Вес (число от 0 до 10) совпадения по любимым фильмам: "))
    interests_weight = int(input("Вес (число от 0 до 10) совпадения по интересам: "))
    params = SearchParams([
        StringField(name='city', value=user_city, weight=city_weight),
        ListField(name='books', value=user_books, weight=books_weight),
        ListField(name='movies', value=user_movies, weight=movies_weight),
        ListField(name='interests', value=user_interests, weight=interests_weight),
    ])

    candidates = search(
        fields=list(params.registry),
        age_min=age_min,
        age_max=age_max,
        sex=needed_sex,
    )

    top_10_candidates = data_process(search_params=params, candidates=candidates)
    sorted_result = sort_data(top_10_candidates)
    sorted_top_10 = list(sorted_result)[0:10]

    for candidate in sorted_top_10:
        time.sleep(0.3)
        photos = get_photos(
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
