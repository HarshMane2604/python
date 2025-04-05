score = int(input("Please Enter your score: "))
Grade = ''
if score >= 90 and score <= 100:
    Grade = 'A'
elif score >= 80 and score <= 89:
    Grade = 'B'
elif score >= 70 and score <= 79:
    Grade = 'C'
elif score >= 60 and score <= 69:
    Grade = 'D'
else:
    Grade = 'F'

print("Grade: ", Grade)
    

