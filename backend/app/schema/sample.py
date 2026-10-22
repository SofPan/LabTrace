import uuid

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

from app.models.sample import Stage


class SampleCreate(BaseModel):
    clinic: str = Field(min_length=1, max_length=255)
    submitted_by: uuid.UUID
    stage: Stage
    created_at: datetime.datetime
    updated_at: datetime.datetime

class SampleRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    clinic: str
    submitted_by: uuid.UUID
    stage: Stage
    created_at: datetime.datetime
    updated_at: datetime.datetime
