from pydantic import BaseModel

class UserAnimeCreate(BaseModel):
    anime_id: int

