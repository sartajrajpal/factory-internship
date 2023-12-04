from openai import OpenAI
import requests
from requests.auth import HTTPBasicAuth
import os


def gpt(task_title, api_key):

    client = OpenAI(api_key = api_key)
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Task Title: " + task_title + " Required Expansion Scope: " +
        "Description: Elaborate briefly on the objective and technical specifics. " +
        "Acceptance Criteria: List specific functional and performance requirements for completion. " +
        "Sub-Tasks: Outline key sub-tasks with succinct descriptions. " +
        "Assumptions: Note any assumptions underpinning this task. " +
        "Challenges and Solutions: Identify potential hurdles and propose practical solutions. " +
        "Resources: Specify essential tools and resources. " +
        "Time Estimate: Provide an overall time estimate for completion. " +
        "Notes: Add any other critical information for understanding and executing the task. " +
        "Response Format: Structure the response for direct integration into a project management tool (e.g., Jira, Linear), ensuring clarity and actionability for software engineers."
    },
        {"role": "user", "content": "Please expand the given project title into a detailed scope for a software engineering task as described. Make sure you don't double print."}
    ]
    )

    return (completion.choices[0].message.content)
'''
def jira(issue_title, issue_description, jira_domain, jira_username, jira_api_token):
    url = f"https://{jira_domain}.atlassian.net/rest/api/3/issue"
    auth = HTTPBasicAuth(jira_username, jira_api_token)

    headers = {
       "Accept": "application/json",
       "Content-Type": "application/json"
    }

    payload = {
        "fields": {
           "project":
           {
               "key": "ENTER KEY NAME"
           },
           "summary": issue_title,
           "description": issue_description,
           "issuetype": {
               "name": "Task"
           }
       }
    }

    response = requests.request(
       "POST",
       url,
       json=payload,
       headers=headers,
       auth=auth
    )

    return response.json()
'''
def main():
    # i know this is not good practice in terms of swe but im just putting it here for simplicity's sake
    OPENAI_API_KEY = "api-key" #replace with your OpenAI API token
    jira_domain = "sartaj"        
    jira_username = "Sartaj Rajpal"    
    jira_api_token = "api-key"  # Replace with your Jira API token

    if not OPENAI_API_KEY:
        print("OpenAI API key not found.")
        return
    task_title = input("Enter task title: ")
    task = gpt(task_title, OPENAI_API_KEY)
    #ticket_response = jira(task_title, task, jira_domain, jira_username, jira_api_token)
    #print("Ticket Created:", ticket_response)
    print(task)

if __name__ == "__main__":
    main()