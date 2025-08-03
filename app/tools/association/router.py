from fastapi import APIRouter, Depends, status

from app.core.database import SessionLocal, create_session
from app.tools.association.crud import AssociationCRUD
from app.tools.schema import Association

router = APIRouter(
    tags=["association"]
)



@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(
    data: Association,
    dbsession: SessionLocal = Depends(create_session),
):
    """
    Create association entry
    """
    data = data.model_dump()
    user_metric = AssociationCRUD.add(dbsession, data=data)
    return user_metric