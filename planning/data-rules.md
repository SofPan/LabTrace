1. Data constraints
All tables
[ ] Every record must have a primary key (`id`).
[ ] All foreign keys must reference an existing record.
[ ] Required fields must not be NULL.
[ ] UUID fields must use the same data type wherever they reference one another.
[ ] Timestamps must use a consistent convention, preferably UTC.

Samples
[ ] `clinic`, `submitter_id`, `stage`, `created_at`, and `updated_at` are required.
[ ] `submitter_id` must reference an existing user.
[ ] `stage` must be a valid `sample_stage` enum value.
[ ] `updated_at` must not be earlier than `created_at`.

Processing events
[ ] `sample_id` must reference an existing sample.
[ ] `performed_by` must reference an existing user.
[ ] `type` and `performed_at` are required.
[ ] Processing events should be retained as history rather than overwritten when a sample changes stage.

QC findings
[ ] `sample_id` must reference an existing sample.
[ ] `reported_by` must reference an existing user.
[ ] `type` must be `warning` or `failure`.
[ ] `status` must be `pending`, `reviewed`, or `resolved`.

Audit events
[ ] `actor` must reference an existing user.
[ ] `record_type`, `record_id`, `recorded_at`, and `action` are required.
[ ] `record_type` and `action` must use valid enum values.
[ ] Audit records should be append-only for normal application users.

2. Data validation requirements
Sample lifecycle
- Only permitted stage transitions are allowed.
- A sample cannot be marked completed while a blocking QC failure remains unresolved.
- A sample placed on_hold must have a recorded reason.
- Failed review may require returning a sample to processing.

User permissions
- Only authorized users may perform each action.
- Only reviewers may approve QC review, if that is your chosen business rule.
- Administrators may view audit history.
- The actor recorded for an action must match the user, not an arbitrary user ID

QC findings
- A finding must belong to an existing sample.
- A warning does not automatically block progression, a failure does
- Resolving a finding should preserve its original type and reporting history.
- A resolution should record who resolved it and when.

Audit integrity
- Every significant state change should create an audit event.
- Audit events should record the actor, action, timestamp, and relevant context.
- Audit history should not be silently rewritten or deleted.
- record_type and record_id must refer to a real record of the stated type.