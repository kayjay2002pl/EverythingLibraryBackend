from app.core.crud import BaseCRUD
from app.tools.models import AssociationModel


class AssociationCRUD(BaseCRUD):
    model = AssociationModel