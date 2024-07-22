print("Welcome to Tip Calculator")
bill = float(input("what is your total bill?"))
tip = input("how much tip would you like to give? 10, 12 or 15?")
tip_int =int(tip)
people = int(input("How many people to split the bill?"))
tip_percentage = tip_int / 100
bill_tip = bill * tip_percentage
total_bill = bill + bill_tip
each_one = total_bill / people
final_bill_one = round(each_one)
print(f"Your bill after tip aded is {total_bill}, And each person should give {final_bill_one}")