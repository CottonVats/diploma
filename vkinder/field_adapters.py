def get_cityname(city):
    return city['title']


def split_string(string):
    parts = string.split(',')
    for i, part in enumerate(parts):
        parts[i] = part.strip()
    return parts


def donot_adapt(anything):
    return anything
