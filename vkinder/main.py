import json
from vkinder.params_for_search import SearchParams
from .field_adapters import donot_adapt, get_cityname, split_string
from .evaluators import eval_lists, eval_city


EVALUATORS = {
    'city': eval_city,
    'interests': eval_lists,
    'music': eval_lists,
    'books': eval_lists,
    'movies': eval_lists,
}
ADAPTERS = {
    'city': get_cityname,
    'interests': split_string,
    'music': split_string,
    'books': split_string,
    'movies': split_string,

}


def data_process(search_params: SearchParams, candidates) -> dict:
    assert isinstance(candidates, list)
    data = dict()

    for raw in candidates:
        weight = 0
        for field, evaluator in EVALUATORS.items():
            if not raw.get(field):
                continue
            if not search_params.registry.get(field):
                continue
            field_obj = search_params.registry[field]
            adapter = ADAPTERS.get(
                field, donot_adapt)

            weight += evaluator(
                adapter(raw[field]),
                field_obj.value,
                field_obj.weight,
            )

        data[raw['id']] = {'weight': weight, 'user': raw}

        filename = 'candidates.json'
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(json.dumps(data,
                               sort_keys=False,
                               indent=4,
                               ensure_ascii=False,
                               separators=(',', ': ')))

    return data


def sort_data(data):
    sort_dict = {}
    for uid, user in data.items():
        sort_dict[uid] = user['weight']

    sort_by_weight = dict(sorted(sort_dict.items(), key=lambda item: item[1], reverse=True))

    filename = 'sorted_weight.json'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(sort_by_weight,
                           sort_keys=False,
                           indent=2,
                           ensure_ascii=True,
                           separators=(',', ': ')))

    user_list = []
    for user in sort_by_weight.keys():
        user_list.append(user)
    top_10_list = user_list[0:10]

    print(top_10_list)

    return sort_by_weight
