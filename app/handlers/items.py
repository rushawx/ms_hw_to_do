import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.engine import Item
from app.models.items import AllItemsResponse, ItemRequest, ItemResponse
from app.utils.utils import get_db

router = APIRouter(prefix="/items", tags=["items"])


@router.post("/")
async def create_item(item: ItemRequest, db: Session = Depends(get_db)) -> ItemResponse:
    db_item = Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@router.get("/")
async def get_items(db: Session = Depends(get_db)) -> AllItemsResponse:
    db_items = db.query(Item).all()
    response_items = []
    for db_item in db_items:
        response_items.append(
            ItemResponse(
                id=db_item.id,
                title=db_item.title,
                description=db_item.description,
                completed=db_item.completed,
                created_at=db_item.created_at,
                updated_at=db_item.updated_at,
            )
        )
    return AllItemsResponse(items=response_items)


@router.get("/{item_id}")
async def get_item(item_id: int, db: Session = Depends(get_db)) -> ItemResponse:
    db_item = db.query(Item).get(item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    response = ItemResponse(
        id=db_item.id,
        title=db_item.title,
        description=db_item.description,
        completed=db_item.completed,
        created_at=db_item.created_at,
        updated_at=db_item.updated_at,
    )
    return response


@router.put("/{item_id}")
async def update_item(
    item_id: int, item: ItemRequest, db: Session = Depends(get_db)
) -> ItemResponse:
    db_item = db.query(Item).get(item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db_item.title = item.model_dump()["title"]
    db_item.description = item.model_dump()["description"]
    db_item.completed = item.model_dump()["completed"]
    db_item.updated_at = datetime.datetime.now()
    response = ItemResponse(
        id=db_item.id,
        title=db_item.title,
        description=db_item.description,
        completed=db_item.completed,
        created_at=db_item.created_at,
        updated_at=db_item.updated_at,
    )
    db.query(Item).filter(Item.id == item_id).update(response.model_dump())
    db.commit()
    return response


@router.delete("/{item_id}")
async def delete_item(item_id: int, db: Session = Depends(get_db)) -> ItemResponse:
    db_item = db.query(Item).get(item_id)
    db.query(Item).filter(Item.id == item_id).delete()
    db.commit()
    response = ItemResponse(
        id=db_item.id,
        title=db_item.title,
        description=db_item.description,
        completed=db_item.completed,
        created_at=db_item.created_at,
        updated_at=db_item.updated_at,
    )
    return response
