count = 0  

print("Numbers divisible by 3 from 1 to 100:")

for number in range(1, 100):
    if number % 3 == 0:
        print(number, end=" ")
        count += 1

print("\n\nTotal numbers divisible by 3:", count)