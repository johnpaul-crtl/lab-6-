age = int(input("Enter your age:"))
member = input("are you a member? (yes/no):")

if age < 18:
    if member == "Yes":
        fee = 450
    else:
        fee = 650
elif 18 <= age  <= 65:
    if member == "yes":
        fee = 550
    else:
        fee = 750
elif age > 65:
    if member == "No":
        fee = 400
    else:
        fee = 600
else:
    fee = None
    
if fee is not None:
    print(f"the registration fee is {fee} pesos.")
else:
    print("invalid input.")
    
