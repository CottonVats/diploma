class BaseField:
    mytype = str

    def __init__(self, name, value, weight=1):
        self.check_type_name(name)
        self.check_type_value(value)
        self.check_type_weight(weight)

        self.name = name
        self.value = value
        self.weight = weight

    @staticmethod
    def check_type_name(name):
        if isinstance(name, str):
            return name
        raise TypeError('name must be an instance of string')

    @staticmethod
    def check_type_weight(weight):
        if isinstance(weight, int):
            return weight
        raise TypeError('Weight must be an integer')

    def check_type_value(self, value):
        if isinstance(value, self.mytype):
            return value
        raise TypeError('value must be an instance of %s' % type(self.mytype))


class StringField(BaseField):
    mytype = str


class ListField(BaseField):
    mytype = list


class SearchParams:
    def __init__(self, fields):
        self.registry = dict()
        for field in fields:
            self.registry[field.name] = field
