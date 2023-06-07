from datetime import datetime

from pydantic import BaseModel


# What we get from the API
class PostBase(BaseModel):
    image_url: str
    title: str
    content: str
    creator: str


# Give back to the caller
class PostDisplay(BaseModel):
    id: int
    image_url: str
    title: str
    content: str
    creator: str
    timestamp: datetime

    class Config():
        orm_mode = True