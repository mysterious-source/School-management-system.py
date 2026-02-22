students = []
teachers= []
subjects= []
grades = []
id = []
year_1 = []
year_2 = []
year_3 = []
year_4 = []
year_5 = []
year_6 = []
year_7 = []
year_8 = []
year_9 = []
year_10 = []
year_11 = []
year_12 = []
year_13 = []
 
def add_student():
    student_number = int(input("Enter the number of student you want to add: "))
    for i in range (student_number):
     student_name = input(f"Enter student number {i + 1}'s name: ")
     student_id = input("Enter student ID: ")
     student_class = input("Enter student year: ")
     if student_id in id:
         print("Student ID already exists. Please try again.")
         return
    student = {}
    student[student_name] = student_id
    students.append(student)
def view_students():
   new_students= students
   print(new_students)   
def view_students_by_id():      
    student_id = input("Enter student ID: ")
    for student in students:
         if student_id in student.values():
              print(student)
              return
    print("Student not found.")
def check_if_student_exists():
    student_id = input("Enter student ID:")
    if student_id in id:
       print("Print student exists.")
    else:
       print("Student does not exist.")
def check_if_student_exist_in_class():
   check_student_id = input("Enter student ID: ")
   check_student_class = input("Enter student year:")
   if check_student_id in check_student_class.values():
    print("Student exists")
   else:
    print("Student does not exist.")     
def add_subject():
   new_subject = input("Enter subject name: ")
   subjects.append(new_subject)
   if new_subject in subjects:
      print("Subject already exits. Please try again.")
   else:
      print("Subject added successfully.")
def check_number_of_subjects():
   number_of_subjects = len(subjects)
   print("Total number of subjects:", number_of_subjects)
   print("And those subjects are,", subjects)
def view_subjects():  
   new_subjects = subjects
   print(new_subjects) 
def assign_subject_to_student():
   students_grades = {}
   assign_student_number = int(input("Enter the number of students you want to assign subjects to: "))
   for i in range (assign_student_number): 
    assign_student_id = input("Enter student ID: ")
    assign_subject_name = input("Enter subject name: ") 
    students_grades[assign_student_id] = assign_subject_name
    grades.append(students_grades)
def add_teacher():
   teacher_name = input("Enter teacher name: ")
   teacher_id = input("Enter teacher ID: ")
   teacher_subject = input("Enter subject taught by the teacher: ")
   teacher = {}
   number_of_teachers = int(input("Enter the number of teachers you want to add: "))
   for i in range (number_of_teachers):
    teacher[teacher_name] = teacher_id
    teachers.append(teacher) 
def view_teachers():
   new_teachers = teachers
   print(new_teachers)  
def add_or_update_grade():
    student_id_for_grade = input("Enter student ID: ")
    subject_for_grade = input("Enter subject name: ")
    grade_value = input("Enter grade: ")
    grade_entry = {
        'student_id': student_id_for_grade,
        'subject': subject_for_grade,
        'grade': grade_value
    }
    grades.append(grade_entry)
def view_grades(): 
    new_grades = grades
    print(new_grades)    
def caculate_average_grade():
    student_id_for_average = input("Enter student ID: ")
    total = 0
    count = 0   
    for grade_entry in grades:
        if grade_entry['student_id'] == student_id_for_average:
            total += float(grade_entry['grade'])
            count += 1
    if count > 0:
        average = total / count
        print(f"Average grade for student ID {student_id_for_average}: {average}")
    else:
        print("No grades found for the given student ID.")
def generate_report():
    student_id_for_report = input("Enter student ID: ")
    print(f"Report for student ID {student_id_for_report}:")
    for grade_entry in grades:
        if grade_entry['student_id'] == student_id_for_report:
            print(f"Subject: {grade_entry['subject']}, Grade: {grade_entry['grade']}")    
print("Welcome to the school management system")
print("This system helps manage students grades, subjects, teachers, grades and reports")
print("If you want to exit, just enter exit below else write continue to continue")
answer_1 = input("Enter: ")
while answer_1.lower() != "exit":
     print("1- Student management")
     print("2-Subject management")
     print("3- Teacher management")
     print("4- Grades management")
     print("5- Reports")
     choice = input("Enter your choice: ")
     if choice == "1":
        print("Welcome to student management section")
        print("1-Add student")
        print("2-View students")
        print("3-View student by ID")  
        print("4-Check if student exists")
        print("5-Check if student exists in class")
        student_choice = input("Enter your choice: ")
        if student_choice == "1":
           add_student()
        elif student_choice == "2":
           view_students()
        elif student_choice == "3":
           view_students_by_id()
        elif student_choice == "4":
           check_if_student_exists()
        elif student_choice == "5":
           check_if_student_exist_in_class()
     elif choice == "2":
        print("Welcome to subject managemnt section")
        print("1-Add subject")
        print("2-Check number of subjects")
        print("3-View subjects")
        print("4-Assign subject to student")
        subject_choice = input("Enter your choice: ")
        if subject_choice == "1":
           add_subject()
        elif subject_choice == "2":
           check_number_of_subjects()
        elif subject_choice == "3":
           view_subjects()
        elif subject_choice == "4":
           assign_subject_to_student()
     elif choice == "3":
        print("Welcome to teacher ,management section")
        print("1-Add teacher")
        print("2-View teachers")
        teacher_choice = input("Enter your choice: ")
        if teacher_choice == "1":
           add_teacher()
        elif teacher_choice == "2":
           view_teachers()
        else:
          print("Invalid choice,please try again")       
     elif choice == "4":
        print("Welcome to grades management section")
        print("1-Add or update grade")
        print("2-View grades")
        print("3-Calculate average grade")
        print("4-Generate report")
        grades_choice = input("Enter your choice: ")
        if grades_choice == "1":
           add_or_update_grade()
        elif grades_choice == "2":
           view_grades()
        elif grades_choice == "3":
           caculate_average_grade()
        elif grades_choice == "4":
           generate_report()
        else:
          print("Invalid choice,please try again")
     else:
        print("Invalid choice,please try again") 
        
