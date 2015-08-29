from sqlalchemy import Culumn

class Inputs:
    id 

class Device:
    id = Column(String(36), primary_key=True,
                default=lambda: str(uuid.uuid4()))
    name = Column(String(255))
    inputs
