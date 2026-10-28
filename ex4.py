#Student Record Management With List,Tuple,Dictionary and CSV
import csv
students=[
    {"rollNo": "101", "Name": "Anitha", "Department": "CSE","Marks": 86},
    {"rollNo": "102", "Name": "Bala", "Department": "CSE","Marks": 91},
    {"rollNo": "103", "Name": "Chitra", "Department": "ECE","Marks": 78}
]
#Tuple example
course=("python",4)
print("Course Tuple:", course)
#Write text file
with open("students.txt", "w") as file:
    for student in students:
        file.write(str(student)+"\n")
#Write CSV file
with open("students.csv", "w", newline="") as csvfile:
    field = ["rollNo", "Name", "Department","Marks"]
    writer = csv.DictWriter(csvfile, fieldnames=field)
    writer.writeheader()
    writer.writerow(student)
#Read CSV file
print("\n---Student Records from CSV---")
with open("students.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row["rollNo"], row["Name"], row["Department"], row["Marks"])    