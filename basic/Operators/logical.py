is_student = True
marks = 45
has_sports_quota = False

# AND
if is_student and marks >= 40:
    print("You have passed the exam.")

# OR
if marks >= 40 or has_sports_quota:
    print("You are eligible for admission.")

# NOT
if not is_student:
    print("Student record not found.")