from app.core.crud import BaseCRUD
from app.tools.models import ItemModel


class ItemCRUD(BaseCRUD):
    model = ItemModel