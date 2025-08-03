from kinoBE.core.crud import BaseCRUD
from kinoBE.tools.models import ItemModel


class ItemCRUD(BaseCRUD):
    model = ItemModel