# Create blocks for each job detail
job_blocks = []
for job in output_jobs:
    job_block = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": f"*Job Name*: {job['Job Name']}\n*Status*: {job['Status']}\n*HTML URL*: {job['HTML URL']}"
        }
    }
    job_blocks.append(job_block)

# Create the Slack message
MESSAGE = {
    "channel": channel_id,
    "text": "Daily run cypress report",
    "blocks": [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": ":newspaper: Daily CircleCi Report :newspaper:",
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
    ] + job_blocks,  # Add job detail blocks to the message
    "attachments": [output_jobs],
}

# Send the Slack message
response = client.chat_postMessage(
    channel=channel_id,
    text=MESSAGE["text"],
    blocks=MESSAGE["blocks"],
    attachments=MESSAGE["attachments"]
)

assert response["message"]["text"] == MESSAGE["text"]