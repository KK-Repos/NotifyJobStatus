from slack_sdk import WebClient
from dotenv import load_dotenv
load_dotenv()
import os
from datetime import datetime
import zipfile
import json

bot_id = os.environ.get("SLACK_BOT_TOKEN")
repoName = os.environ.get("GH_PROJECT_REPONAME") 
enable_fail_case = os.environ.get("ENABLE_FAIL_CASE") 
currentDate = datetime.now().strftime("%A, %B %d, %Y")
job_name_1 = os.environ.get("JOB_NAME_1")
artifactFileName = os.environ.get("ARTIFACT_FILE_NAME")
client = WebClient(token=bot_id)
zip_file_path = "artifact.zip"
totalFailedCount = 0


def create_slack_report_message(channel_id, job_details):
    global totalFailedCount
    """
    Creates a Slack message with job details and formatted blocks.
    """

    job_blocks = []

    for job in job_details:
        key_length = len(job.keys())
        status_text = f"*Status*: {job['Status']}"
        if job['Status'] == 'failure':
            status_text = f"*Status*: :x: {job['Status']}"
        elif job['Status'] == 'success':
            status_text = f"*Status*: :white_check_mark: {job['Status']}"

        details_text = f"*Job Name*: {job['Job Name']}\n{status_text}"

        if enable_fail_case == 'true' and job['Status'] == 'failure' and job['Job Name'] == job_name_1:
            totalFailedCount = job['Total failed test cases']

        job_block = {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": details_text,
            },
            "accessory": {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "text": "View Details",
                },
                "url": job['HTML URL'],
            },
        }
        if job['Status'] == 'success':
            job_block["accessory"]["style"] = "primary"
        elif job['Status'] == 'failure':
            job_block["accessory"]["style"] = "danger"
    
        job_blocks.append(job_block)

    if enable_fail_case:
        job_blocks.append({
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": f"*Total Failed Test cases count*:  { totalFailedCount }",
        },
    })

    if enable_fail_case == 'true' and job['Status'] == 'failure' and job['Job Name'] == job_name_1:
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            file_content = zip_ref.read(artifactFileName)
            res = json.loads(file_content.decode('utf-8'))
            for result in res["result"]:
                runner_name = result["runnerName"]
                test_cases = result["testcases"]
                filenames = [test_case["text"] for test_case in test_cases]
                            
                runner_block = [
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": f"*Container ID:* {runner_name}",
                        },
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": f"\t ".join(filenames),
                        },
                    },
                ]

                job_blocks.extend(runner_block)

    message = {
        "channel": channel_id,
        "text": "Github Actions Daily Report ",
        "blocks": [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": ":sparkles: Github Actions Daily Report :sparkles:",
                },
            },
            {
                "type": "divider",
            },
            {
                "type": "context",
                "elements": [
                    {
                        "text": f"{currentDate} | Repo: *{repoName.upper()}*",
                        "type": "mrkdwn"
                    }
                ]
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": " :loud_sound: *STATS* :loud_sound:",
                },
            },
            {
                "type": "divider",
            },
        ] + job_blocks
    }

    return message


def send_slack_message(channel_id, message_payload):
    """
    Sends a Slack message using the provided channel Id  and message payload.
    """
    response = client.chat_postMessage(
        channel=channel_id,
        text=message_payload["text"],
        blocks=message_payload["blocks"]
    )
    return response
