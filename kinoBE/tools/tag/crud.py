from kinoBE.core.crud import BaseCRUD
from kinoBE.tools.models import TagModel


class TagCRUD(BaseCRUD):
    model = TagModel