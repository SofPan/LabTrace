
"""Seed LabTrace with deterministic synthetic development data."""

from datetime import datetime, timedelta, timezone
from uuid import UUID

from app.db.session import SessionLocal
from app.models.user import User, UserRole
from app.models.sample import Sample, Stage
from app.models.processing_event import ProcessingEvent
from app.models.qc_finding import QCFinding, FindingType, QCStatus
from app.models.audit_event import AuditEvent, RecordType, Action

# Stable IDs make this script safe to rerun.
BASE_TIME = datetime(2026, 10, 20, 9, 0, 0)

USER_IDS = [UUID(f"00000000-0000-4000-8000-{i:012d}") for i in range(1, 6)]
SAMPLE_IDS = [UUID(f"10000000-0000-4000-8000-{i:012d}") for i in range(1, 16)]
EVENT_IDS = [UUID(f"20000000-0000-4000-8000-{i:012d}") for i in range(1, 21)]
FINDING_IDS = [UUID(f"30000000-0000-4000-8000-{i:012d}") for i in range(1, 9)]
AUDIT_IDS = [UUID(f"40000000-0000-4000-8000-{i:012d}") for i in range(1, 16)]


def seed_database() -> None:
    with SessionLocal() as session:
        try:
            # Users
            users = [
                User(
                    id=USER_IDS[0],
                    name="Alex Morgan",
                    role=UserRole.technician,
                ),
                User(
                    id=USER_IDS[1],
                    name="Jordan Lee",
                    role=UserRole.technician,
                ),
                User(
                    id=USER_IDS[2],
                    name="Taylor Chen",
                    role=UserRole.reviewer,
                ),
                User(
                    id=USER_IDS[3],
                    name="Morgan Patel",
                    role=UserRole.reviewer,
                ),
                User(
                    id=USER_IDS[4],
                    name="Casey Brooks",
                    role=UserRole.administrator,
                ),
            ]

            for user in users:
                if session.get(User, user.id) is None:
                    session.add(user)

            session.flush()

            # Samples distributed across all workflow stages.
            stages = [
                Stage.received,
                Stage.received,
                Stage.received,
                Stage.processing,
                Stage.processing,
                Stage.processing,
                Stage.processing,
                Stage.qc_review,
                Stage.qc_review,
                Stage.qc_review,
                Stage.completed,
                Stage.completed,
                Stage.completed,
                Stage.on_hold,
                Stage.on_hold,
            ]

            clinics = [
                "Northstar Family Clinic",
                "Riverside Medical Centre",
                "Cedar Grove Clinic",
                "Westfield Health Centre",
                "Lakeside Family Practice",
            ]

            samples = [
                Sample(
                    id=SAMPLE_IDS[i],
                    clinic=clinics[i % len(clinics)],
                    submitted_by=USER_IDS[i % 2],
                    stage=stages[i],
                    created_at=BASE_TIME - timedelta(hours=4 * i),
                    updated_at=BASE_TIME - timedelta(hours=2 * i),
                )
                for i in range(15)
            ]

            for sample in samples:
                if session.get(Sample, sample.id) is None:
                    session.add(sample)

            session.flush()

            # Processing history for samples.
            event_types = [
                "sample_received",
                "processing_started",
                "processing_completed",
                "quality_check_started",
                "sample_released",
            ]

            events = [
                ProcessingEvent(
                    id=EVENT_IDS[i],
                    sample_id=SAMPLE_IDS[i % 10],
                    performed_by=USER_IDS[i % 2],
                    event_type=event_types[i % len(event_types)],
                    performed_at=BASE_TIME - timedelta(hours=i),
                )
                for i in range(20)
            ]

            for event in events:
                if session.get(ProcessingEvent, event.id) is None:
                    session.add(event)

            session.flush()

            # QC findings covering both types and all statuses.
            finding_types = [
                FindingType.warning,
                FindingType.failure,
            ]
            statuses = [
                QCStatus.pending,
                QCStatus.reviewed,
                QCStatus.resolved,
            ]

            findings = [
                QCFinding(
                    id=FINDING_IDS[i],
                    finding_type=finding_types[i % 2],
                    status=statuses[i % 3],
                    sample_id=SAMPLE_IDS[7 + (i % 8)],
                    reported_by=USER_IDS[2 + (i % 2)],
                )
                for i in range(8)
            ]

            for finding in findings:
                if session.get(QCFinding, finding.id) is None:
                    session.add(finding)

            session.flush()

            # Audit history for samples, processing events, and QC findings.
            record_types = [
                RecordType.sample,
                RecordType.processing,
                RecordType.qc_finding,
            ]

            actions = [
                Action.SUBMITTED,
                Action.STATE_CHANGED,
                Action.REVIEWED,
                Action.ON_HOLD,
            ]

            audit_events = []

            for i in range(15):
                record_type = record_types[i % len(record_types)]

                if record_type == RecordType.sample:
                    record_id = SAMPLE_IDS[i % len(SAMPLE_IDS)]
                elif record_type == RecordType.processing:
                    record_id = EVENT_IDS[i % len(EVENT_IDS)]
                else:
                    record_id = FINDING_IDS[i % len(FINDING_IDS)]

                audit_events.append(
                    AuditEvent(
                        id=AUDIT_IDS[i],
                        actor=USER_IDS[i % len(USER_IDS)],
                        record_type=record_type,
                        record_id=record_id,
                        recorded_at=BASE_TIME - timedelta(minutes=30 * i),
                        action=actions[i % len(actions)],
                        details=f"Synthetic development audit event {i + 1}",
                    )
                )

            for event in audit_events:
                if session.get(AuditEvent, event.id) is None:
                    session.add(event)

            session.flush()
            session.commit()

            print("LabTrace development seed completed.")
            print(f"Users: {len(users)}")
            print(f"Samples: {len(samples)}")
            print(f"Processing events: {len(events)}")
            print(f"QC findings: {len(findings)}")
            print(f"Audit events: {len(audit_events)}")

        except Exception:
            session.rollback()
            raise


if __name__ == "__main__":
    seed_database()
