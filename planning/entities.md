# Schema Entities

**Sample**
id: uuid
clinic: string, name of the clinic the sample came from
submitter_id: string, id of the technician that submitted the sample
stage: ENUM, the current processing stage
created_at: timestamp, when sample entered the system
updated_at: timestamp, when the sample was last updated

**User**
id: uuid
name: string
role: ENUM, tech reviewer or administrator

**ProcessingEvent**
id: uuid
sample_id: sample_id
performed_by: user_id
type: string, the processing event type
performed_at: timestamp

**QCFinding**
id: uuid
type: warning, failure
status: pending, reviewed, resolved
sample_id: sample_id
reported_by: user_id

**AuditEvent**
id: uuid
actor: user_id
record_type: QC Finding, Sample, Processing
record_id: id from the record type
recorded_at: timestamp
action: ENUM, what was done (e.g. STATE_CHANGED)
details: string, additional information


