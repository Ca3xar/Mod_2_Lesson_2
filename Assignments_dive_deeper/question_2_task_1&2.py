number1 = float(input("enter the first number: "))
number2 = float(input("enter the second number: "))
number3 = float(input("enter the third number: "))

largest = number3
smallest = number1

if number2 > largest:
    largest = number2
elif number1 > largest:
    largest = number1
elif number2 < smallest:
    smallest = number2
elif number3 < smallest:
    smallest = number3
print("The largest number is:", largest,"the smallest number is: smallest")