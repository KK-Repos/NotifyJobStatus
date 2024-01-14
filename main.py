import workflow
import os
from dotenv import load_dotenv
load_dotenv()

org = os.environ.get("ORG")
repo = os.environ.get("REPO")
github_token = os.environ.get("GH_TOKEN")
run_id = os.environ.get("RUN_ID")
job_name_1 = os.environ.get("JOB_NAME_1")
job_name_2 = os.environ.get("JOB_NAME_2")

print("[job_name_1]",job_name_1)
print("[job_name_2]",job_name_2)

target_jobs = [job_name_1,job_name_2]
print("[target_jobs]",target_jobs)
print("[run_id]",run_id)


res = workflow.getWorkflowJobs(org,repo,github_token,run_id)

target_jobs = ["unit-test-job", "cypress-run-job"]

output_jobs = []

for x in res["jobs"]:
    if x["name"] in target_jobs:
        job_info = {
            "Job Name": x["name"],
            "HTML URL": x["html_url"],
            "Status": x["conclusion"]
        }
        output_jobs.append(job_info)


output_file = os.getenv('GITHUB_OUTPUT')
    
with open(output_file, "a") as myfile:
    myfile.write(f"my_output={output_jobs}")


