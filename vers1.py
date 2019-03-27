from urllib.parse import urlencode
import requests
import json
import time
oauth_url = 'htpps://oauth.vk.com/authorize'
app_id = 6896760
auth_params = {
    'client_id': app_id,
    'display': 'page',
    'scope': ['friends', 'groups'],
    'response_type': 'token',
    'v': 5.92
}
print("?".join((oauth_url, urlencode(auth_params))))
token1 = "821d8ff0443b81f2e4ac06c63aec707e53126f151e9001db3bfe30bebb7668762b74237dec3aa33c28980"
class VK_user:
    def __init__(self, token):
        self.params_list = []
        self.all_groups_list = []
        self.friends_groups_ids =[]
        self.token = token
        self.params = {'access_token':self.token,
        'v':5.98
        }
        self.response = requests.get('https://api.vk.com/method/users.get', self.params)
        self.resp = self.response.json()['response']
        self.id = self.resp[0]['id']
    def get_nonmultual_groups(self, givenid):
        self.group_dict_list = []
        self.new_params ={
            'access_token': self.token,
            'v': 5.98,
            'id': givenid}
        self.friends = requests.get('https://api.vk.com/method/friends.get', self.new_params)
        self.friends_ids = self.friends.json()['response']['items']
        self.groups = requests.get('https://api.vk.com/method/groups.get', self.new_params)
        self.groupsid_set = set(self.groups.json()['response']['items'])
        self.nonmultual_groups_list = []
        self.new_params1 = {
            'access_token': self.token,
            'v': 5.98,
            'id': givenid,
            'extended': 1,
            'fields': 'members_count'}
        self.groups_dicts = requests.get('https://api.vk.com/method/groups.get', self.new_params1)
        self.all_groups = self.groups_dicts.json()['response']['items']
        for group in self.all_groups:
            print(group)
            group_dict = {'gid': group['id'],
                          'name': group['name'],
                          'members_count': group['members_count']
                          }
            self.group_dict_list.append(group_dict)
        for id in self.friends_ids:
            friends_params = {
                "access_token": self.token,
                "user_id": id,
                "v": 5.98,
            }
            self.params_list.append(friends_params)
        for friend_params in self.params_list:
            response = requests.get('https://api.vk.com/method/groups.get', friend_params)
            time.sleep(1)
            response_text = response.json()['response']
            groups = response_text['items']
            for group in groups:
                self.friends_groups_ids.append(group)
        self.friends_groups_set = set(self.friends_groups_ids)
        self.nonmultual_groups = self.groupsid_set.difference_update(self.friends_groups_set)
        for group_dict in self.group_dict_list:
            if group_dict['gid'] in self.nonmultual_groups:
                self.nonmultual_groups_list.append(group_dict)
        with open('groups.json', 'w') as file:
            json.dump(self.nonmultual_groups_list, file)


im = VK_user(token1)
im.get_nonmultual_groups(467929995)
