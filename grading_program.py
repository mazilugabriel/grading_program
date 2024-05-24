student_score = {
    "Harry": 81,
    "John": 70,
    "Gabi": 10,
    "Draco": 82,
    "Neville": 10,
}
student_grades = {}

for student in student_score:
    score = student_score[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectation"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
print(student_grades)