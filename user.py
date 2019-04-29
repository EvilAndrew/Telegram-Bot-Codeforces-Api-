import requests
from contest import ContestInfo
from common import CommonInfo


url = "http://codeforces.com/api/"


class UserInfo:
    
    def __init__(self):
        pass


    # Returning (-1, ''), if there is no such user
    # Returning user's current rating and his/her avatar

    def find_handle(self, handle):
        map_params = {
            'handles': handle
        }
        a = requests.get(url + 'user.info', params=map_params).json()
        if a['status'] != 'OK':
            return (-1, '')
        rate = a['result'][0]['rating']
        photo_url = a['result'][0]['titlePhoto']
    
        return (rate, photo_url)


    # Returning -1, if there is no such user
    # Returning user's current rank

    def get_rank(self, handle):
        map_params = {
            'handles': handle
        }
        a = requests.get(url + 'user.info', params=map_params).json()
        if a['status'] != 'OK':
            return -1
        rank = a['result'][0]['rank']    
        return rank


    # Returning 'error', if there is no such user
    # Returning user's current color

    def what_color_is_user(self, handle):
        common_info = CommonInfo()
        map_params = {
            'handles': handle
        }    
        a = requests.get(url + 'user.info', params=map_params).json()
        if a['status'] != 'OK':
            return 'error'
        rate = a['result'][0]['rating']
        return common_info.what_color_is_number(rate)


    # Returning -1, if there is no such user
    # Returning user's current number of friends

    def how_many_friend(self, handle):
        map_params = {
            'handle': handle
        }
        a = requests.get(url + 'user.info', params=map_params).json()
        if a['status'] != 'OK':
            return -1
        return a['result'][0]['friendOfCount']


    # Returning -1, if there is no such user
    # Returning user's maximum rating

    def max_rating_of_user(self, handle):
        map_params = {
            'handles': handle
        }
        a = requests.get(url + 'user.info', params=map_params).json()
        if a['status'] != 'OK':
            return -1
        return a['result'][0]['maxRating']

    
    # Returning -1 if there is no such handle
    # Returning user's maximum rank

    def max_rank_of_user(self, handle):
        map_params = {
            'handles': handle
        }
        a = requests.get(url + 'user.info', params=map_params).json()
        if a['status'] != 'OK':
            return -1
        return a['result'][0]['maxRank']


    # Returning 'error' if there is no such problem or no such handle
    # Returning whether user has solved exact problem by its name or CONTEST_ID + LETTER_IN_CONTEST (for example 533C or 1234D)

    def is_solved(self, handle, problem):
        map_params = {
            'handle': handle
        }
        a = requests.get(url + 'user.status', params=map_params).json()
        if a['status'] != 'OK':
            return 'error'
        for i in a['result']: 
            try:
                if str(i['problem']['contestId']) + str(i['problem']['index']) == problem or i['problem']['name'] == problem:
                    if i['verdict'] == 'OK':
                        return 'solved'
            except:
                pass
        return 'not solved'

    
    # Returning -1, if there is no such contest or no such handle
    # Returning whether user has solved exact problem by its name or CONTEST_ID + LETTER_IN_CONTEST (for example 533C or 1234D)

    def place_in_contest(self, contest, handle):
        contest_info = ContestInfo()
        contest_id = contest_info.find_contest(contest)
        if contest_id == -1:
            return -1
        map_params = {
            'contestId': str(contest_id)
        }
        a = requests.get(url + 'contest.standings', params=map_params).json()
        for i in a['result']['rows']:
            party = i['party']
            for j in party['members']:
                if j['handle'] == handle:
                    return i['rank']
        return -1


    # Returning link to user by its handle, if the user exists

    def link_to_user(self, handle):
        user_info = UserInfo()
        exist = user_info.find_handle(handle)
        if exist[0] == -1:
            return "there is no such handle"
        return "https://codeforces.com/profile/" + handle