import json
import os

FILE_PATH = "data/issues.json"

def load_issues():
    if not os.path.exists(FILE_PATH):
        return []

    with open(FILE_PATH, "r") as file:
        return json.load(file)

def save_issues(issues):
    with open(FILE_PATH, "w") as file:
        json.dump(issues, file, indent=4)
