# JobStatus in Slack Notification

![NGJS](https://kk-artifacts.s3.ap-south-1.amazonaws.com/banner2.png)

Retrieve the workflow job status for specified jobs within a GitHub workflow run.

This action fetches the status of one or two specified jobs within a running workflow and makes the results available for downstream actions. It's ideal for integrating job status checks into your workflows for conditional execution or slack notifications.

## Usage
- Add this action to your workflow:

```yaml
- uses: KK-Repos/NotifyJobStatus@v1
  with:
    ORG: 'your-organization'
    REPO: 'your-repository'
    RUN_ID: ${{ github.run_id }}
    JOB_NAME_1: 'job_name_1'
    JOB_NAME_2: 'job_name_2'  # Optional
    CHANNEL_ID: ${{ secrets.CHANNEL_ID }}
    SLACK_BOT_TOKEN: ${{ secrets.SLACK_BOT_TOKEN }}

```

###### Inputs
- ORG (required): The GitHub organization name.
- REPO (required): The GitHub repository name.
- RUN_ID (required): The ID of the current workflow run.
- JOB_NAME_1 (required): The name of the first job to check status for.
- JOB_NAME_2 (optional): The name of the second job to check status for.
- GH_TOKEN (required): Store the GITHUB_TOKEN as GH_TOKEN in either environment secrets or organization-level secrets.
- CHANNEL_ID (required): Provide Slack channel Id to send notification
- SLACK_BOT_TOKEN: Slack bot token
------------

## Sample output for reference

![SampleOutput](https://kk-artifacts.s3.ap-south-1.amazonaws.com/sampleOutput.png)


