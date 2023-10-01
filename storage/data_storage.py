import json

user = []
class user_info:
    def __init__(self, email, phone_number, password, high_score, money):
        self.email = email
        self.phone_number = phone_number
        self.password = password
        self.high_score = high_score
        self.money = money

def save_account():
    data = {
        "users": []
    }
    for users in user:
        user_data = {
            "email": users.email,
            "phone_number": users.phone_number,
            "password": users.password,
            "high_score": users.high_score
        }
        data["users"].append(user_data)

    with open("user_score.json", "w") as file:
        json.dump(data, file)
