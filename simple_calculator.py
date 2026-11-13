try:
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
except ValueError:
    print("Error: Please enter valid numbers.")
    raise SystemExit
operation = input("Choose an operation (+, -, *, /): ")
# Add the numbers when the user chooses +.
if operation == "+":
    result = first_number + second_number
    print(f"{first_number:g} + {second_number:g} = {result:g}")
elif operation == "-":
    result = first_number - second_number
    print(f"{first_number:g} - {second_number:g} = {result:g}") 
elif operation == "*":
    result = first_number * second_number
    print(f"{first_number:g} * {second_number:g} = {result:g}")
elif operation == "/":
    if second_number == 0:
        print("Error: Cannot divide by zero.")
    else:
        result = first_number / second_number
        print(f"{first_number:g} / {second_number:g} = {result:g}") 
else:
    print("Error: Choose +, -, *, or /.")    
