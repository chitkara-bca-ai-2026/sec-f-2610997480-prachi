print("="*50)
print("             SCHOOL RESULT PROCESSING             ")
print("="*50)
student_name=input("Enter Student Name : ")
roll_num=int(input("Enter Roll Number  : "))
print()
print("--- Enter Marks for 5 Subjects (0-100) ---")
total_marks=0
has_failed=False
for i in range(1,6):
    marks=float(input(f"Enter marks for Subject {i}: "))
    if marks < 0 or marks >100:
        print("Error: Marks must be between 0 and 100.")
    if marks < 40:
        has_failed=True
    total_marks += marks
percentage=(total_marks / 500)*100
if has_failed:
    result="FAIL"
    grade="F"
    remark="Failed in one or more subjects."
else:
    result="PASS"
    if percentage >= 90:
        grade="A+"
        remark="Outstanding"
    elif percentage >= 80:
        grade="A+"
        remark="Excellent"
    elif percentage >= 70:
        grade="b"
        remark="Very Good"
    elif percentage >= 60:
        grade="C"
        remark="Good"
    elif percentage >= 50:
        grade="D"
        remark="Satisfactory"
    elif percentage >= 40:
        grade="E"
        remark="Pass"
    else:
        result="FAIL"
        grade="F"
        remark="Fail"
print()
print("="*50)
print("             STUDENT REPORT CARD                  ")
print("="*50)
print(f"Student Name : {student_name}")
print(f"Roll Number  : {roll_num}")
print("-"*50)
print(f"Total Marks  : {total_marks}/500.0")
print(f"Percentage   : {percentage:.2f}%")
print(f"Result       : {result}")
print(f"Grade        : {grade}")
print(f"Remarks      : {remark}")