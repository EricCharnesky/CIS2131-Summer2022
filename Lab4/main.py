TODAYS_DAY = 20
TODAYS_MONTH = 6
TODAYS_YEAR = 2022

day = 0
month = 0
year = 0

# doesn't work
#while day >= 1 and day <= 31:

#while day < 1 or day > 31:

while not (1 <= day <= 31):
    day = int(input("Enter the day of the month: 1-31 "))

while not (1 <= month <= 12):
    month = int(input("Enter the month: 1-12 "))

while not (2023 <= year <= 2099):
    year = int(input("Enter the year: 2023-2099 "))

days_until_date = 0


days_until_date = day - TODAYS_DAY

if month < TODAYS_MONTH:
    months = 12 - (TODAYS_MONTH - month)
    year -= 1
else:
    months = month - TODAYS_MONTH

days_until_date += int(months * 30.5)

days_until_date += 365 * (year - TODAYS_YEAR)

print(days_until_date, "days until your date ( approximately ) ")


for hour in range(24): # 0-23
    for minute in range(60): # 0-59
        for second in range(60): #0-59
            print(f'{hour:>02}:{minute:>02}:{second:>02}')
