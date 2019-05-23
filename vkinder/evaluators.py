def eval_lists(one: list, another: list, cost=1):
    common = []
    for elem in one:
        if elem in another:
            common.append(elem)
    weight = cost * len(common)
    return weight


def eval_city(city, usercity, cost=10):
    match_factor = 10
    if not usercity or not city:
        return 0
    if city == usercity:
        return match_factor * cost
    return 0
