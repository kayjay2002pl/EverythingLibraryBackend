import uuid

import sqlalchemy as db
from sqlalchemy.dialects.postgresql import UUID

from kinoBE.core.database import Base

class BaseModel(Base):
    __abstract__ = True

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
