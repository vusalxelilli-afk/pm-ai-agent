from src.jira_layer import create_jira_issue
from datetime import datetime

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

create_jira_issue(
    task_name=f"AI Agent automatic Jira task {now}",
    description=f"This task was automatically created from Python at {now}."
)