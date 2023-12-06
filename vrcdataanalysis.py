import requests as requests
import json
import pprint

def prediction(red1, red2, blue1, blue2):
    request_url = "https://vrc-data-analysis.com/v1/predict/{}/{}/{}/{}".format(red1, red2, blue1, blue2)
    r = requests.get(request_url)
    return r.json()

#def team_trueskill_rank(team):
    #request_url = "https://vrc-data-analysis.com/v1/team/" + team
    #r = requests.get(request_url)
    #data = r.json()

    #return data['trueskill_ranking']

#def team_trueskill_value(team):
    #request_url = "https://vrc-data-analysis.com/v1/team/" + team
    #r = requests.get(request_url)
    #data = r.json()

    #return data['trueskill']