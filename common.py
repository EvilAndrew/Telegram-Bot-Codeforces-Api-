import requests

url = "http://codeforces.com/api/"

class CommonInfo:

    def __init__(self):
        pass


    # Returning color and name of the rating
    # We suppose that if rating is below 0, it's grey newbie

    def what_color_is_number(self, n):
        num = int(n)
        if num < 1200:
            return 'Grey newbie'
        if 1200 <= num < 1400:
            return 'Green pupil'
        if 1400 <= num < 1600:
            return 'Cyan specialist'
        if 1600 <= num < 1900:
            return 'Blue expert'
        if 1900 <= num < 2100:
            return 'Purple candidate master'
        if 2100 <= num < 2300:
            return 'Yellow master'
        if 2300 <= num < 2400:
            return 'Orange international master'
        if 2400 <= num < 2600:
            return 'Red grandmaster'
        if 2600 <= num < 3000:
            return 'Red international grandmaster'
        if 3000 <= num:
            return 'Black-and-red legendary grandmaster'

    # Returning 0 if there is no such tag
    # Returning number of problems with the tag, or totally, if there is no tag given

    def how_many_problems_at_all(self, tag=None):
        if tag is None:
            a = requests.get(url + 'problemset.problems').json()
            return len(a['result']['problems'])
        map_params = {
            'tags': tag
        }
        a = requests.get(url + 'problemset.problems', params=map_params).json()
        if a['status'] != 'OK':
            return 0
        return len(a['result']['problems'])


    # Returning -1, if there is no such problem
    # Returning link to the problem by its name or code+letter

    def link_to_problem(self, name):
        a = requests.get(url + 'problemset.problems').json()
        if a['status'] != 'OK':
            return -1
        for i in a['result']['problems']:
            if i['name'] == name or str(i['contestId']) + str(i['index']) == name:
                return "https://codeforces.com/problemset/problem/" + str(i['contestId']) + "/" + str(i['index'])
        return "there is no such link"
            