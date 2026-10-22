import enum
import uuid

from datetime import datetime
from sqlalchemy import Enum, String, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Stage(str, enum.Enum):
    received = "Received"
    processing = "Processing"
    qc_review = "QC Review"
    completed = "Completed"
    on_hold = "On Hold"


class Sample(Base):
    __tablename__ = "samples"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    clinic: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    submitted_by: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    stage: Mapped[Stage] = mapped_column(
        Enum(Stage, name="stage"),
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )