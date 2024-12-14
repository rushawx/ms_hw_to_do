import datetime
from typing import List

from pydantic import BaseModel


class ItemRequest(BaseModel):
    title: str
    description: str
    completed: bool | None = False


class ItemResponse(BaseModel):
    id: int
    title: str
    description: str
    completed: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime


class AllItemsResponse(BaseModel):
    items: List[ItemResponse]

    class Config:
        orm_mode = True
        from_attributes = True
