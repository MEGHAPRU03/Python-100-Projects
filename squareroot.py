import math as m
print('SQUARE ROOT FINDER'.center(175,'-'))
def root_finder():
    inp = int(input("Enter a number:"))
    if inp >= 1:
        if inp == 1:
            print("The square root of 1 is 1.")
        else:
            print(f"The square root of {inp} is {m.sqrt(inp)}.")
    else:
        print('Enter a number greater than 1.')
    y = input("DO u want to play game again (yes/no)?").lower().strip()
    if y == "yes":
        root_finder()
    else:
        print('BYE')
        print('-'*175)


y=input("DO u want to play game(yes/no)?").lower().strip()
if y=="yes":
    root_finder()
else:
    print('thanks for visit')
    print('-'*175)

