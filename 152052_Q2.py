class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def get_average_grade(self):
        if not self.grades:
            return 0.0
        return sum(self.grades.values()) / len(self.grades)

    def __str__(self):
        return f"Name: {self.name}, Grades: {self.grades}"

class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, name):
        student = Student(name)
        self.students.append(student)
        print(f"Student '{name}' added successfully.\n")

    def display_students(self):
        if not self.students:
            print("No students in the class.\n")
        else:
            print("List of Students:")
            for student in self.students:
                print(student)
            print()

    def get_student_average(self, name):
        found = False
        for student in self.students:
            if student.name.lower() == name.lower():
                average_grade = student.get_average_grade()
                print(f"Average grade for {student.name}: {average_grade:.2f}\n")
                found = True
                break
        if not found:
            print(f"Student '{name}' not found.\n")

    def get_class_average_subject(self, subject):
        total = 0
        count = 0
        for student in self.students:
            if subject in student.grades:
                total += student.grades[subject]
                count += 1
        if count > 0:
            class_average = total / count
            print(f"Class average for '{subject}': {class_average:.2f}\n")
        else:
            print(f"No students have grades for '{subject}'.\n")

def main():
    class_room = Classroom()

    # Adding students
    class_room.add_student("Alice")
    class_room.students[0].add_grade("Math", 85)
    class_room.students[0].add_grade("Science", 90)

    class_room.add_student("Bob")
    class_room.students[1].add_grade("Math", 75)
    class_room.students[1].add_grade("Science", 80)

    class_room.add_student("Carol")
    class_room.students[2].add_grade("Math", 90)
    class_room.students[2].add_grade("Science", 85)

    # Displaying all students
    class_room.display_students()

    # Getting average grade of a student
    class_room.get_student_average("Alice")

    # Getting class average for a subject
    class_room.get_class_average_subject("Math")
    class_room.get_class_average_subject("Science")
    class_room.get_class_average_subject("History")

if __name__ == "__main__":
    main()
