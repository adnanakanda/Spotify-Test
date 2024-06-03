from pydantic import BaseModel
from typing import List

class Artist(BaseModel):
    id: str
    name: str
    genres: List[str]
    songs: List[str]
