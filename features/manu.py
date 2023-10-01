from storage.data_storage import user


def manu_list():
    print("--------------------- Guess the number -----------------------")
    for user_info in user:
        print("Your high score:", user_info.high_score)
        print("Your Current money: $", user_info.money)
    print("1. Play game\n"
          "2. Account\n"
          "3. High score\n"
          "4. Exit the program")

