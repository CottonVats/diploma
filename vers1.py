from urllib.parse import urlencode
import requests
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
token1 = "5e354313b78f73ef38950d096b4b462bdcd2847acfac2c4c8bd244c0d6609e48469871f1409b32bd14d6f"
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
        for id in self.friends_ids:
            friends_params = {
                "access_token":self.token,
                "user_id":id,
                "v":5.98
            }
            self.params_list.append(friends_params)
        for friend_params in self.params_list:
            response = requests.get('https://api.vk.com/method/groups.get', friend_params)
            response_text = response.json()['response']
            groups_ids_set = set(response_text['items'])
            self.sets_list.append(groups_ids_set)






im = VK_user(token1)
im.get_nonmultual_groups()
