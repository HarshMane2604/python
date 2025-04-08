distance = int(input("Enter distance you want to walk "))
if distance < 3:
    print("Go by walk")
elif distance <= 15:
    print("you can use bike")
else:
    print("you can use car")