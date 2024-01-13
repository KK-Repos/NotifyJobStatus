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
print(type(res))

print(len(res["jobs"]))

for x in res["jobs"]:
    if x["name"] == "unit-test-job" or  x["name"] == "cypress-run-job":
        print(x["name"])
        print(x["html_url"])
        print(x["status"])