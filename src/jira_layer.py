import os
import requests
from dotenv import load_dotenv

load_dotenv()


def create_jira_issue(task_name, description):

    jira_url = os.getenv("JIRA_BASE_URL")
    jira_email = os.getenv("JIRA_EMAIL")
    jira_token = os.getenv("JIRA_API_TOKEN")
    project_key = os.getenv("JIRA_PROJECT_KEY")

    url = f"{jira_url}/rest/api/3/issue"

    payload = {
        "fields": {
            "project": {"key": project_key},
            "summary": task_name,
            "description": {
                "type": "doc",
                "version": 1,
                "content": [
                    {
                        "type": "paragraph",
                        "content": [
                            {
                                "type": "text",
                                "text": description
                            }
                        ]
                    }
                ]
            },
            "issuetype": {
                "name": "Task"
            }
        }
    }

    response = requests.post(
        url,
        json=payload,
        auth=(jira_email, jira_token),
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
    )

    if response.status_code == 201:
        issue_key = response.json()["key"]
        print(f"Jira issue created: {issue_key}")
    else:
        print("Error:", response.status_code)
        print(response.text)


class JiraConnector:

    def __init__(self):
        self.base_url = os.getenv("JIRA_BASE_URL")
        self.email = os.getenv("JIRA_EMAIL")
        self.token = os.getenv("JIRA_API_TOKEN")
        self.project_key = os.getenv("JIRA_PROJECT_KEY")

    def fetch_tasks(self):

        url = f"{self.base_url}/rest/api/3/search"

        query = {
            "jql": f"project={self.project_key}",
            "maxResults": 10,
            "fields": "summary,status"
        }

        response = requests.get(
            url,
            params=query,
            auth=(self.email, self.token),
            headers={
                "Accept": "application/json"
            }
        )

        print("Status code:", response.status_code)

        data = response.json()

        tasks = []

        for issue in data.get("issues", []):

            fields = issue.get("fields", {})

            tasks.append({
                "task_id": issue.get("key", issue.get("id", "UNKNOWN")),
                "task_name": fields.get("summary", "No summary"),
                "status": fields.get("status", {}).get("name", "Unknown")
            })

        return tasks