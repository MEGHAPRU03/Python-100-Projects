#guess the word game
import random
print('Guess The Word Game'.center(175,'-'),end='\n')
print('The game starts now!!')
a= {'python' : 'The famous dangerous snake but everyone started using it.',
    'instagram' : 'Which gram is measured in mb \'s ?',
    'age': 'what can grow but never fall?',
'moustache' : 'What ache does a guy has?',
    'nuts': 'what drives someone?'}
word= random.choice(list(a.keys())).lower()
print(f'Here comes the HINT!! \n HINT: {a[word]} ')

for i in range(3,0,-1):
    user_input = input().lower()
    if(user_input==word):
        print(f'You guessed the word!! \n The word is {word}')
        break
    else:
        i=i-1
        print(f'Retry bro!! \n You have {i} attempts left')



