import requests
from LOLcard import exceptions

tft_token_file = open("LOLcard/token.txt", "r", encoding="utf-8")
TFTAPIKEY = tft_token_file.read()
lol_token_file = open("LOLcard/LOLtoken.txt", "r", encoding="utf-8")
LOLAPIKEY = lol_token_file.read()
REGION = 'https://kr.api.riotgames.com'


def get_player_id(nickname):
    url = f'{REGION}/lol/summoner/v4/summoners/by-name/{nickname}'
    req = requests.get(url, {'api_key': LOLAPIKEY})

    return req.json()['id'] if 'id' in req.json() else ""


def get_tft_id(nickname):
    url = f'{REGION}/tft/summoner/v1/summoners/by-name/{nickname}'
    req = requests.get(url, {'api_key': TFTAPIKEY})

    return req.json()['id'] if 'id' in req.json() else ""


def get_player_stat(id, tftid):
    if id == "":
        raise exceptions.UserNotFoundException

    output = {}

    url = f'{REGION}/lol/league/v4/entries/by-summoner/{id}'
    req = requests.get(url, {'api_key': LOLAPIKEY, 'encryptedSummonerId': id})
    for data in req.json():
        output[data["queueType"]] = data

    if tftid == "":
        return output

    tft_url = f'{REGION}/tft/league/v1/entries/by-summoner/{tftid}'
    req = requests.get(tft_url, {'api_key': TFTAPIKEY})

    for data in req.json():
        output[data["queueType"]] = data

    return output


def tier_text(data):
    if data["tier"] in ["MASTER", "GRANDMASTER", "CHALLENGER"]:
        return data["tier"]
    return data["tier"] + " " + data["rank"]