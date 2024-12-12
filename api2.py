import requests
import api_key

Zokon_puuid = 'DbjcFQpoiF_-F6FriNwcW2eLOMUwvpatv2if1W3JnEq3DZiYfylB9bzpzTuTVSIXHndatE0ag7Ecow'

def Find_info_about_zokon(game_id):
    Zokon_and_opponent_id = {'Zokon':None,'Zokon_opponent':None}
    Zokon_and_opponent_champ = {'Zokon':None,'Zokon_opponent':None}
    Zokon_lane = None
    zokon_team_id = None
    game = requests.get(f'https://europe.api.riotgames.com/lol/match/v5/matches/{game_id}?api_key={api_key.api_key}').json()
    def Zokon_id_ingame():
        nonlocal Zokon_lane, zokon_team_id
        if game['info']['gameMode'] != 'ARAM':
            for i in range(10):
                if game['info']['participants'][i]['puuid'] == Zokon_puuid:
                    Zokon_and_opponent_id['Zokon'] = i
                    Zokon_lane = game['info']['participants'][i]['individualPosition']
                    zokon_team_id = game['info']['participants'][i]['teamId']
                    break
            for i in range(10):
                if game['info']['participants'][i]['individualPosition'] == Zokon_lane and zokon_team_id != game['info']['participants'][i]['teamId']:
                    Zokon_and_opponent_id['Zokon_opponent'] = i
                    Zokon_and_opponent_champ['Zokon'] = game['info']['participants'][Zokon_and_opponent_id['Zokon']]['championName']
                    Zokon_and_opponent_champ['Zokon_opponent'] = game['info']['participants'][Zokon_and_opponent_id['Zokon_opponent']]['championName']
                    break
    Zokon_id_ingame()
    if Zokon_and_opponent_id['Zokon'] is not None:
        return Zokon_and_opponent_id, Zokon_and_opponent_champ
def Zokon_bully():
    number_of_matches = 10
    try:
        games = requests.get(f'https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{Zokon_puuid}/ids?start=0&count={number_of_matches}&api_key={api_key.api_key}').json()
        print(games)
        
        lst_zokon_and_lane_opponent = []
        for i in range(number_of_matches):
            if Find_info_about_zokon(games[i]) is not None: 
                lst_zokon_and_lane_opponent.append(Find_info_about_zokon(games[i]))
        print(lst_zokon_and_lane_opponent)
             
        
        
    except Exception as e:
        print(e)

Zokon_bully()