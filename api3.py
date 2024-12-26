import requests
import api_key
import datetime
puuid = 'T_JrqTPht92WOsjhvXfMymiTTrm0BvsNJtcyx7l24owunfH49a4UXVYw9H0d8BhFmSCmrwggVsO2MQ'

lst = []

challenges = requests.get(f'https://eun1.api.riotgames.com/lol/challenges/v1/player-data/{puuid}?api_key={api_key.api_key}').json()

for i in range(len(challenges['challenges'])):
    #print(challenges['challenges'][i]['level'],i)
    if challenges['challenges'][i]['level'] == 'CHALLENGER' or challenges['challenges'][i]['level'] == 'GRANDMASTER':
        lst.append([challenges['challenges'][i]['challengeId'],challenges['challenges'][i]['level'],str(datetime.datetime.fromtimestamp(int(challenges['challenges'][i]['achievedTime'])/1000))[0:4]])

print(lst)
print(f'{len(lst)} were found in rang CHALLENGER/GRANDMASTER')

lst2 = []

for i in range(len(lst)):
    Leaderboard = requests.get(f'https://eun1.api.riotgames.com/lol/challenges/v1/challenges/{lst[i][0]}/leaderboards/by-level/{lst[i][1]}?limit=100000&api_key={api_key.api_key}').json()
    
    print(f'{i+1}/{len(lst)} challenges checked if on the leaderboard')
    
    for j in range(len(Leaderboard)):
        if Leaderboard[j]['puuid'] == puuid:
            print([lst[i],Leaderboard[j]['position']])
            lst2.append([lst[i],Leaderboard[j]['position']])    

for i in range(len(lst2)):
    name = requests.get(f'https://eun1.api.riotgames.com/lol/challenges/v1/challenges/{lst2[i][0][0]}/config?api_key={api_key.api_key}').json()
    #print(name)
    print(i)
    lst2[i][0].append(name['localizedNames']['en_US']['shortDescription'])
    print(lst2)
 
#print(lst2)
for i in range(len(lst2)):
	print(f'You are rank {lst2[i][1]} (all ranks included) on challenge "{lst2[i][0][3]}" on {lst2[i][0][1]} level in {lst2[i][0][2]}')