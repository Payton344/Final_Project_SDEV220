# Payton Sales
# 5 / 5 / 26
# SDEV220 Final Project
# user.py

# Superclass for every user

class User:

    # Create profile with username and password
    def __init__(self, username, password):
        self.username = username
        self.password = password