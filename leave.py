leaves = []

while True:
    print("\n1. Apply Leave")
    print("2. View Leaves")
    print("3. Edit Leave")
    print("4. Approve Leave")
    print("5. Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        emp = input("Employee Name: ")
        leave_type = input("Leave Type (SL/CL/PL/LWP): ")
        reason = input("Reason: ")
        start = input("Start Date: ")
        end = input("End Date: ")
        days = int(input("Total Days: "))

        leaves.append({
            "employee": emp,
            "leave_type": leave_type,
            "reason": reason,
            "start_date": start,
            "end_date": end,
            "total_days": days,
            "status": "Pending"
        })

        print("Leave Applied Successfully.")

    elif ch == 2:
        for l in leaves:
            print(l)

    elif ch == 3:
        emp = input("Employee Name: ")

        for l in leaves:
            if l["employee"] == emp:
                if l["status"] == "Pending":
                    l["reason"] = input("New Reason: ")
                    print("Leave Updated.")
                else:
                    print("Approved leave cannot be edited.")

    elif ch == 4:
        emp = input("Employee Name: ")

        for l in leaves:
            if l["employee"] == emp:
                l["status"] = input(
                    "Status (Approved/Rejected): "
                )

    elif ch == 5:
        break