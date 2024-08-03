import requests
import logging
import json
import time


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

def getLatestArtifactId(org, repo, pat_token,artifactName,run_id):
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {pat_token}",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    url = f"https://api.github.com/repos/{org}/{repo}/actions/runs/{run_id}/artifacts"
    response = json.loads(requests.get(url, headers=headers).text)
    for artifact in response['artifacts']:
        if artifact['name'] == artifactName:
            return artifact['id']

def downloadArtifact(org, repo, pat_token,artifactID):
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {pat_token}",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    url = f"https://api.github.com/repos/{org}/{repo}/actions/artifacts/{artifactID} /zip"

    response = requests.get(url, headers=headers, allow_redirects=True)

    if response.status_code == 200:
        with open("artifact.zip", "wb") as f:
            f.write(response.content)
        print(f"Artifact-{artifactID} downloaded successfully.")
    else:
        print(f"Failed to download artifact. Status code: {response.status_code}")
