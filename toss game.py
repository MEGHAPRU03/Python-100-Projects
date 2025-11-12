import random
print('Toss Game'.center(175,'-'))
l1=['heads','tails']
def toss_a_coin():
    user_choice=input('Choose heads or tails :').strip().lower()
    computer_choice=random.choice(l1)
    if computer_choice==user_choice:
        print('You won the toss!!')
    else:
        print('You lost the toss!!')
    val = input('Do you want to play again?').strip().lower()
    if val == 'yes':
        toss_a_coin()
toss_a_coin()

