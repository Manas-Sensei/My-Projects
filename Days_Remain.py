age = input("what is your age?")
age_in_int = int(age)
years = 90 - age_in_int
weeks = years * 52
weeks_in_int = int(weeks)
days = weeks_in_int * 7
print(f"You have {days} days left. Use it wisely.")