import pandas as pd

class Student:
    def __init__(self, first_name, last_name, birth_date, transcript):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.transcript = transcript

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"

class Transcript:
    def __init__(self, subject, exam_date, teacher):
        self.subject = subject
        self.exam_date = exam_date
        self.teacher = teacher

    def __repr__(self):
        return f"{self.subject}, {self.exam_date}, {self.teacher}"

def create_student_group(num_students):
    students = []
    for i in range(num_students):
        first_name = f"First{i+1}"
        last_name = f"Last{i+1}"
        birth_date = f"2000-01-01"  # You can customize the birth date format
        transcript = Transcript("Math", "2023-05-01", "Teacher1")
        student = Student(first_name, last_name, birth_date, transcript)
        students.append(student)
    return students

def print_teacher_table(teachers):
    df = pd.DataFrame(teachers, columns=["Teacher"])
    print(df)

def main():
    num_students = 5
    students = create_student_group(num_students)

    teachers = ["Teacher1", "Teacher2", "Teacher3"]
    print("Teacher Table:")
    print_teacher_table(teachers)

    for student in students:
        print(f"\nStudent: {student}")
        for transcript in student.transcript:
            print(f"  {transcript}")

if __name__ == "__main__":
    main()