# guess the random number
from auth.register import register
from features.account import account, hight_score
from features.manu import manu_list
var = True
while var:
    manu_list()
    choice = input("Choose the option: ")
    if choice == '1':
        # check user
        register()
    elif choice == '2':
        account()
    elif choice == '3':
        hight_score()
    elif choice == '4' or 'sop':
        var = False
        print("Exiting ........")
