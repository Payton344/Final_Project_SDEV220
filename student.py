# Payton Sales
# 5 / 5 / 26
# SDEV220 Final Project
# student.py

# Subclass inherits from User()


from user import User

class Student(User):

    # Create student profile from User() entry
    def __init__(self, username, password):
        super().__init__(username, password)

    # Access gradebook() for saved grades
    def view_grade(self, gradebook):

        grades = gradebook.get_student_grades(self.username)

        # Check/Call grades
        if len(grades) == 0:
            print("\nNo grades could be found.. ")

        else:
            print("\nHere are the grades: ")

        # Display all logged grades from gradebook()
            for assignment, grade in grades:
                print(f"{assignment}: {grade}")

            print()