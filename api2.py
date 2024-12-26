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
    Win_or_lose = {'Zokon':None}
    
    Infos = {'game_index':game_index,'gameid':game_id,'Zokon_and_opponent_champ':Zokon_and_opponent_champ,'Zokon_kills_and_deaths':Zokon_kills_and_deaths,'Zokon_and_opponent_gold':Zokon_and_opponent_gold,
             'Zokon_and_opponent_level':Zokon_and_opponent_level,'Zokon_vision':Zokon_vision,'Win/lose':Win_or_lose}
    
    Zokon_lane = None
    zokon_team_id = None
    game = requests.get(f'https://europe.api.riotgames.com/lol/match/v5/matches/{game_id}?api_key={api_key.api_key}').json()
    
    Teammate_puuids = [['Zeno','-PcTeoPUgqTB78I1NhKZmIYD_scNmCQMLWbq99P-h3cj4fwW80arGO7HmMdbVbrgMLdhCHP_pvFheg'],['Ado','FIBj2fy964xkTEaipq_dQhHIaxGQLDulvRO9nBp7YyidffV-ta7VshudlInNazpCVa77f3b_4xMu4Q'],
                       ['Tucsok','T_JrqTPht92WOsjhvXfMymiTTrm0BvsNJtcyx7l24owunfH49a4UXVYw9H0d8BhFmSCmrwggVsO2MQ'],['Enzo','AFhMtV6gZg9wyDFBnM-DMTel8PEz8ltwxxIe0LcU5Y94k8eXJ7iFgaG19UHwY0DluuQalBNarUyezw']]
    
    winrates = []
    for i in range(len(Teammate_puuids)):
                winrates.append([Teammate_puuids[i][0],0,0])   
        
       
    print(winrates)
    
    #print('LEFUTOTT BAZZZZEEEEEGGGGG')
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
                
            for j in range(len(Teammate_puuids)):
                if game['info']['participants'][i]['puuid'] == Teammate_puuids[j][1]:
                    print(Teammate_puuids[j][0])
                    if game['info']['participants'][i]['win'] == True:
                        Win_or_lose['Zokon'] = 'Win'
                        winrates[j][1] += 1
                    else:
                        Win_or_lose['Zokon'] = 'Lose'
                        winrates[j][2] += 1
                            
    print(winrates)
    
    if Zokon_and_opponent_id['Zokon'] is not None:
        #return Zokon_and_opponent_champ,Zokon_kills_and_deaths,Zokon_and_opponent_gold,Zokon_and_opponent_level
        return {'Infos_about_zokon_and_lane_opponent':Infos}
def Zokon_bully():
    number_of_matches = 10
    try:
        games = requests.get(f'https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{Zokon_puuid}/ids?start=0&count={number_of_matches}&api_key={api_key.api_key}').json()
        
        lst_zokon_and_lane_opponent = []
        for i in range(number_of_matches):
            info = Find_info_about_zokon(games[i],i)['Infos_about_zokon_and_lane_opponent']
            
            if info is not None:
                lst_zokon_and_lane_opponent.append(info)
                print(f'{i+1}/{number_of_matches} games checked')
            else:
                print(f'{i+1}/{number_of_matches} games checked (did not meet game requirements eg. ARAM)')
        print(lst_zokon_and_lane_opponent)

    except Exception as e:
        if games == {'status': {'message': 'Forbidden', 'status_code': 403}}:
            print('GET A NEW API KEY BOZO!!!44!4')
        else:
            print('idk what the fuck went wrong')
            print(f'error:{games}')

Zokon_bully()