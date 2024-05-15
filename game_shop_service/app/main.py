import os
import uvicorn
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Annotated

from database import database as database
from database.database import GameDB
from model.model import Game

app = FastAPI()

database.Base.metadata.create_all(bind=database.engine)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.get("/health", status_code=status.HTTP_200_OK)
async def service_alive():
    return {'message': 'Service alive'}


@app.post("/add_game")
async def add_game(game: Game, db: db_dependency):
    new_game = GameDB(**game.dict())
    db.add(new_game)
    db.commit()
    db.refresh(new_game)
    return "success"


@app.get("/games")
async def list_games(db: db_dependency):
    games = db.query(GameDB).all()
    return games


@app.get("/get_game_by_id")
async def get_game_by_id(game_id: int, db: db_dependency):
    game = db.query(GameDB).filter(GameDB.id == game_id).first()
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    return game


@app.delete("/delete_game")
async def delete_game(game_id: int, db: db_dependency):
    game = db.query(GameDB).filter(GameDB.id == game_id).first()
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    db.delete(game)
    db.commit()
    return {"message": "Game deleted successfully"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv('PORT', 80)))
