def grade_score(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    elif 60 <= score <= 69:
        return "D"
    else:
        return "F"


for i in range(1, 6):
    score = int(input(f"Enter score #{i}: "))
    grade = grade_score(score)
    print ( f"Score: {score} → Grade: {grade}")