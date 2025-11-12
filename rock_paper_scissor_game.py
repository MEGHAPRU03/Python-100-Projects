import random
print("Rock-Paper-Scissor Game".center(175,'-'))
name=input("Enter your name: ").upper()
l1=['rock','paper','scissor']
computer_score=0
user_score=0
for i in range(1,6,1):
    computer_choice = random.choice(l1)
    user_choice = input('Enter your choice: rock, paper, or scissor').lower().strip()
    print('Your choice:',user_choice)
    print('Computer choice:',computer_choice)
    if computer_choice==user_choice:
         print('Its a draw!!')
    elif computer_choice=='paper' and user_choice=='rock':
         print('Computer gets a point!!\n +1')
         computer_score=computer_score+1
    elif computer_choice=='rock' and user_choice=='paper':
        print(f'{name} gets a point!!\n +1')
        user_score=user_score+1
    elif computer_choice=='rock' and user_choice=='scissor':
        print(f'{name} gets a point!!\n +1')
        user_score = user_score + 1
    elif computer_choice=='scissor' and user_choice=='rock':
        print('Computer gets a point!!\n +1')
        computer_score = computer_score + 1
    elif computer_choice=='scissor' and user_choice=='paper':
        print('Computer gets a point!!\n +1')
        computer_score = computer_score + 1
    elif computer_choice=='paper' and user_choice=='scissor':
        print(f'{name} gets a point!!\n +1')
        user_score = user_score + 1

print('-'*175)
print('Paper Scissor Game'.center(55,'-'))
print('Player name:',name)
if user_score<computer_score:
    print('Computer wins!!')
elif user_score==computer_score:
    print('Draw!!')
else:
    print(f'{name} wins!!')
    print('Score:',user_score)
print('-'*175)




