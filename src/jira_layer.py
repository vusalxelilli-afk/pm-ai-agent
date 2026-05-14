import os
import requests
from dotenv import load_dotenv

load_dotenv()

def create_jira_issue(task_name, description):
    jira_url = os.getenv("JIRA_BASE_URL")
    jira_email = os.getenv("JIRA_EMAIL")
    jira_token = os.getenv("JIRA_API_TOKEN")
    project_key = os.getenv("JIRA_PROJECT_KEY")

    print("JIRA_BASE_URL:", jira_url)
    print("JIRA_EMAIL:", jira_email)
    print("JIRA_PROJECT_KEY:", project_key)

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
                            {"type": "text", "text": description}
                        ]
                    }
                ]
            },
            "issuetype": {"name": "Task"}
        }
    }

    print("Sending request to Jira...")

    try:
        response = requests.post(
            url,
            json=payload,
            auth=(jira_email, jira_token),
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json"
            },
            timeout=20
        )

        print("Response received")
        print("Status code:", response.status_code)
        print("Response text:", response.text[:500])

        if response.status_code == 201:
            issue_key = response.json()["key"]
            print(f"Jira issue created: {issue_key}")
        else:
            print("Jira issue was NOT created.")

    except Exception as e:
        print("Request failed:")
        print(e)