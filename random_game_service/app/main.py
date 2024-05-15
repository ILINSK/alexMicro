import uvicorn
from fastapi import FastAPI, HTTPException, status
import requests

app = FastAPI()

FREE_TO_GAME_API_URL = "https://www.freetogame.com/api"

@app.get("/health", status_code=status.HTTP_200_OK)
async def service_alive():
    return {'message': 'Service alive'}

@app.get("/game/{game_id}")
async def get_game_by_id(game_id: int):
    url = f"{FREE_TO_GAME_API_URL}/game?id={game_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise HTTPException(status_code=400, detail="Error retrieving game data")

@app.get("/games")
async def get_games():
    url = f"{FREE_TO_GAME_API_URL}/games"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise HTTPException(status_code=400, detail="Error retrieving games data")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
