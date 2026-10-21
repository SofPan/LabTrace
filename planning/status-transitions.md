# Sample Status Transitions

**Received:** Sample registered and awaiting processing
**Processing:** Lab processing is underway
**QC Review:** Processing is complete; results await review
**Completed:** Review passed
**On Hold:** A problem requires investigation

## Transition Rules
- Received -> Processing
- Processing -> QC Review
- QC Review -> COmpleted
- QC Review -> Processing (Review failed, reprocessing necessary)
- Any active stage -> On Hold
- On Hold -> Any previous stage

## QC Findings
- Warning: The sample can continue, but the finding remains visible for review.
- Blocked: Sample cannot advance until the finding is resolved.
- Resolved: Preserve original finding, record how and when it was resolved.

## Illegal Transitions
- Received -> QC Review
- Received/Processing -> Completed 
- On Hold -> Completed
- Completed -> Any other stage