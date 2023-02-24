import requests
import datetime

TINDER_URL = "https://api.gotinder.com"


class TinderAPI():
    def __init__(self, token):
        self._token = token
        self.chatroom_match_id = []

    def profile(self):
        data = requests.get(TINDER_URL + "/v2/profile?include=account%2Cuser", headers={"X-Auth-Token": self._token}).json()
        return Profile(data["data"], self)

    def matches(self, limit=10):
        data = requests.get(TINDER_URL + f"/v2/matches?count={limit}", headers={"X-Auth-Token": self._token}).json()
        self.chatroom_match_id = list(map(lambda match: match['id'], data["data"]["matches"]))
        return list(map(lambda match: Match(match, self), data["data"]["matches"]))

    def get_messages(self, match_id):
        data = requests.get(TINDER_URL + f"/v2/matches/{match_id}/messages?count=50", headers={"X-Auth-Token": self._token}).json()
        return Chatroom(data['data'], match_id, self)

    def get_user_info(self, user_id):
        data = requests.get(TINDER_URL + f"/user/{user_id}", headers={"X-Auth-Token": self._token}).json()
        return Person(data["results"], self)

    def send_message(self, match_id, from_id, to_id, message):
        body = {
            'matchId': match_id,
            'message': message,
            'userId': from_id,
            'otherId': to_id,
            'sessonId': None
        }
        data = requests.post(TINDER_URL + f'/user/matches/{match_id}', json=body, headers={"X-Auth-Token": self._token}).json()
        return data


class Chatroom(object):
    def __init__(self, data, match_id, api):
        self._api = api
        self.match_id = match_id
        self.messages = list(map(lambda message: Message(match_id, message, self), data['messages']))

    def send(self, message, from_id, to_id):
        return self._api.send_message(self.match_id, from_id, to_id, message)

    def get_lastest_message(self):
        if len(self.messages) > 0:
            return self.messages[0]
        return None


class Message(object):
    def __init__(self, match_id, data, api):
        self._api = api
        self.match_id = match_id
        self.message_id = data['_id']
        self.sent_date = data['sent_date']
        self.message = data['message']
        self.to_id = data['to']
        self.from_id = data['from']
        self.sent_date = datetime.datetime.strptime(data['sent_date'], '%Y-%m-%dT%H:%M:%S.%fZ')

    def __repr__(self):
        return f'{self.from_id}: {self.message}'


class Match(object):
    def __init__(self, data, api):
        self.match_id = data['id']
        self.person = Person(data['person'], api)


class Person(object):

    def __init__(self, data, api):
        self._api = api

        self.id = data["_id"]

        self.name = data.get("name", "Unknown")

        self.bio = data.get("bio", "")
        self.city = data.get("city", {}).get('name', "")
        self.relationship_intent = data.get("relationship_intent", {}).get('body_text', "")
        selected_descriptors = data.get('selected_descriptors', [])
        self.selected_descriptors = []
        for selected_descriptor in selected_descriptors:
            if selected_descriptor.get('prompt'):
                self.selected_descriptors.append(f"{selected_descriptor.get('prompt')} {'/'.join([s['name'] for s in selected_descriptor['choice_selections']])}")
            else:
                self.selected_descriptors.append(f"{selected_descriptor.get('name')}: {'/'.join([s['name'] for s in selected_descriptor['choice_selections']])}")

        self.distance = data.get("distance_mi", 0) / 1.60934

        self.birth_date = datetime.datetime.strptime(data["birth_date"], '%Y-%m-%dT%H:%M:%S.%fZ') if data.get(
            "birth_date", False) else None
        self.gender = ["Male", "Female", "Unknown"][data.get("gender", 2)]

        self.images = list(map(lambda photo: photo["url"], data.get("photos", [])))

        self.jobs = list(
            map(lambda job: {"title": job.get("title", {}).get("name"), "company": job.get("company", {}).get("name")}, data.get("jobs", [])))
        self.schools = list(map(lambda school: school["name"], data.get("schools", [])))

    def infos(self):
        return {
            'name': self.name,
            'bio': self.bio,
            'city': self.city,
            'relationship_intent': self.relationship_intent,
            'selected_descriptors': self.selected_descriptors,
            'birth_date': self.birth_date,
            'gender': self.gender,
            'jobs': self.jobs,
            'schools': self.schools
        }

    def __repr__(self):
        return f"{self.id}  -  {self.name} ({self.birth_date.strftime('%d.%m.%Y')})"


class Profile(Person):

    def __init__(self, data, api):

        super().__init__(data["user"], api)
        self.email = data["account"].get("email")
        self.phone_number = data["account"].get("account_phone_number")

        self.age_min = data["user"]["age_filter_min"]
        self.age_max = data["user"]["age_filter_max"]
        user_interests = data["user"].get('user_interests', {}).get('selected_interests', [])
        self.user_interests = []
        for user_interest in user_interests:
            self.user_interests.append(user_interest.get('name'))

        self.max_distance = data["user"]["distance_filter"]
        self.gender_filter = ["Male", "Female"][data["user"]["gender_filter"]]
