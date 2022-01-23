def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())

    return lines


def avg(values):
    return sum(values) / len(values)


n = int(input())
student_grades_lines = input_to_list(n)
student_grades = {}

for line in student_grades_lines:
    student, grade = line.split(' ')
    if student not in student_grades:
        student_grades[student] = []
    student_grades[student].append(float(grade))

for el in student_grades.items():
    student, grade = el
    avg_grade = avg(grade)
    print(f"{student} -> {' '.join(map(lambda x: f'{x:.2f}', grade))} (avg: {avg_grade:.2f})")