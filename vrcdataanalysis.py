import requests as requests
import json
import pprint

def prediction(red1, red2, blue1, blue2)
    request_url = "https://vrc-data-analysis.com/v1/predict/{}/{}/{}/{}".format(red1, red2, blue1, blue2)
    r = requests.get(request_url)
    return r.json()

