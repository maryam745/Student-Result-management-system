print("===== Student Result Management System =====\n")

students = []  # List to store multiple students' data

while True:
    name = input("Enter student name: ").strip()
    if not name:
        print("Name cannot be empty!")
        continue

    # Validate number of subjects
    while True:
        try:
            subjects = int(input("Enter number of subjects: "))
            if subjects <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid positive integer for subjects.")

    marks_list = []
    total_marks = 0

    for i in range(subjects):
        while True:
            try:
                marks = float(input(f"Enter marks of subject {i+1} (0-100): "))
                if marks < 0 or marks > 100:
                    raise ValueError
                break
            except ValueError:
                print("Invalid marks! Enter a number between 0 and 100.")
        marks_list.append(marks)
        total_marks += marks

    percentage = total_marks / subjects

    if percentage >= 80:
        grade = "A"
        status = "Pass"
    elif percentage >= 60:
        grade = "B"
        status = "Pass"
    elif percentage >= 40:
        grade = "C"
        status = "Pass"
    else:
        grade = "F"
        status = "Fail"

    student_record = {
        "Name": name,
        "Subjects": marks_list,
        "Total": total_marks,
        "Percentage": percentage,
        "Grade": grade,
        "Status": status
    }

    students.append(student_record)

    choice = input("\nAdd another student? (yes/no): ").strip().lower()
    if choice != "yes":
        break

# Calculate class average and topper
if students:
    total_class_marks = sum(s["Total"] for s in students)
    total_subjects_class = sum(len(s["Subjects"]) for s in students)
    class_average = total_class_marks / total_subjects_class

    topper = max(students, key=lambda x: x["Percentage"])

# Display results
print("\n===== Final Results =====")
for s in students:
    print("\nName:", s["Name"])
    print("Marks per Subject:", s["Subjects"])
    print("Total Marks:", s["Total"])
    print("Percentage: {:.2f}%".format(s["Percentage"]))
    print("Grade:", s["Grade"])
    print("Status:", s["Status"])

print("\n===== Class Summary =====")
print("Class Average Percentage: {:.2f}%".format(class_average))
print("Topper: {} with {:.2f}%".format(topper["Name"], topper["Percentage"]))
