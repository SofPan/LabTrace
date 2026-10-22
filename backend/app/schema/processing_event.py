import uuid

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

class ProcessingEventCreate(BaseModel):
    sample_id = uuid.UUID
    event_type: str = Field(min_length=1, max_length=255)
    performed_by: uuid.UUID
    performed_at: datetime.datetime

class ProcessingEventRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    sample_id = uuid.UUID
    event_type: str
    performed_by: uuid.UUID
    performed_at: datetime.datetime
