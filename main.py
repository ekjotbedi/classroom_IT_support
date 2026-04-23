from services.issue_manager import IssueManager

def menu():
    print("\n--- Classroom IT Support System ---")
    print("1. Log Issue")
    print("2. View Issues")
    print("3. Update Issue Status")
    print("4. Escalate Issue")
    print("5. Exit")

def main():
    manager = IssueManager()

    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            room = input("Enter room: ")
            device = input("Enter device (projector/mic/etc): ")
            description = input("Describe issue: ")
            priority = input("Priority (LOW/MEDIUM/HIGH): ")
            manager.create_issue(room, device, description, priority)

        elif choice == "2":
            manager.list_issues()

        elif choice == "3":
            issue_id = int(input("Enter issue ID: "))
            status = input("Enter new status (IN PROGRESS / RESOLVED): ")
            manager.update_status(issue_id, status)

        elif choice == "4":
            issue_id = int(input("Enter issue ID: "))
            manager.escalate_issue(issue_id)

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
