import datetime

dt = datetime.datetime.now();

name = input("What's your name?") 
product = input("What's do you want?") 
qty = int(input("How many?"))
price_per_unit = float(input("What is price per unit?"))

subtotal = qty * price_per_unit
tax_rate = 0.07
tax = subtotal * tax_rate
total = subtotal + tax

print(dt)
print("My name is", name)
print("I want ", product)
print("I want ", qty)
print("It's ",subtotal , "but not includes tax")
print("tax 7 %", tax)
print("It's cost",total )