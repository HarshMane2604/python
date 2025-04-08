order_size = input("Enter your order size \"Small\", \"Medium\" or \"Large\"")
order_size = order_size.lower()
extra_shot = True

if extra_shot:
    coffee = order_size + "Coffee with an extra shot" 
else:
    coffee = order_size + "coffee"

print(coffee)