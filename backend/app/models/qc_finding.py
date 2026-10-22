import enum
import uuid

from datetime import datetime
from sqlalchemy import Enum, String, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

class FindingType(str, enum.Enum):
    warning = "warning"
    failure = "failure"

class QCStatus(str, enum.Enum):
    pending = "pending"
    reviewed = "reviewed"
    resolved = "resolved"


class QCFinding(Base):
    __tablename__ = "qc_findings"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    finding_type: Mapped[FindingType] = mapped_column(
        Enum(FindingType, name="finding_type"),
        nullable=False,
    )

    status: Mapped[QCStatus] = mapped_column(
        Enum(QCStatus, name="status"),
        nullable=False,
    )

    sample_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("samples.id"),
        nullable=False,
    )

    reported_by: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )