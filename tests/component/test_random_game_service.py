import requests

base_url = 'http://localhost:8001'





def test_get_games():
    response = requests.get(f"{base_url}/games")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
