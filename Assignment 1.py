students = {
    1: (101, "Aman", "CSE", 85),
    2: (102, "Riya", "IT", 90),
    3: (103, "Rahul", "ECE", 78)
}

students[4] = (104, "Neha", "CSE", 88)
del students[2]
students[3] = (103, "Rahul", "CSE", 82)

for roll, details in students.items():
    print(roll, details)
