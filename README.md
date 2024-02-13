# JobStatus in Slack Notification

![NGJS](https://kk-artifacts.s3.ap-south-1.amazonaws.com/banner2.png)

Retrieve the workflow job status for specified jobs within a GitHub workflow run.

This GitHub Action fetches the status of one or two specified jobs within a running workflow and makes the results available for downstream actions. It is ideal for integrating job status checks into your workflows for conditional execution or Slack notifications.

## Features

- Notify the status of one or two specified jobs in a GitHub workflow.
- Integration with Slack for real-time notifications.
- Customizable "View Details" link for specific jobs.
- Support for matrix jobs and display of total failed test cases for automation workflows.

## Usage

Add this action to your workflow:

```yaml
- name: Send Slack notification for job status
  id: notifyjobstatus-id
  uses: KK-Repos/NotifyJobStatus@v1
  with:
    GH_PROJECT_ORGNAME: 'your-organization'
    GH_PROJECT_REPONAME: 'your-repository'
    RUN_ID: ${{ github.run_id }}
    JOB_NAME_1: 'job_name_1'
    JOB_NAME_2: 'job_name_2'  # Optional
    CHANNEL_ID: ${{ secrets.SLACK_CHANNEL_ID }}
    SLACK_BOT_TOKEN: ${{ secrets.SLACK_BOT_TOKEN }}
    GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
    
- name: Get output from NotifyJobStatus action
  run: echo ${{ steps.notifyjobstatus-id.outputs.my_output }}
```

### Inputs
- **GH_PROJECT_ORGNAME** (required): The GitHub organization name.
- **GH_PROJECT_REPONAME** (required): The GitHub repository name.
- **RUN_ID** (required): The ID of the current workflow run.
- **JOB_NAME_1** (required): The name of the first job to check status for.
- **JOB_NAME_2** (optional): The name of the second job to check status for.
- **GITHUB_TOKEN** (required): GitHub automatically creates a unique GITHUB_TOKEN secret to use in your workflow - [learn more](https://docs.github.com/en/actions/security-guides/automatic-token-authentication)
- **SLACK_CHANNEL_ID** (required): Provide Slack channel ID to send notifications.
- **SLACK_BOT_TOKEN**: Slack bot token.

To modify the link in the "View Details" button for a specific job:

- Set **CUSTOM_LINK** to `true`.
- Set **NEW_LINK_JOB_NAME** to the new link job name.

#### Matrix Jobs
If you have matrix jobs in your workflow Add the common name for the matrix in **JOB_NAME_1** as input, providing the common name for matrix (e.g., `automation-test`).

To display the total failed test cases for your automation, use **FAILURE_STATS** as the input value.

## Sample Output for Reference

![SampleOutput](https://kk-artifacts.s3.ap-south-1.amazonaws.com/sampleOutput.png)

## Open-Source Contribution Guidelines

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/improvement`.
3. Make your changes and commit them: `git commit -m 'Improve: Add more details to readme'`.
4. Push to the branch: `git push origin feature/improvement`.
5. Submit a pull request.

If you find this project helpful or just want to support it, consider [buying me coffee](https://www.buymeacoffee.com/kk.repos)!

Contributions are welcome! 🚀
