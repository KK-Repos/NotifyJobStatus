
# GetJobStatus GitHub Action

Retrieve the workflow job status for specified jobs within a GitHub workflow run.

This action fetches the status of one or two specified jobs within a running workflow and makes the results available for downstream actions. It's ideal for integrating job status checks into your workflows for conditional execution or notifications.

Inputs
ORG (required): The GitHub organization name.
REPO (required): The GitHub repository name.
RUN_ID (required): The ID of the current workflow run.
JOB_NAME_1 (required): The name of the first job to check status for.
JOB_NAME_2 (optional): The name of the second job to check status for.
