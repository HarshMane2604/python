age = int(input("Enter your age: "))
day = input("Enter the Day: ")
price = 12 if age >= 18 else 8

if day == "Wednesday":
    price -= 2

print("Ticket price for you is $", price)