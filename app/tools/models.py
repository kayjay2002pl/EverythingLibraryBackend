import sqlalchemy as db
from sqlalchemy.dialects.postgresql import UUID

from app.core.models import BaseModel

# This is a config file for main database objects
# Feature roadmap includes interactive commandline program to easily edit all of them
# For now they have to be edited here.
# After you're done with editing, you need to create an alembic revision and upgrade your database using the following:

# alembic revision?--autogenerate -m "nameYourRevision"
# alembic upgrade head


class AssociationModel(BaseModel):
    """
    Postgresql model for association object
    """
    __tablename__= "associations"
    item_id = db.Column(UUID(as_uuid=True), db.ForeignKey("items.id", ondelete="CASCADE"))
    tag_id = db.Column(UUID(as_uuid=True), db.ForeignKey("tags.id", ondelete="CASCADE"))


class ItemModel(BaseModel):
    """
    Postgresql model for item object
    """
    __tablename__= "items"
    name = db.Column(db.String, unique=False, nullable=False)
    description = db.Column(db.String, unique=False)
    owner_id = db.Column(UUID(as_uuid=True), db.ForeignKey("users.id", ondelete="CASCADE"))


class TagModel(BaseModel):
    """
    Postgresql model for tag object
    """
    __tablename__= "tags"
    name = db.Column(db.String, unique=True, nullable=False)


class UserModel(BaseModel):
    """
    Postgresql model for user object
    """
    __tablename__= "users"
    email = db.Column(db.String, unique=True, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)