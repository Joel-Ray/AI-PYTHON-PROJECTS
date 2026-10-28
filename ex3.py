#Menu-Driven Student Information System
Students={}
def add_student():
    roll=input("Enter  rollNo: ")
    name=input("Enter name: ")
    dept=input("Enter department: ")
    Students[roll]={"name":name,"department":dept}
    print("Student added successfully!")
def view_students():
    if not Students:
        print("No students record found.")
        return
    else:
        print("\n---Student Records---")
        for roll,data in Students.items():
            print("Roll No:",roll, 
                  "|Name:", data["name"], 
                  "|Department:", data["department"])
def search_student():
    roll=input("Enter rollNo to search: ")
    if roll in Students:
        print(Students[roll])
    else:
        print("Student not found.")                
def delete_student():
    roll=input("Enter rollNo to delete: ")
    if roll in Students:
        del Students[roll]
        print("Student deleted successfully!")
    else:
        print("Student not found.")
while True:
    print("\n---Student Information System---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
    choice=input("Enter your choice (1-5): ")
    if choice=="1":
        add_student()
    elif choice=="2":
        view_students()
    elif choice=="3":
        search_student()
    elif choice=="4":
        delete_student()
    elif choice=="5":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")                    