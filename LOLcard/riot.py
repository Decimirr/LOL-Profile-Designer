import requests
from LOLcard import errors

token_file = open("LOLcard/token.txt", "r", encoding="utf-8")
APIKEY = token_file.read()
REGION = 'https://kr.api.riotgames.com'


def get_player_id(nickname):
    print(APIKEY)
    url1 = f'{REGION}/lol/summoner/v4/summoners/by-name/{nickname}'
    req = requests.get(url1, {'api_key': APIKEY})

    if req.status_code != 200:
        errormsg = errors.ERRORMSG[req.status_code]
        if errormsg:
            print(errormsg)
            raise Exception
    return req.json()


def get_player_stat(id):
    url = f'{REGION}/lol/league/v4/entries/by-summoner/{id}'
    req = requests.get(url, {'api_key': APIKEY, 'encryptedSummonerId': id})

    return req.json()


def tier_text(data):
    if data["tier"] in ["MASTER", "GRANDMASTER", "CHALLENGER"]:
        return data["tier"]
    return data["tier"] + " " + data["rank"]