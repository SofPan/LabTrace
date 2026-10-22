import uuid

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

from app.models.audit_event import RecordType, Action


class AuditEventCreate(BaseModel):
    actor: uuid.UUID
    record_type: RecordType
    record_id = uuid.UUID
    recorded_at = datetime.datetime
    action: Action
    details: str = Field(min_length=1, max_length=255)

class AuditEventRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    actor: uuid.UUID
    record_type: RecordType
    record_id = uuid.UUID
    recorded_at = datetime.datetime
    action: Action
    details: str
