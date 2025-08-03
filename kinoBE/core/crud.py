from abc import ABC

from sqlalchemy.orm import Session


class BaseCRUD(ABC):

    @classmethod
    def model(cls):
        """
        Specify ORM Model
        """
        return {}

    @classmethod
    def query(cls, dbsession: Session, *columns):
        """
        Make a query to the ORM Model
        """
        if columns:
            return dbsession.query(*columns).select_from(cls.model)
        return dbsession.query(cls.model)

    @classmethod
    def get(cls, dbsession: Session, object_id, *args, **kwargs):
        """
        Get object by ID
        """
        return cls.query(dbsession, *args, **kwargs).filter(cls.model.id == object_id).one()

    @classmethod
    def add(cls, dbsession: Session, data: dict, *args, **kwargs):
        """
        Create an object
        """
        db_object = cls.model(**data)
        dbsession.add(db_object)
        dbsession.commit()
        dbsession.refresh(db_object)
        return db_object

    @classmethod
    def update(cls, dbsession: Session, object_id, data: dict, *args, **kwargs):
        """
        Update an object
        """
        db_object = cls.get(dbsession, object_id, *args, **kwargs)
        for key, value in data.items():
            setattr(db_object, key, value)
        dbsession.commit()
        dbsession.refresh(db_object)
        return db_object

    @classmethod
    def delete(cls, dbsession: Session, object_id, *args, **kwargs):
        """
        Delete an object
        """
        db_object = cls.get(dbsession, object_id, *args, **kwargs)
        dbsession.delete(db_object)
        dbsession.commit()
        return object_id
