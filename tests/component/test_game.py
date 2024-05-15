import requests

game_shop_url = 'http://localhost:8000'
add_game_url = f'{game_shop_url}/add_game'
get_games_url = f'{game_shop_url}/games'
get_game_by_id_url = f'{game_shop_url}/get_game_by_id'
delete_game_url = f'{game_shop_url}/delete_game'

new_game = {
    "id": 1,
    "name": "The Witcher 3: Wild Hunt",
    "release_year": 2015,
    "genre": "Action RPG"
}


def test_1_add_game():
    res = requests.post(add_game_url, json=new_game)
    assert res.status_code == 200


def test_2_get_games():
    res = requests.get(get_games_url).json()
    assert any(game['name'] == "The Witcher 3: Wild Hunt" for game in res)


def test_3_get_game_by_id():
    res = requests.get(get_games_url).json()
    game_id = next((game['id'] for game in res if game['name'] == "The Witcher 3: Wild Hunt"), None)
    res = requests.get(f"{get_game_by_id_url}?game_id={game_id}").json()
    assert res['id'] == game_id


def test_4_delete_game():
    res = requests.get(get_games_url).json()
    game_id = next((game['id'] for game in res if game['name'] == "The Witcher 3: Wild Hunt"), None)
    res = requests.delete(f"{delete_game_url}?game_id={game_id}")
    assert res.status_code == 200
