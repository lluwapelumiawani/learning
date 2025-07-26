
name = input("Enter student name: ")
age = int(input("Enter student age: "))
score1 = float(input("Enter score for subject 1: "))
score2 = float(input("Enter score for subject 2: "))
score3 = float(input("Enter score for subject 3: "))


average = (score1 + score2 + score3) / 3


status = "Passed" if average >= 50 else "Failed"


print("\nStudent Profile Summary:\n")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Average Score: {round(average, 1)}")
print(f"Status: {status}") # type: ignore