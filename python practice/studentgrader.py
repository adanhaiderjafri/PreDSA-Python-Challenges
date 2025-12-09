def grade_student(name,score,passing_marks=40):
    if score > passing_marks:
        print(f"{name} PASSED with {score}")
    else:
        print(f"{name} FAILED with {score}")
grade_student("adan",44)
grade_student("fatima",22)