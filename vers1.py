from urllib.parse import urlencode
import requests
import json
import time
oauth_url = 'htpps://oauth.vk.com/authorize'
app_id = 6896760
auth_params = {
    'client_id': app_id,
    'display': 'page',
    'scope':['friends','groups'],
    'response_type':'token',
    'v': 5.92
}
print("?".join((oauth_url, urlencode(auth_params))))
token1 = "6cce3f3c00860bbd32b8f8271cd083184c0c092dafcd6f35d2edc26a3ffec55396301ba6f7a7999631427"
class VK_user:
    def __init__(self, token):
        self.token = token
        self.params = {'access_token':self.token,
        'v':5.98
        }
        self.response = requests.get('https://api.vk.com/method/users.get', self.params)
        self.resp = self.response.json()['response']
        self.id = self.resp[0]['id']
    def get_nonmultual_groups(self):
        self.friends =  requests.get('https://api.vk.com/method/friends.get', self.params)
        self.friends_ids = self.friends.json()['response']['items']
        self.groups = requests.get('https://api.vk.com/method/groups.get', self.params)
        self.groups_set = set(self.groups.json()['response']['items'])
        self.params_list = []
        self.sets_list = []
        self.all_group_ids_list = []
        for id in self.friends_ids:
            friends_params = {
                "access_token":self.token,
                "user_id":id,
                "v":5.98
            }
            self.params_list.append(friends_params)
        for friend_params in self.params_list:
            response = requests.get('https://api.vk.com/method/groups.get', friend_params)
            time.sleep(1)
            response_text = response.json()['response']
            groups_ids = response_text['items']
            for id in groups_ids:
                self.all_group_ids_list.append(id)
        self.friends_group_ids_set = set(self.all_group_ids_list)
        self.nonmultual_groups = self.groups_set.difference_update(self.friends_group_ids_set)
        with open('groups.json', 'w') as file:
            json.dump(self.nonmultual_groups, file)


im = VK_user(token1)
im.get_nonmultual_groups()
