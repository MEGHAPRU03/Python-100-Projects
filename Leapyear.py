print('Check whether its a leap year or not?')

a=int(input("Enter a number:"))

if (a%4==0 and a%100!=0) or (a%400==0):
    print("Leap year")
else:
    print("Not a leap year")