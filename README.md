
# GetJobStatus GitHub Action

<p align=”center”>

<img width=”200" height=”200" src=”https://devopsjournal.io/images/2021/20211204/20211204_dev_to_hackathon.jpg" alt=”my banner”>

</p>

Retrieve the workflow job status for specified jobs within a GitHub workflow run.

This action fetches the status of one or two specified jobs within a running workflow and makes the results available for downstream actions. It's ideal for integrating job status checks into your workflows for conditional execution or notifications.

## Usage
- Add this action to your workflow:

```yaml
- uses: iamkishorekumar-git/GetJobStatus@v.01
  with:
    ORG: 'your-organization'
    REPO: 'your-repository'
    RUN_ID: ${{ github.run_id }}
    JOB_NAME_1: 'job_name_1'
    JOB_NAME_2: 'job_name_2'  # Optional

```

###### Inputs
- ORG (required): The GitHub organization name.
- REPO (required): The GitHub repository name.
- RUN_ID (required): The ID of the current workflow run.
- JOB_NAME_1 (required): The name of the first job to check status for.
- JOB_NAME_2 (optional): The name of the second job to check status for.
