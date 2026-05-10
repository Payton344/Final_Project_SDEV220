# Payton Sales
# 5 / 5 / 26
# SDEV220 Final Project
# main.py

# Main program for interface

# Pull student, teacher, gradebook classes
from student import Student
from teacher import Teacher
from gradebook import Gradebook

# Teacher Grade Hub
def teacher_access(teacher, gradebook):

    # Loop Hub
    while True:

        print("\n-- Welcome to the Teacher Grade Hub --\n")
        print("Enter 1 to input grades")
        print("Enter 2 if you would like to log out")

        choice = input("Choose (1/2): ")

        if choice == "1":
            teacher.add_grade(gradebook)

        elif choice == "2":
            print()
            break

        else:
            print("\nInvalid input.. ")

# Student Grade Hub
def student_menu(student, gradebook):

    # Loop Hub
    while True:

        print("\n-- Welcome to the Student Grade Hub --\n")
        print("Enter 1 to view current grades")
        print("Enter 2 if you would like to log out")

        choice = input("Choose (1/2): ")

        if choice == "1":
            student.view_grade(gradebook)

        elif choice == "2":
            print()
            break

        else:
            print("\nInvalid input.. ")


# Main
def main():

    # Initialize Gradebook()
    gradebook = Gradebook()

# Loop until user exit
    while True:

        print("\n-- Welcome to the Central Grade Hub --\n")
        print("Enter 1 to login ")
        print("Enter 2 to register a new Teacher profile ")
        print("Enter 3 to register a new Student profile ")
        print("Enter 4 to exit the system ")

        choice = input("\nChoose (1/2/3/4): ")

        # Login
        if choice == "1":
            user = gradebook.login()
            if user is not None:

                # Takes Student/Teacher to appropriate Hub
                if isinstance(user, Teacher):
                    teacher_access(user,gradebook)
                elif isinstance(user, Student):
                    student_menu(user, gradebook)

        # Register Teacher
        elif choice == "2":
            gradebook.register_user("teacher")

        # Register Teacher
        elif choice == "3":
            gradebook.register_user("student")

        # User Exit
        elif choice == "4":
            print("\nYou have chosen to exit the program.. ")
            print("Program closed. Goodbye! \n")
            break

        else:
            print("\nInvalid input.. ")

main()