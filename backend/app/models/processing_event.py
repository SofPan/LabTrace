import uuid

from datetime import datetime
from sqlalchemy import Enum, String, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

class ProcessingEvent(Base):
    __tablename__ = "processing_events"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    sample_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("samples.id"),
        nullable=False,
    )

    performed_by: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    event_type: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    performed_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )