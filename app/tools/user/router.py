from fastapi import APIRouter, Depends, status

from app.core.database import SessionLocal, create_session
from app.tools.user.crud import UserCRUD
from app.tools.schema import User

router = APIRouter(
    tags=["user"]
)



@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(
    data: User,
    dbsession: SessionLocal = Depends(create_session),
):
    """
    Create user entry
    """
    data = data.model_dump()
    user_metric = UserCRUD.add(dbsession, data=data)
    return user_metric