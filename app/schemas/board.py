from datetime import datetime

from pydantic import BaseModel


class Board(BaseModel):
    bno: int
    title: str
    userid: str
    regdate: datetime
    views: int
    contents: str

    class Config:
        from_attributes = True


class NewBoard(BaseModel):
    title: str
    userid: str
    contents: str
    response: str