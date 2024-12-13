import requests
import time

Zokon_puuid = "DbjcFQpoiF_-F6FriNwcW2eLOMUwvpatv2if1W3JnEq3DZiYfylB9bzpzTuTVSIXHndatE0ag7Ecow"
api_key = '<<<<API_KEY_HERE>>>>'

def get_kdas():
    number_of_games = 5
    try:
        matches_url = f"https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{Zokon_puuid}/ids"
        params = {"start": 0, "count": number_of_games, "api_key": api_key}
        games = requests.get(matches_url, params=params).json()

        KDAs = []
        for game_id in games:
            match_url = f"https://europe.api.riotgames.com/lol/match/v5/matches/{game_id}"
            match_response = requests.get(match_url, params={"api_key": api_key})
            match_data = match_response.json()

            participants = match_data.get("info", {}).get("participants", [])
            for participant in participants:
                if participant.get("puuid") == Zokon_puuid:
                    kda = participant.get("challenges", {}).get("kda", 0)
                    KDAs.append("%.2f" % kda)
                    break
            
            time.sleep(1.2)

        print(f"Zokon's KDAs from the last {number_of_games} games: {KDAs}")
    except Exception as e:
        print(f"An error occurred: {e}")

get_kdas()