import requests
import logging
import json


logging.basicConfig(level=logging.INFO)

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
        logging.error(f"Failed to fetch the job details: {error}")