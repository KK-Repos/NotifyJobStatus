from slack_sdk import WebClient
from dotenv import load_dotenv
load_dotenv()
import os
from datetime import datetime

bot_id = os.environ.get("SLACK_BOT_TOKEN")
repoName = os.environ.get("REPO_NAME") 
enable_fail_case = os.environ.get("ENABLE_FAIL_CASE") 
currentDate = datetime.now().strftime("%A, %B %d, %Y")


client = WebClient(token=bot_id)


def create_slack_report_message(channel_id, job_details):
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

        if enable_fail_case and key_length >=4:
            details_text += f"\n*Total failed test cases*: {job['Total failed test cases']}"

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

            # Add color bar based on status



    message = {
        "channel": channel_id,
        "text": "Github Actions Daily Report ",
        "blocks": [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": ":slack: Github Actions Daily Report :slack:",
                },
            },
            {
                "type": "divider",
            },
            {
                "type": "context",
                "elements": [
                    {
                        "text": f"{currentDate} | Repo: *{repoName}*",
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
