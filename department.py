departments = []

while True:
    print("\n1.Add Department")
    print("2.View Department")
    print("3.Update Department")
    print("4.Delete Department")
    print("5.Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        name = input("Department Name: ")
        desc = input("Description: ")

        departments.append({
            "name": name,
            "description": desc,
            "status": True
        })

        print("Department Added")

    elif ch == 2:
        for d in departments:
            print(d)

    elif ch == 3:
        old = input("Department Name: ")
        for d in departments:
            if d["name"] == old:
                d["name"] = input("New Name: ")
                d["description"] = input("New Description: ")

    elif ch == 4:
        old = input("Department Name: ")
        for d in departments:
            if d["name"] == old:
                d["status"] = False
                print("Department Inactive")

    elif ch == 5:
        break