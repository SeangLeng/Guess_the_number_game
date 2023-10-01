# guess the random number
import sys
from auth.register import register
from features.account import account, hight_score
from features.manu import manu_list
var = True
while var:
    global choice
    manu_list()
    try:
        choice = input("Choose the option: ")
    except ValueError:
        print("Enter the value please!!")

    if choice == '1':
        # check user
        register()
    elif choice == '2':
        account()
    elif choice == '3':
        hight_score()
    elif choice == '4' or 'sop':
        print("Exiting ........")
        sys.exit()

