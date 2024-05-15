import requests

base_url = 'http://localhost:8001'


def test_get_game_by_id():
    response = requests.get(f"{base_url}/game/3498")  # Замените ID на корректный ID игры
    assert response.status_code == 200
    assert 'name' in response.json()


def test_get_games():
    response = requests.get(f"{base_url}/games")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
