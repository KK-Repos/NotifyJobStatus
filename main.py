import workflow , customSlack
import os
from dotenv import load_dotenv
load_dotenv()

org = os.environ.get("ORG")
repo = os.environ.get("REPO")
github_token = os.environ.get("GH_TOKEN")
run_id = os.environ.get("RUN_ID")
job_name_1 = os.environ.get("JOB_NAME_1")
job_name_2 = os.environ.get("JOB_NAME_2")
select_job = os.environ.get("TARGET_JOB")
modify_job = os.environ.get("MODIFY_JOB")
customLink = os.environ.get("CUSTOM_LINK")
CHANNEL_ID = os.environ.get("CHANNEL_ID") 
html_url = None 
target_jobs = [job_name_1,job_name_2]


getJobResponse = workflow.getWorkflowJobs(org,repo,github_token,run_id)

output_jobs = []

if customLink and select_job:
    print("inside")
    for x in res["jobs"]:
        if x["name"] in select_job:
            html_url=x["html_url"]

for x in res["jobs"]:
    if x["name"] in target_jobs:
        job_info = {
            "Job Name": x["name"],
            "HTML URL": html_url if (customLink and x["name"] == modify_job and x["conclusion"] == "failure") else x["html_url"],
            "Status": x["conclusion"]
        }
        output_jobs.append(job_info)

output_file = os.getenv('GITHUB_OUTPUT')
    
with open(output_file, "a") as myfile:
    myfile.write(f"my_output={output_jobs}")

slackReportMessage = customSlack.create_slack_report_message(CHANNEL_ID,output_jobs)
sendMessage=customSlack.send_slack_message(CHANNEL_ID,slackReportMessage)
