from sqlalchemy import Column
from sqlalchemy import String
import uuid

class Id(object):
    id = Column(String(36),
                primary_key=True,
                default=uuid.uuid4())
