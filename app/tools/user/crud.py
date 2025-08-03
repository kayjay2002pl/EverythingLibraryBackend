from app.core.crud import BaseCRUD
from app.tools.models import UserModel


class UserCRUD(BaseCRUD):
    model = UserModel