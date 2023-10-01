from auth.register import logged
from options.game import user_score
from storage.data_storage import user


def account():
    if user:
        for user_info in user:
            print(f"Email: {user_info.email}")
            print(f"Phone number: {user_info.phone_number}")
            last_index = len(user_score) - 1
            if last_index >= 0:
                print(f"Money: {user_info.money}")
                print(f"Score: {user_score[last_index]}")
            else:
                print("No Money available.")
                print("No scores available.")
    else:
        print("Opp! please register !")
    input()