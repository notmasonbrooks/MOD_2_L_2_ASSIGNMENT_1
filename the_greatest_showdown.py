num1 = int(input("Enter your first number.\n"))
num2 = int(input("Enter your second number.\n"))
num3 = int(input("Enter your third number.\n"))

if num1 >= num2 and num1 >= num3:
    print(f"{num1} is the largest number!")
elif num2 >= num1 and num2 >= num3:
    print(f"{num2} is the largest number!")
else:
    print(f"{num3} is the largest number!")

if num1 <= num2 and num1 <= num3:
    print(f"{num1} is the smallest number!")
elif num2 <= num1 and num2 <= num3:
    print(f"{num2} is the smallest number!")
else:
    print(f"{num3} is the smallest number!")
