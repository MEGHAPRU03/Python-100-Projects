from datetime import datetime, date

dob = datetime.strptime(input("Enter DOB (dd/mm/yyyy): "), "%d/%m/%Y").date()
today = date.today()

# Years
years = today.year - dob.year
if (today.month, today.day) < (dob.month, dob.day):
    years -= 1

# Months
months = today.month - dob.month
if today.day < dob.day:
    months -= 1
if months < 0:
    months += 12

# Days
if today.day >= dob.day:
    days = today.day - dob.day
else:
    # previous month days
    prev_month = today.month - 1 or 12
    prev_year = today.year if today.month != 1 else today.year - 1
    days_in_prev_month = (date(prev_year, prev_month + 1, 1) - date(prev_year, prev_month, 1)).days
    days = today.day + days_in_prev_month - dob.day

print(f"Your Age: {years} years, {months} months, {days} days")
