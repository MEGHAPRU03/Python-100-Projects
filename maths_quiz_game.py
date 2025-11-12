import random,time
print('MATHS QUIZ GAME'.center(175,'-'))
DIFFICULTIES = {
    "easy":    {"min": 1,   "max": 10,   "ops": ["+", "-"], "points": 2},
    "medium":  {"min": 10,   "max": 500,   "ops": ["+", "-", "*"], "points": 5},
    "hard":    {"min": 500,   "max": 2000,  "ops": ["+", "-", "*", "/"], "points": 10},
}

print("Welcome to the Maths Quiz Game!!")
name=input('What\'s your name?')
level= input('Enter difficulty level: easy, medium, hard').strip().lower()
cfg = DIFFICULTIES[level]
no_of_questions = int(input("How many questions would you like?"))

def operation(a,op,b):
    if op == "+":
        return a+b
    elif op == "-":
        return a-b
    elif op == "*":
        return a*b
    elif op == "/":
        return round(a/b,2)
    elif op == "^":
        return a**b
    else:
        return 0


score=0
correct=0
start_time =time.time()
for i in range(1,no_of_questions+1,1):
    op = random.choice(cfg["ops"])
    a = random.randint(cfg["min"], cfg["max"])
    b = random.randint(cfg["min"], cfg["max"])
    print(f'Question {i}/{no_of_questions}:{a} {op} {b}')
    ans=operation(a,op,b)
    user_answer=float(input("Your answer : "))
    if ans == user_answer:
        correct=correct+1
        score= score + cfg["points"]
        print("Correct!",cfg['points'])
    else:
        print("Incorrect!",0 ,'points')
end_time=time.time()
duration = round(end_time-start_time,2)
print('-'*175)
print('-----------Quiz Summary------------')
print('Player Name:',name.capitalize())
print("Difficulty Level:",level)
print("Correct answers:",correct)
print("Score :",score)
print("Time taken:",duration ,'seconds')
print('Accuracy:',correct/no_of_questions * 100,'%' )
percentage=(correct/no_of_questions)*100
if percentage<=33.33:
    print(f'Not a bad attempt {name}!!')
elif percentage>33.33 or percentage<=75:
    print(f'Great attempt {name}!!')
elif percentage>75:
    print(f'Excellent play {name}!! Well Done!!')
print('-'*175)






