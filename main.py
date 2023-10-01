# guess the random number
from auth.register import register
from features.account import account
from features.manu import manu_list

while True:
    manu_list()
    choice = input("Choose the option: ")
    if choice == '1':
        # check user
        register()
    elif choice == '2':
        account()