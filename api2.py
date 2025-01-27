import discord
from discord.ext import commands
from discord import app_commands
import discord_bot_token
import api_key
print(f'API key = {api_key.api_key}')
intents = discord.Intents.default()

client = commands.Bot(command_prefix='!', intents=intents)

GUILD_ID = 881507710993063936


@client.event
async def on_ready():
    print(f'Bot is ready. Logged in as {client.user}')
    try:
        guild = discord.Object(id=GUILD_ID)
        synced = await client.tree.sync(guild=guild)
        print(f'Synced {len(synced)} command(s) to guild {GUILD_ID}.')
    except Exception as e:
        print(f'Error syncing commands: {e}')


@client.tree.command(name='zokon_bully_simulator', description='Ohhh YEAAAHHH', guild=discord.Object(id=GUILD_ID))
@app_commands.describe(numberofgames='This is a useless parameter')
async def alma(interaction: discord.Interaction, numberofgames: int):
    import requests

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
                        ['Tucsok','T_JrqTPht92WOsjhvXfMymiTTrm0BvsNJtcyx7l24owunfH49a4UXVYw9H0d8BhFmSCmrwggVsO2MQ'],['Enzo','AFhMtV6gZg9wyDFBnM-DMTel8PEz8ltwxxIe0LcU5Y94k8eXJ7iFgaG19UHwY0DluuQalBNarUyezw'],
                        ['Astra','HAeJux-_xw5kPp7egJIKY73wArfD2VpCc32Fp53nBFPg39C--np1bAbjtOWU4gGRhWdLCs7DRgZUHg'],['Adam','EZBu30T1tGf3Mr4YU_d2HJqJAuEgzPZO2OeBgg_ZiW3i3A_1NFFZwSp3zWcjhYqq5pIVQ7lWlrdi7A'],
                        ['Dani','NrtvUImvM5fa9lCUjtJxi0OX5QjfBVHgzxPgJTAjL--u83cCkafl-cJP-RAtoL2BQMX7bHplTD0Y0Q']]
        
        winrates = []
        for i in range(len(Teammate_puuids)):
                    winrates.append([Teammate_puuids[i][0],0,0])   
            
        
        #print(winrates)
        
        #print('LEFUTOTT BAZZZZEEEEEGGGGG')
        #print(game)
        if game == {'status': {'message': 'Rate limit exceeded', 'status_code': 429}}:
            print(str(game['status']['message']) + '(' + str(game['status']['status_code'])+ ')')
            return game['status']['status_code']
        else:
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
                            #print(Teammate_puuids[j][0])
                            if game['info']['participants'][i]['win'] == True:
                                Win_or_lose['Zokon'] = 'Win'
                                winrates[j][1] += 1
                            else:
                                Win_or_lose['Zokon'] = 'Lose'
                                winrates[j][2] += 1
                                    
            #print(winrates)
            
            if Zokon_and_opponent_id['Zokon'] is not None:
                #return Zokon_and_opponent_champ,Zokon_kills_and_deaths,Zokon_and_opponent_gold,Zokon_and_opponent_level
                return {'Infos_about_zokon_and_lane_opponent':Infos,'Winrates':winrates}

    number_of_matches = numberofgames
    try:
        games = requests.get(f'https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{Zokon_puuid}/ids?start=0&count={number_of_matches}&api_key={api_key.api_key}').json()
                
        lst_zokon_and_lane_opponent = {}
        Winrates = []
        for i in range(number_of_matches):
            The_whole_function = Find_info_about_zokon(games[i],i)
            #print(The_whole_function,games[i],i)
            if The_whole_function is not None and isinstance(The_whole_function,dict) == True:
                info = The_whole_function['Infos_about_zokon_and_lane_opponent']
                Wins_and_Loses = The_whole_function['Winrates']
                
                if Winrates == []:
                    Winrates = Wins_and_Loses
                else:
                    for j in range(len(Winrates)):
                        if Wins_and_Loses[j][1] == 1:
                            Winrates[j][1] += 1
                        elif Wins_and_Loses[j][2] == 1:
                            Winrates[j][2] += 1
                            
                lst_zokon_and_lane_opponent.update({i:info})
                try:
                    print((i+1)%5,i+1)
                    if (i+1)%5 == 0 or i+1 == number_of_matches:
                        await interaction.response.send_message(f'{i+1}/{number_of_matches} games checked')
                except:
                    if (i+1)%5 == 0 or i+1 == number_of_matches:
                        await interaction.followup.send(f'{i+1}/{number_of_matches} games checked')
            elif The_whole_function == 429:
                pass
            else:
                try:
                    if (i+1)%5 == 0 or i+1 == number_of_matches:
                        await interaction.response.send_message(f'{i+1}/{number_of_matches} games checked')
                except:
                    if (i+1)%5 == 0 or i+1 == number_of_matches:
                        await interaction.followup.send(f'{i+1}/{number_of_matches} games checked')
        #for i in range(len(lst_zokon_and_lane_opponent)):
            #pass
            #await interaction.followup.send(lst_zokon_and_lane_opponent[i])
        for i in range(len(Winrates)):
            if Winrates[i][1]+Winrates[i][2] > 0:
                Winrates[i].append(str((Winrates[i][1]/(Winrates[i][1]+Winrates[i][2]))*100)[0:5])
            else:
                Winrates[i].append(None)
        #await interaction.followup.send(Winrates)
        #await interaction.followup.send(lst_zokon_and_lane_opponent)

    except Exception as e:
        if games != None:
            await interaction.followup.send(e)
            print(e)
            #await interaction.response.send_message(games['status']['message'] , '(' , games['status']['status_code'], ')')
        else:
            await interaction.followup.send('idk what the fuck went wrong')
    print(lst_zokon_and_lane_opponent)         
    for i in range(len(lst_zokon_and_lane_opponent)):
        try:
            print(lst_zokon_and_lane_opponent[i]['Zokon_kills_and_deaths']['Kill'],lst_zokon_and_lane_opponent[i]['Zokon_kills_and_deaths']['Death'])
            if lst_zokon_and_lane_opponent[i]['Zokon_kills_and_deaths']['Death'] != 0:
                if lst_zokon_and_lane_opponent[i]['Zokon_kills_and_deaths']['Kill']/lst_zokon_and_lane_opponent[i]['Zokon_kills_and_deaths']['Death'] < 0.5:
                    await interaction.followup.send(f"Zokonnak {lst_zokon_and_lane_opponent[i]['Zokon_and_opponent_champ']['Zokon']} champel {lst_zokon_and_lane_opponent[i]['Zokon_kills_and_deaths']['Kill']} killje és {lst_zokon_and_lane_opponent[i]['Zokon_kills_and_deaths']['Death']} halála volt.)
        except:
            pass

client.run(discord_bot_token.discord_bot_token)