tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Update Status")
    print("4. Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        title = input("Task Title: ")
        desc = input("Description: ")
        priority = input("Priority (High/Medium/Low): ")
        employee = input("Assigned To: ")
        status = "Pending"

        tasks.append({
            "title": title,
            "description": desc,
            "priority": priority,
            "employee": employee,
            "status": status
        })

        print("Task Assigned Successfully.")

    elif ch == 2:
        for t in tasks:
            print(t)

    elif ch == 3:
        title = input("Task Title: ")

        for t in tasks:
            if t["title"] == title:
                t["status"] = input(
                    "Status (Pending/In Progress/Completed): "
                )

    elif ch == 4:
        break