# JobStatus in Slack Notification

![NGJS](https://kk-artifacts.s3.ap-south-1.amazonaws.com/banner2.png)

Retrieve the workflow job status for specified jobs within a GitHub workflow run.

This action fetches the status of one or two specified jobs within a running workflow and makes the results available for downstream actions. It's ideal for integrating job status checks into your workflows for conditional execution or slack notifications.

## Usage
- Add this action to your workflow:

```yaml

- name: Send Slack notificatoin for job status
  id: notifyjobstatus-id
  uses: KK-Repos/NotifyJobStatus@v1
  with:
    GH_PROJECT_ORGNAME: 'your-organization'
    GH_PROJECT_REPONAME: 'your-repository'
    RUN_ID: ${{ github.run_id }}
    JOB_NAME_1: 'job_name_1'
    JOB_NAME_2: 'job_name_2'  # Optional
    CHANNEL_ID: ${{ secrets.CHANNEL_ID }}
    SLACK_BOT_TOKEN: ${{ secrets.SLACK_BOT_TOKEN }}
    GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
- name: Get output from NotifyJobStatus actions
  run: echo ${{ steps.notifyjobstatus-id.outputs.my_output }}

```

###### Inputs
- ORG (required): The GitHub organization name.
- REPO (required): The GitHub repository name.
- RUN_ID (required): The ID of the current workflow run.
- JOB_NAME_1 (required): The name of the first job to check status for.
- JOB_NAME_2 (optional): The name of the second job to check status for.
- GITHUB_TOKEN (required): GitHub automatically creates a unique GITHUB_TOKEN secret to use in your workflow - to know more click [here](https://docs.github.com/en/actions/security-guides/automatic-token-authentication)
- CHANNEL_ID (required): Provide Slack channel Id to send notification
- SLACK_BOT_TOKEN: Slack bot token
------------

To modify the link in the "View Details" button for a specific job:

- CUSTOM_LINK: true
- NEW_LINK_JOB_NAME: New link job name

#### Matrx Jobs
Matrix jobs should same name but ending with 0,1 like that if you have matrix jobs in your workflow - add that job name in JOB_NAME_1 as input provide the common name for matrix - automation-test 
## Sample output for reference

# To Display total failed test cases for your automaytion use

FAILURE_STATS input value as some number 

![SampleOutput](https://kk-artifacts.s3.ap-south-1.amazonaws.com/sampleOutput.png)
