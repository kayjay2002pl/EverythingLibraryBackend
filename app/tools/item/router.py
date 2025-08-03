from fastapi import APIRouter, Depends, status

from app.core.database import SessionLocal, create_session
from app.tools.item.crud import ItemCRUD
from app.tools.schema import Item

router = APIRouter(
    tags=["item"]
)



@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(
    data: Item,
    dbsession: SessionLocal = Depends(create_session),
):
    """
    Create item entry
    """
    data = data.model_dump()
    user_metric = ItemCRUD.add(dbsession, data=data)
    return user_metric