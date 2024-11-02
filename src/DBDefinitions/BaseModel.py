import sqlalchemy
import datetime

from sqlalchemy import (
    Column,
    String,
    BigInteger,
    Integer,
    DateTime,
    ForeignKey,
    Sequence,
    Table,
    Boolean,
    Uuid
)
from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.hybrid import hybrid_property
import uuid


def newUuidAsString():
    return f"{uuid.uuid4()}"


def UUIDFKey(comment=None, nullable=True, **kwargs):
    return Column(Uuid, index=True, comment=comment, nullable=nullable, **kwargs)

def UUIDColumn():
    return Column(Uuid, primary_key=True, comment="primary key", default=uuid)

###########################################################################################################################
#
# zde definujte sve SQLAlchemy modely
# je-li treba, muzete definovat modely obsahujici jen id polozku, na ktere se budete odkazovat
#


class BaseModel(DeclarativeBase):
    id = UUIDColumn()

    lastchange = Column(DateTime, server_default=sqlalchemy.sql.func.now())
    created = Column(DateTime, server_default=sqlalchemy.sql.func.now())

    createdby_id = UUIDFKey(nullable=True)#Column(ForeignKey("users.id"), index=True, nullable=True)
    changedby_id = UUIDFKey(nullable=True)#Column(ForeignKey("users.id"), index=True, nullable=True)
    rbacobject_id = UUIDFKey(nullable=True, comment="id rbacobject")#Column(ForeignKey("users.id"), index=True, nullable=True)
