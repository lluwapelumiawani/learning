class Student:
    def __init__(self, name):
        self.name = name
        self.scores = {} 

    def add_score(self, subject, score):
        self.scores[subject] = score

    def average_score(self):
        if not self.scores:
            return 0
        return sum(self.scores.values()) / len(self.scores)

    def get_grade(self):
        avg = self.average_score()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        elif avg >= 50:
            return 'E'
        else:
            return 'F'

    def __str__(self):
        return f"{self.name} | Avg: {self.average_score():.2f} | Grade: {self.get_grade()}"


class School:
    def __init__(self):
        self.students = []

    def register_student(self, name):
        self.students.append(Student(name))
        print(f"Student '{name}' registered successfully.")

    def record_score(self, name, subject, score):
        for student in self.students:
            if student.name == name:
                student.add_score(subject, score)
                print(f"Score recorded for {name} - {subject}: {score}")
                return
        print(f"Student '{name}' not found.")

    def display_all_grades(self):
        print("\nFinal Report:")
        for student in self.students:
            print(student)


school = School()

school.register_student("Dave")
school.register_student("Pelzy")
school.register_student("Papi")

school.record_score("Dave", "Math", 92)
school.record_score("Dave", "English", 85)
school.record_score("Pelzy", "Math", 74)
school.record_score("Pelzy", "English", 68)
school.record_score("Papi", "Math", 56)
school.record_score("Papi", "English", 45)

school.display_all_grades()