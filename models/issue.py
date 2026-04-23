from datetime import datetime

class Issue:
    def __init__(self, issue_id, room, device, description, priority):
        self.issue_id = issue_id
        self.room = room
        self.device = device
        self.description = description
        self.priority = priority
        self.status = "OPEN"
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.updated_at = self.created_at

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        issue = Issue(
            data["issue_id"],
            data["room"],
            data["device"],
            data["description"],
            data["priority"]
        )
        issue.status = data["status"]
        issue.created_at = data["created_at"]
        issue.updated_at = data["updated_at"]
        return issue
