from app.core.crud import BaseCRUD
from app.tools.models import TagModel


class TagCRUD(BaseCRUD):
    model = TagModel