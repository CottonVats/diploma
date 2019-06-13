import unittest

from vkinder import evaluators


class TestEvaluators(unittest.TestCase):

    def test_eval_city_match(self):
        assert evaluators.eval_city('Воронеж', 'Воронеж', 1) == 10

    def test_eval_city_mycity_not_set(self):
        assert evaluators.eval_city('Воронеж', '', 1) == 0

    def test_eval_city_different_city(self):
        assert evaluators.eval_city('Воронеж', 'Москва', 1) == 0

    def test_eval_city_mycity_dict_not_set(self):
        assert evaluators.eval_city(
            {'id': 1, 'title': 'Москва'}, None, 1) == 0

    def test_eval_city_mycity_dict(self):
        assert evaluators.eval_city(
            {'id': 1, 'title': 'Москва'},
            {'id': 2, 'title': 'Cанкт-Питербург'},
            1
        ) == 0

    def test_eval_lists_match(self):
        assert evaluators.eval_lists(["Шахматы, концерты, книги"],
                                    ['Шахматы, концерты, книги'], 1) == 1

    def test_eval_lists_mylist_not_set(self):
        assert evaluators.eval_lists(['Музыка, Книги, Disney'],
                                    [''], 1) == 0

    def test_eval_lists_not_set(self):
        assert evaluators.eval_lists([''],
                                    ['Музыка, Книги, Disney'], 1) == 0

    def test_eval_lists_different(self):
        assert evaluators.eval_lists(['Книги'],
                                    ['Музыка'], 1) == 0

if __name__ == '__main__':
    unittest.main()