from app.core.schema import SchemaConfig


class User(SchemaConfig):
    email: str
    username: str
    password: str


class Tag(SchemaConfig):
    name: str


class Item(SchemaConfig):
    name: str
    owner_id: str


class Association(SchemaConfig):
    item_id: str
    tag_id: str