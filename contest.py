import requests
import pprint

url = "http://codeforces.com/api/"

class ContestInfo:

    def __init__(self):
        pass

    
    # Returning -1, if there is no such contest
    # Returning id of contest with the name

    def find_contest(self, name):
        a = requests.get(url + 'contest.list').json()
        print(name)
        if a['status'] != 'OK':
            return -1
        for i in a['result']:
            if name in i['name']:
                return i['id']
        return -1


    # Returning -1, if there is no such contest
    # Returning place of user in exact contest

    def place_in_contest(self, contest, handle):
        contest_info = ContestInfo()
        contest_id = contest_info.find_contest(contest)
        if contest_id == -1:
            return -1
        map_params = {
            'contestId': str(contest_id)
        }
        a = requests.get(url + 'contest.standings', params=map_params).json()
        for i in a['results']['rows']:
            party = i['party']
            for i in party['members']:
                if i['handle'] == handle:
                    return i['rank']
        return -1


    # Returning "there is no such contest", if there is no such contest
    # Returning link to contest with the title
    
    def link_to_contest(self, name):
        contest_info = ContestInfo()
        contest_id = contest_info.find_contest(name)
        if contest_id == -1:
            return "there is no such contest"
        return "https://codeforces.com/contest/" + str(contest_id)