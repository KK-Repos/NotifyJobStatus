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


output_jobs = []

for x in res["jobs"]:
    if x["name"] in target_jobs:
        job_info = {
            "Job Name": x["name"],
            "HTML URL": x["html_url"],
            "Status": x["status"]
        }
        output_jobs.append(job_info)


output_file = os.getenv('GITHUB_OUTPUT')
    
with open(output_file, "a") as myfile:
    myfile.write(f"my_output={output_file}")


