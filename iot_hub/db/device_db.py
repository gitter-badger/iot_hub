from sqlalchemy import Culumn

from iot_hub.db import input_db
from iot_hub.db import model_base
from iot_hub.db import output_db


class Device(model_base.Id, input_db.Input, output_db.Output):
    name = Column(String(255))
    inputs
