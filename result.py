def process_student_results(student_id, student_name, subject_marks,
                            attendance_percentage,
                            assignment_score,
                            extracurricular_points):
    total_marks = sum(subject_marks.values())
    average = total_marks / len(subject_marks)
    average += assignment_score * 0.10
    average += extracurricular_points
    if attendance_percentage < 75:
        average -= 5
        attendance_status = "Attendance Below 75% (-5 Marks)"
    else:
        attendance_status = "Good Attendance"
    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "Fail"
    failed_subjects = []

    for subject, marks in subject_marks.items():
        if marks < 35:
            failed_subjects.append(subject)
    if len(failed_subjects) == 0:
        result = "Pass"
    else:
        result = "Fail"
    return {
        "Student ID": student_id,
        "Student Name": student_name,
        "Total Marks": total_marks,
        "Average": round(average, 2),
        "Grade": grade,
        "Attendance Status": attendance_status,
        "Failed Subjects": failed_subjects,
        "Result": result
    }

student_id = 1001
student_name = "Alex"

subject_marks = {
    "Math": 95,
    "Science": 88,
    "English": 76,
    "Computer": 92,
    "Physics": 34
}

attendance_percentage = 82
assignment_score = 18
extracurricular_points = 3
report = process_student_results(
    student_id,
    student_name,
    subject_marks,
    attendance_percentage,
    assignment_score,
    extracurricular_points
)
print("=" * 40)
print("STUDENT RESULT REPORT")
print("=" * 40)

for key, value in report.items():
    print(f"{key}: {value}")