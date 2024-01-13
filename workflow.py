import requests
import logging
import json


logging.basicConfig(level=logging.INFO)

def trigger_workflow(org, repo, github_token, branch_name):

    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {github_token}",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    data = {"ref": branch_name}

    url = f"https://api.github.com/repos/{org}/{repo}/actions/workflows/deploy.yml/dispatches"

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        logging.info(f"Workflow dispatch triggered successfully: {response}")
    except requests.exceptions.RequestException as error:
        logging.error(f"Failed to trigger workflow: {error}")

def getWorkflowJobs(org, repo, github_token, run_id):

    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {github_token}",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    url = f"https://api.github.com/repos/{org}/{repo}/actions/runs/{run_id}/jobs"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return json.loads(response.text)
    except requests.exceptions.RequestException as error:
        logging.error(f"Failed to trigger workflow: {error}")