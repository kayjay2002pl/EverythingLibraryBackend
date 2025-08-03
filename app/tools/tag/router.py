from fastapi import APIRouter, Depends, status

from app.core.database import SessionLocal, create_session
from app.tools.tag.crud import TagCRUD
from app.tools.schema import Tag

router = APIRouter(
    tags=["tag"]
)



@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(
    data: Tag,
    dbsession: SessionLocal = Depends(create_session),
):
    """
    Create tag entry
    """
    data = data.model_dump()
    user_metric = TagCRUD.add(dbsession, data=data)
    return user_metric