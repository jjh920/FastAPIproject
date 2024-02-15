from datetime import datetime

from pydantic import BaseModel


class Gallery(BaseModel):
    gno: int
    title: str
    userid: str
    regdate: datetime
    views: int
    contents: str

    class Config:
        from_attributes = True



class NewGallery(BaseModel):
    title: str
    userid: str
    contents: str



class GalAttach(BaseModel):
    gano: int
    gno: int
    fname: str
    fsize: int

    class Config:
        from_attributes = True


