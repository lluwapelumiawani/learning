# Get user input
num1 = float(input("Enter the first number: "))
operator = input("Choose an operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

# Perform calculation based on operator
if operator == '+':
    result = num1 + num2
    print(f"Result: {result}")
elif operator == '-':
    result = num1 - num2
    print(f"Result: {result}")
elif operator == '*':
    result = num1 * num2
    print(f"Result: {result}")
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {result}")
    else:
        print("Error: Cannot divide by zero!")
else:
    print("Invalid operator!")


     # type: ignore