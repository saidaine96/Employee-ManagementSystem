reviews = []

while True:
    print("\n1. Add Review")
    print("2. View Reviews")
    print("3. Update Rating")
    print("4. Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        title = input("Review Title: ")
        date = input("Review Date (DD-MM-YYYY): ")
        employee = input("Employee Name: ")
        reviewer = input("Reviewed By: ")
        period = input("Review Period (Monthly/Quarterly/Annual): ")
        rating = int(input("Rating (1-10): "))
        comments = input("Comments: ")

        reviews.append({
            "title": title,
            "date": date,
            "employee": employee,
            "reviewer": reviewer,
            "period": period,
            "rating": rating,
            "comments": comments
        })

        print("Review Added Successfully.")

    elif ch == 2:
        for r in reviews:
            print(r)

    elif ch == 3:
        employee = input("Employee Name: ")

        for r in reviews:
            if r["employee"] == employee:
                r["rating"] = int(input("New Rating: "))
                r["comments"] = input("New Comments: ")
                print("Review Updated.")

    elif ch == 4:
        break