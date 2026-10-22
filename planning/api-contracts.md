# LabTrace API Contracts

## Samples

### List Samples
- **Method:** `GET`
- **Endpoint:** `/api/samples`
- **Request:** Optional query parameters for filtering and pagination
- **Success:** `200 OK`
- **Response:** List of samples with `id`, `clinic`, `submitted_by`, `stage`, `created_at`, and `updated_at`

### Get Sample
- **Method:** `GET`
- **Endpoint:** `/api/samples/{sample_id}`
- **Request:** Sample UUID
- **Success:** `200 OK`
- **Errors:** `404 Not Found`
- **Response:** Sample details

### Create Sample
- **Method:** `POST`
- **Endpoint:** `/api/samples`
- **Request:** `clinic`, `submitted_by`
- **Success:** `201 Created`
- **Errors:** `422 Unprocessable Entity`
- **Response:** Created sample details, including generated `id`, `stage`, `created_at`, and `updated_at`

### Update Sample Stage
- **Method:** `PATCH`
- **Endpoint:** `/api/samples/{sample_id}/stage`
- **Request:** New `stage`
- **Success:** `200 OK`
- **Errors:** `404 Not Found`, `422 Unprocessable Entity`
- **Response:** Updated sample details

## Processing Events

### List Sample Processing Events
- **Method:** `GET`
- **Endpoint:** `/api/samples/{sample_id}/processing-events`
- **Request:** Sample UUID
- **Success:** `200 OK`
- **Errors:** `404 Not Found`
- **Response:** List of processing events with `id`, `sample_id`, `performed_by`, `event_type`, and `performed_at`

### Create Processing Event
- **Method:** `POST`
- **Endpoint:** `/api/samples/{sample_id}/processing-events`
- **Request:** `performed_by`, `event_type`
- **Success:** `201 Created`
- **Errors:** `404 Not Found`, `422 Unprocessable Entity`
- **Response:** Created processing event details, including generated `id` and `performed_at`

## QC Findings

### List QC Findings
- **Method:** `GET`
- **Endpoint:** `/api/qc-findings`
- **Request:** Optional query parameters for filtering by `status`, `finding_type`, or `sample_id`
- **Success:** `200 OK`
- **Response:** List of QC findings with `id`, `finding_type`, `status`, `sample_id`, and `reported_by`

### Get QC Finding
- **Method:** `GET`
- **Endpoint:** `/api/qc-findings/{finding_id}`
- **Request:** QC finding UUID
- **Success:** `200 OK`
- **Errors:** `404 Not Found`
- **Response:** QC finding details

### Create QC Finding
- **Method:** `POST`
- **Endpoint:** `/api/qc-findings`
- **Request:** `finding_type`, `sample_id`, `reported_by`
- **Success:** `201 Created`
- **Errors:** `404 Not Found`, `422 Unprocessable Entity`
- **Response:** Created QC finding details, including generated `id` and initial `status`

### Update QC Finding Status
- **Method:** `PATCH`
- **Endpoint:** `/api/qc-findings/{finding_id}/status`
- **Request:** New `status`
- **Success:** `200 OK`
- **Errors:** `404 Not Found`, `422 Unprocessable Entity`
- **Response:** Updated QC finding details

## Audit Events

### List Audit Events
- **Method:** `GET`
- **Endpoint:** `/api/audit-events`
- **Request:** Optional query parameters for filtering by `record_type`, `record_id`, `actor`, or date range
- **Success:** `200 OK`
- **Response:** List of audit events with `id`, `actor`, `record_type`, `record_id`, `recorded_at`, `action`, and `details`

### Get Audit Event
- **Method:** `GET`
- **Endpoint:** `/api/audit-events/{event_id}`
- **Request:** Audit event UUID
- **Success:** `200 OK`
- **Errors:** `404 Not Found`
- **Response:** Audit event details

## Users

### List Users
- **Method:** `GET`
- **Endpoint:** `/api/users`
- **Success:** `200 OK`
- **Response:** List of users with `id`, `name`, and `role`

### Get User
- **Method:** `GET`
- **Endpoint:** `/api/users/{user_id}`
- **Request:** User UUID
- **Success:** `200 OK`
- **Errors:** `404 Not Found`
- **Response:** User details

## Shared Conventions

- **Content type:** `application/json`
- **Identifiers:** UUIDs
- **Timestamps:** ISO 8601
- **Enums:**
  - `UserRole`: `technician`, `reviewer`, `administrator`
  - `Stage`: `received`, `processing`, `qc_review`, `completed`, `on_hold`
  - `FindingType`: `warning`, `failure`
  - `QCStatus`: `pending`, `reviewed`, `resolved`
  - `RecordType`: `qc_finding`, `sample`, `processing`
  - `Action`: `STATE_CHANGED`, `SUBMITTED`, `REVIEWED`, `ON_HOLD`
- **Validation errors:** `422 Unprocessable Entity`
- **Not found:** `404 Not Found`
