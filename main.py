import workflow
import os
from dotenv import load_dotenv
load_dotenv()

org = os.environ.get("ORG")
repo = os.environ.get("REPO")
github_token = os.environ.get("GH_TOKEN")
branch_name = os.environ.get("BRANCH_NAME")

# workflow.trigger_workflow(org, repo, github_token, branch_name)

res = workflow.getWorkflowJobs(org,repo,github_token,7501651743)

target_jobs = ["unit-test-job", "cypress-run-job"]

output_lines = []

for x in res["jobs"]:
    if x["name"] in target_jobs:
        output_lines.append(f"Job Name: {x['name']}")
        output_lines.append(f"HTML URL: {x['html_url']}")
        output_lines.append(f"Status: {x['status']}")
        output_lines.append("---")

output = "\n".join(output_lines)  # Combine lines with newlines
print(f"::set-output name=my_output::{output}")  # Set output in single line
