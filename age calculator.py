from datetime import date
def calculate_age(birth_year, birth_month, birth_day):
    today = date.today()
    age = today.year - birth_year

    # If birthday hasn't happened yet this year, subtract 1
    if (today.month, today.day) < (birth_month, birth_day):
        age -= 1

    return age

# Input
by = int(input("Enter your birth year: "))
bm = int(input("Enter your birth month: "))
bd = int(input("Enter your birth day: "))

print("Your Age is:", calculate_age(by, bm, bd), "years")
