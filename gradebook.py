# Payton Sales
# 5 / 5 / 26
# SDEV220 Final Project
# gradebook.py

# Read / Write user info from / to files
# Handles users / grades

# Pull student, teacher, gradebook classes
from student import Student
from teacher import Teacher


class Gradebook:

    # Read / Load all users with existing profiles
    def __init__(self):
        self.students = []
        self.teachers = []
        self.load_users()

    def load_users(self):


        try:
            # Open users.txt file
            file = open("users.txt", "r")

            for line in file:

                # .txt File text management
                data = line.strip().split(",")

                role = data[0]
                username = data[1]
                password = data[2]

                # Create the student / teacher object
                if role == "student":
                    student = Student(username, password)
                    self.students.append(student)
                    
                elif role == "teacher":
                    teacher = Teacher(username, password)
                    self.teachers.append(teacher)

            # Close users.txt file
            file.close()

        except FileNotFoundError:
            pass

    # Add user profile
    def register_user(self, role):

        username = input("Create a username: ")
        password = input("Create a password: ")

        # Check for duplicate profile
        for student in self.students:
            if student.username == username:
                print("\nThat username already exists.. ")
                return

        for teacher in self.teachers:
            if teacher.username == username:
                print("\nThat username already exists.. ")
                return


        # User object for student / teacher
        if role == "student":
            user = Student(username, password)
            self.students.append(user)

        elif role == "teacher":
            user = Teacher(username, password)
            self.teachers.append(user)

        # Open users.txt for {user},{pass}
        file = open("users.txt", "a")
        # Save to file
        file.write(f"{role},{username},{password}")
        file.close()

        print("\nThe profile was successfully created. ")

    # User login
    def login(self):

        username = input("Input Username: ")
        password = input("Input Password: ")

        # Check student login credentials
        for student in self.students:

            if (student.username == username and student.password == password):
                print("\nStudent has logged in successfully \n")
                return student
        
        # Check teacher login credentials
        for teacher in self.teachers:

            if (teacher.username == username and teacher.password == password):
                print("\nTeacher has logged in successfully \n")
                return teacher
            
        print("\nLogin credentials were invalid / Profile not made \n")
        return None

    # Save grades
    def save_grade(self, username, assignment, grade):

        student_exists = False

        for student in self.students:
            if student.username == username:
                student_exists = True

        if not student_exists:
            return False
        
        # Open grades.txt file
        file = open("grades.txt", "a")

        # Save to file
        file.write(f"{username},{assignment},{grade}\n")

        # Close grades.txt file
        file.close()
        return True

    # View saved grades
    def get_student_grades(self, username):

        grades = []

        try:
            # Open grades.txt file
            file = open("grades.txt", "r")

            for line in file:
                # .txt File text management
                data = line.strip().split(",")

                if len(data) == 3:
                    saved_username = data[0]
                    assignment = data[1]
                    grade = data[2]

                    if saved_username == username:
                        grades.append((assignment, grade))

            # Close grades.txt file
            file.close()
        
        except FileNotFoundError:
            pass
        return grades
                