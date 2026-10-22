import uuid

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

from app.models.qc_finding import QCStatus, FindingType


class QCFindingCreate(BaseModel):
    status: QCStatus
    finding_type: FindingType
    sample_id = uuid.UUID
    reported_by: uuid.UUID

class QCFindingRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    status: QCStatus
    finding_type: FindingType
    sample_id = uuid.UUID
    reported_by: uuid.UUID
