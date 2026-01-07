# f=open("sample.txt","a+")
# for i in range(5):
#     name=input("enter the student name:")
#     f.write(name)
# f.seek(0)
# content=f.read()
# print(content)
# f.close()

# with open ("sample1.txt","a+") as f:
#     f.write("2nd Day Python Internship\n")
#     f.write("Learning with a fun is always best")
#     f.seek(0)
#     con=f.read()
#     print(con)

import csv

# Writing CSV
with open("students.csv", "w", newline="") as file:
    wrote = csv.writer(file)
    wrote.writerow(["Name", "Marks"])
    wrote.writerow(["Amra", 95])
    wrote.writerow(["Ramya", 97])

# Reading CSV
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for i in reader:
        print(i)

import json

# Writing JSON
student = [{"name": "Amra", "marks": 95},{"name": "Ramya", "marks": 97}]
with open("student.json", "w") as file:
    json.dump(student, file)

# Reading JSON
with open("student.json", "r") as file:
    data = json.load(file)
    print(data)

import csv

students_data = [
    ["Name", "Marks"],
    ["Amra", 95],
    ["Ramya", 97],
    ["Sameer", 92]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students_data)
students_list = []
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)  # Reads as dict automatically
    for row in reader:
        students_list.append(row)

print(students_list)  # [{'Name': 'Amra', 'Marks': '95'}, ...]

import json

with open("students.json", "w") as file:
    json.dump(students_list, file)

with open("students.json", "r") as file:
    data = json.load(file)
    for student in data:
        print(f"{student['Name']} scored {student['Marks']} marks")
