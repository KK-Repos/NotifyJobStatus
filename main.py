import workflow , customSlack
import os
from dotenv import load_dotenv
load_dotenv()

org = os.environ.get("GH_PROJECT_ORGNAME")
repo = os.environ.get("GH_PROJECT_REPONAME")
github_token = os.environ.get("GH_ACTION_TOKEN")
run_id = os.environ.get("RUN_ID")
job_name_1 = os.environ.get("JOB_NAME_1")
job_name_2 = os.environ.get("JOB_NAME_2")
select_job = os.environ.get("NEW_LINK_JOB_NAME")
customLink = os.environ.get("CUSTOM_LINK")
CHANNEL_ID = os.environ.get("SLACK_CHANNEL_ID")
FAILURE_STATS = os.environ.get("FAILURE_STATS")
artifactName = os.environ.get("ARTIFACT_NAME")
html_url = None 
target_jobs = [job_name_2]
matrix_jobs = [job_name_1]


getJobResponse = workflow.getWorkflowJobs(org,repo,github_token,run_id)

print("[getJobResponse]",getJobResponse)

def extract_job_info(res, matrix_jobs, customLink=None, select_job=None):
    temp = []
    for x in res["jobs"]:
        jobName = x["name"]
        if any(target_job is not None and target_job in jobName for target_job in matrix_jobs):
            job_info = {
                "Job Name": x["name"],
                "HTML URL": x["html_url"],
                "Status": x["conclusion"]
            }
            temp.append(job_info)
    print("[temp]",temp)
    def check_status(data):
        all_successful = all(job['Status'] == 'success' for job in data)
        print("all_successful",all_successful)
        if all_successful:
            return [{'Job Name': job_name_1, 'Status': 'success', 'HTML URL': data[0]['HTML URL']}]
        else:
            html_url = None 
            if customLink and select_job:
                for x in res["jobs"]:
                    if x["name"] in select_job:
                        html_url = x["html_url"]
                URL = html_url if customLink else x["html_url"]
                return [{'Job Name': job_name_1, 'Status': 'failure', 'HTML URL': URL, 'Total failed test cases': FAILURE_STATS}]
            else:
                return [{'Job Name': job_name_1, 'Status': 'failure', 'HTML URL': data[0]['HTML URL']}]
    result = check_status(temp)
    return result

result_data = extract_job_info(getJobResponse, matrix_jobs, customLink, select_job)

output_jobs = []

for x in getJobResponse["jobs"]:
    jobName = x["name"]
    if jobName in target_jobs:
        job_info = {
            "Job Name": jobName,
            "HTML URL": x["html_url"],
            "Status": x["conclusion"]
        }
        output_jobs.append(job_info)

output_jobs = output_jobs + result_data

print("[output_jobs]",output_jobs)
output_file = os.getenv('GITHUB_OUTPUT')
    
with open(output_file, "a") as myfile:
    myfile.write(f"my_output={output_jobs}")


artifactID = workflow.getLatestArtifactId(org, repo, github_token, artifactName, run_id)

if artifactID is not None:
    workflow.downloadArtifact(org, repo, github_token, artifactID)
else:
    print("No artifact ID found. Skipping download.")

slackReportMessage = customSlack.create_slack_report_message(CHANNEL_ID,output_jobs)
sendMessage=customSlack.send_slack_message(CHANNEL_ID,slackReportMessage)
