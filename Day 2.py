
age = input("What is your current age?")
#
ages_as_int = int(age)

years_left = 90 - ages_as_int
days_left = years_left * 365
months_left = years_left * 12
weeks_left = years_left * 52

total = f"you have {years_left} years, {weeks_left} weeks,{months_left} months and {days_left}days left to live :) "

print(total)