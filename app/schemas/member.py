from datetime import datetime

from pydantic import BaseModel


class Member(BaseModel):
    mno: int
    userid: str
    passwd: str
    name: str
    email: str
    regdate: datetime

    class config:
        from_attributes = True

class NewMember(BaseModel):
    userid: str
    passwd: str
    name: str
    email: str
