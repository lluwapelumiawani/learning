
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


sum_result = num1 + num2
print(f"The sum of the numbers is: {sum_result}")


product_result = num1 * num2
print(f"The product of the numbers is: {product_result}")


if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num2 > num1:
    print(f"{num2} is greater than {num1}")
else:
    print("Both numbers are equal")


if num1 % 2 == 0 and num2 % 2 == 0:
    print("Both numbers are even.")
else:
    print("Both numbers are not even.")