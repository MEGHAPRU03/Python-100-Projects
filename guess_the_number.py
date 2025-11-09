import random
ui=int(input("Guess a number"))
sys_in=random.randint(1,100)
while(ui!=sys_in):
    if ui>sys_in:
        print('Too high!')
    elif ui<sys_in:
        print('Too low!')
    ui = int(input("Enter again"))
if ui == sys_in:
        print('You guessed the number right!')
