from pathlib import Path
import json

DATA_FILE = Path.home() / "StudentPerformance" / "students.json"
DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

def get_name():
    while True:
        details = input(f"Enter Student's name: ")
        if details.replace(" ", "").isalpha():
            return details
        else:
            print("Name is not valid")

def get_age():
    while True:
        try:
            age = int(input(f"Enter Student's age: "))
            if age >= 0:
                return age
            else:
                print("Invalid age. Please enter a valid age")
        except ValueError:
            print("Error Input")

def get_department():
    while True:
            details = input(f"Enter Student's department: ")
            if details.replace(" ", "").isalpha():
                return details
            else:
                print("Department is not valid")

def get_score():
    while True:
        try:
            score = int(input(f"Enter Student's score: "))
            if 0 <= score <= 100:
                return score
            else:
                print("!Invalid score. Please enter a score between 0 and 100")
        except ValueError:
            print(f"Error: Value Error")

def calculate_grade(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    elif 60 <= score <= 69:
        return "D"
    elif 50 <= score <= 59:
        return "E"
    else:
        return "F"

def create_student(name, age, department, score):
    grade = calculate_grade(score)
    return {
        "Name": name,
        "Age": age,
        "Department": department,
        "Score": score,
        "Grade": grade
    }

def add_student_info(student_info, students):
    students.append(student_info)
    return students

def action():
    print("===== STUDENT PERFORMANCE SYSTEM =====\n")
    print("1. Add Student\n" \
    "2. View Students\n" \
    "3. Search Student\n" \
    "4. Show Statistics\n" \
    "5. Exit")
    option = input("Choose an option from 1-5: ")
    return option

def add_student():
    name = get_name()
    age = get_age()
    department = get_department()
    score = get_score()
    student = create_student(name, age, department, score)
    all_students = add_student_info(student, students)
    save_students()
    return all_students

def view_student():
    if not students:
        print("❗No students have been added yet")
        return
    print(f"{'Name':<15}{'Age':<8}{'Department':<15}{'Score':<8}{'Grade':<8}")
    print("-" * 54)
    for student in students:
        print(
            f"{student['Name']:<15}"
              f"{student['Age']:<8}"
              f"{student['Department']:<15}"
              f"{student['Score']:<8}"
              f"{student['Grade']:<8}"
              )

def search_students():
    name = input("Enter Student's name to search: ")
    for student in students:
        if name.lower() == student["Name"].lower():
            print("====== Student Found ======")
            print(
                f"Name: {student["Name"]}\n"
                f"Age: {student["Age"]}\n"
                f"Department: {student["Department"]}\n"
                f"Score: {student["Score"]}\n"
                f"Grade: {student["Grade"]}"
            )
            return
    print("❗Student not found")

def statistics():
    if not students:
        print("No student available for statistics")
        return
    
    scores = []

    for student in students:
        scores.append(student["Score"])

    total_student = len(students)
    average_score = sum(scores)/total_student
    highest_score = max(scores)
    lowest_score = min(scores)

    print("\n===== Student Statistics ===== ")
    print(f"Number of Students: {total_student}")
    print(f"Average Score: {average_score:.2f}")
    print(f"Highest Score: {highest_score}")
    print(f"Lowest Score: {lowest_score}")

def save_students():
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)

def load_students():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        students = []

students = load_students()

while True:
    choice = action()
    if choice == "1":
        add_student()
        print("Student added successfully")
    elif choice == "2":
        view_student()
    elif choice == "3":
        search_students()
    elif choice == "4":
        statistics()
    elif choice == "5":
        print("!Goodbye")
        break
    else:
        print("Invalid, only pick from 1-5")
        
   