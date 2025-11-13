import colorama as c
import random
print('Welcome to Dice Rolling Battle: Player vs Computer!'.center(175,'*'))
name=input('Enter your name: ')
def roll_dice():
    cscore =0
    u_score =0
    computer_choice=random.randint(1,6)
    user_choice=random.randint(1,6)
    print('Your dice value is: ',user_choice,'Computer dice value is: ',computer_choice)
    if computer_choice==user_choice:
        print("It’s a tie.")
    elif computer_choice>user_choice:
        print('Computer won')
        cscore+=1
    elif computer_choice<user_choice:
        print('You won')
        u_score+=1
    else:
        print('Invalid choice')
    take_input()




def take_input():
    opinion = input('Enter yes or no: ').strip().lower()
    if opinion == 'yes':
        roll_dice()
    else:
        print('-'*25)
        print('Thanks for playing!')
        print('-' * 25)
        exit(1)

take_input()







