from pydantic import BaseModel
from typing import Optional

class Game(BaseModel):
    id: Optional[int]
    name: str
    release_year: int
    genre: str
