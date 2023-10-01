import random
import re

from storage.data_storage import user

result = 0
user_score = []
win = True

def game():
    global result, name, user_score, win, choose
    choice = []
    win = True
    while win:
        print("--------------- Guess the number ------------------")
        print("            Guess the number                       \n")
        result = random.randrange(0, 1000)
        answer_sheet = result
        index = random.randrange(0, len(choice) + 1)
        choice.insert(index, answer_sheet)
        choice.insert(index, answer_sheet - random.randrange(5, 100))
        choice.insert(index, answer_sheet + random.randrange(100, 150))
        random.shuffle(choice)
        for i, num in enumerate(choice):
            print(num, end=' ')
        try:
            choose = int(input("\nChoose the answer: "))
            if choose in choice and choose == answer_sheet:
                for users in user:
                    users.high_score += 10
                    users.money += 0.205
                    name = users.email
                    user_score.append(users.high_score)
                choice.clear()
                print("You are correct! Congratulations", name)
                for users in user:
                    print("You have", users.high_score, "score")
                    print("You have $", users.money)
                win = True
            else:
                choice.clear()
                for users in user:
                    users.high_score -= 10
                    users.money -= 0.105
                    if users.high_score <= 0:
                        users.high_score = 0
                    if users.money <= 0:
                        users.money = 0
                    user_score.append(users.high_score)
                    win = False
                print("Ahh! try again later!")
                input()
        except ValueError:
            print("Oop! Error input!!!")
            choice.clear()
            input()
    for users in user:
        print(f"You have {users.high_score} score")

    return
