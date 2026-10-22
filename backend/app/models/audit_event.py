import enum
import uuid

from datetime import datetime
from sqlalchemy import Enum, String, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

class RecordType(str, enum.Enum):
    qc_finding = "QC Finding"
    sample = "Sample"
    processing = "Processing"

class Action(str, enum.Enum):
    STATE_CHANGED = "STATE CHANGED"
    SUBMITTED = "SUBMITTED"
    REVIEWED = "REVIEWED"
    ON_HOLD = "ON_HOLD"


class AuditEvent(Base):
    __tablename__ = "audit_events"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    actor: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    record_type: Mapped[RecordType] = mapped_column(
        Enum(RecordType, name="record_type"),
        nullable=False,
    )

    record_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        nullable=False,
    )

    recorded_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    action: Mapped[Action] = mapped_column(
        Enum(Action, name="action"),
        nullable=False,
    )

    details: Mapped[str] = mapped_column(
        String(255),
        nullable=True,
    )

    