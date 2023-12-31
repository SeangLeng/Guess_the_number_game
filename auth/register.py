import subprocess
import os
import re
from options.game import game
from storage.data_storage import user_info, user

logged = False


def validate_email(email):
    # Regular expression pattern for email validation
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def register():
    global logged
    if not logged:
        print("------------- Register Time ---------------")
        height_score = 0
        money = 0

        while True:
            email = input("1. Your email: ")
            if validate_email(email):
                break
            else:
                print("Invalid email format. Please enter a valid email.")

        while True:
            phone_number = input("2. Your phone number: ")
            if phone_number.isdigit() and len(phone_number) == 10 or len(phone_number)==9:
                break
            else:
                print("Invalid phone number. Please enter a valid number.")

        while True:
            password = input("3. Password: ")
            con_password = input("4. Confirm password: ")

            if password == con_password:
                new_user = user_info(email, phone_number, password, height_score, money)
                user.append(new_user)
                logged = True
                print("Thanks for your registration!")
                break
            else:
                print("Passwords do not match. Please try again.")
        input()
    else:
        login()


def login():
    global logged

    if not logged:
        print("----------------- Login ------------------")
        email = input("Your email or phone number: ")
        password = input("Your password: ")

        for user_obj in user:
            if (user_obj.email == email or user_obj.phone_number == email) and user_obj.password == password:
                print("Login successful!")
                logged = True
                return

        print("Invalid email/phone number or password. Please try again.")
    else:
        game()