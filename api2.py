import requests
import api_key

Zokon_puuid = 'DbjcFQpoiF_-F6FriNwcW2eLOMUwvpatv2if1W3JnEq3DZiYfylB9bzpzTuTVSIXHndatE0ag7Ecow'

def Find_info_about_zokon(game_id,game_index):
    Zokon_and_opponent_id = {'Zokon':None,'Zokon_opponent':None}
    Zokon_and_opponent_champ = {'Zokon':None,'Zokon_opponent':None}
    Zokon_kills_and_deaths = {'Kill':None,'Death':None}
    Zokon_and_opponent_gold = {'Zokon':None,'Zokon_opponent':None}
    Zokon_and_opponent_level = {'Zokon':None,'Zokon_opponent':None}
    Zokon_vision = {'Zokon':None}
    
    Infos = {'game_index':game_index,'gameid':game_id,'Zokon_and_opponent_champ':Zokon_and_opponent_champ,'Zokon_kills_and_deaths':Zokon_kills_and_deaths,'Zokon_and_opponent_gold':Zokon_and_opponent_gold,
             'Zokon_and_opponent_level':Zokon_and_opponent_level,'Zokon_vision':Zokon_vision}
    
    Zokon_lane = None
    zokon_team_id = None
    game = requests.get(f'https://europe.api.riotgames.com/lol/match/v5/matches/{game_id}?api_key={api_key.api_key}').json()
    
    
    def Zokon_game_info():
        nonlocal Zokon_lane, zokon_team_id
        if game['info']['gameMode'] == 'CLASSIC':
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
                    Zokon_kills_and_deaths['Kill'] = game['info']['participants'][Zokon_and_opponent_id['Zokon']]['kills']
                    Zokon_kills_and_deaths['Death'] = game['info']['participants'][Zokon_and_opponent_id['Zokon']]['deaths']
                    Zokon_and_opponent_gold['Zokon'] = game['info']['participants'][Zokon_and_opponent_id['Zokon']]['goldEarned']
                    Zokon_and_opponent_gold['Zokon_opponent'] = game['info']['participants'][Zokon_and_opponent_id['Zokon_opponent']]['goldEarned']
                    Zokon_and_opponent_level['Zokon'] = game['info']['participants'][Zokon_and_opponent_id['Zokon']]['champLevel']
                    Zokon_and_opponent_level['Zokon_opponent'] = game['info']['participants'][Zokon_and_opponent_id['Zokon_opponent']]['champLevel']
                    Zokon_vision['Zokon'] = game['info']['participants'][Zokon_and_opponent_id['Zokon']]['visionScore']
                    break
                
                
    Zokon_game_info()
    if Zokon_and_opponent_id['Zokon'] is not None:
        #return Zokon_and_opponent_champ,Zokon_kills_and_deaths,Zokon_and_opponent_gold,Zokon_and_opponent_level
        return Infos
def Zokon_bully():
    number_of_matches = 100
    try:
        games = requests.get(f'https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{Zokon_puuid}/ids?start=0&count={number_of_matches}&api_key={api_key.api_key}').json()
        #print(games)
        
        lst_zokon_and_lane_opponent = []
        for i in range(number_of_matches):
            if Find_info_about_zokon(games[i],i) is not None: 
                lst_zokon_and_lane_opponent.append(Find_info_about_zokon(games[i],i))
                print(f'{i+1}/{number_of_matches} games checked')
            else:
                print(f'{i+1}/{number_of_matches} games checked (did not meet game requirements eg. ARAM)')
        print(lst_zokon_and_lane_opponent)
             
    except Exception as e:
        print(e)

Zokon_bully()