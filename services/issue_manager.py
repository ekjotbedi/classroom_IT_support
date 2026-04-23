from models.issue import Issue
from utils.file_handler import load_issues, save_issues
from datetime import datetime

class IssueManager:
    def __init__(self):
        self.issues = [Issue.from_dict(i) for i in load_issues()]

    def generate_id(self):
        return len(self.issues) + 1

    def create_issue(self, room, device, description, priority):
        issue = Issue(self.generate_id(), room, device, description, priority)
        self.issues.append(issue)
        self.save()
        print("Issue logged successfully.")

    def list_issues(self):
        if not self.issues:
            print("No issues found.")
            return

        for issue in self.issues:
            print(vars(issue))

    def update_status(self, issue_id, new_status):
        for issue in self.issues:
            if issue.issue_id == issue_id:
                issue.status = new_status
                issue.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save()
                print("Status updated.")
                return
        print("Issue not found.")

    def escalate_issue(self, issue_id):
        for issue in self.issues:
            if issue.issue_id == issue_id:
                issue.status = "ESCALATED"
                issue.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save()
                print("Issue escalated to Technical Support.")
                return
        print("Issue not found.")

    def save(self):
        save_issues([issue.to_dict() for issue in self.issues])
