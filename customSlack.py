from slack_sdk import WebClient
import os

bot_id = os.environ.get("SLACK_BOT_TOKEN") 

client = WebClient(token=bot_id)


def create_slack_report_message(channel_id, job_details):
    """
    Creates a Slack message with job details and formatted blocks.
    """

    job_blocks = []
    for job in job_details:
        print("job-with-in-slack",job)
        status_text = f"*Status*: {job['Status']}"
        if job['Status'] == 'failure':
            status_text = f"*Status*: :x: {job['Status']}"
        elif job['Status'] == 'success':
            status_text = f"*Status*: :white_check_mark: {job['Status']}"

        job_block = {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*Job Name*: {job['Job Name']}\n{status_text}",
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
        job_blocks.append(job_block)

    message = {
        "channel": channel_id,
        "text": "Daily run cypress report ",
        "blocks": [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": ":newspaper: Daily Actions Report :newspaper:",
                },
            },
            {
                "type": "divider",
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
