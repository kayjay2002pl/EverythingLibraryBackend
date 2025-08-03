from kinoBE.core.crud import BaseCRUD
from kinoBE.tools.models import UserModel


class UserCRUD(BaseCRUD):
    model = UserModel