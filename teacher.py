# Payton Sales
# 5 / 5 / 26
# SDEV220 Final Project
# teacher.py

# Subclass inherits from User()


from user import User

class Teacher(User):

    # Create teacher profile from User() entry
    def __init__(self, username, password):
        super().__init__(username, password)

    # Add grade to student profile (Must exist)
    def add_grade(self, gradebook):

        student_username = input("Enter student's username: ")
        assignment = input("Enter the name of the assignment: ")
        grade = input("Enter the grade earned: ")

        # Save logged info to gradebook() student profile
        success = gradebook.save_grade(student_username, assignment, grade)

        if success:
            print("\nGrades were updated successfully. ")
        else:
            print("\nThis student does not have a profile. ")