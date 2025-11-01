import random

print('-'*175)
print('WORD SCRAMBLE GAME'.center(175))
print('-'*175)
list1= ['apple','banana','orange','grapes','kiwi','python','java','mister','miser','gravity','loop','dam','misery']
a= random.choice(list1)
l=[]
for i in a:
    l.append(i)
random.shuffle(l)

s=''
for i in l:
    s=s+i
print('Arrange the word:',s)
b=input("enter your word:")
if b==a:
    print(f'YOU WIN!!! \n The word is {a}')
else:
    print(f'YOU LOSE!!! \n The word is {a}')
