class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        average_marks = sum(self.marks) / len(self.marks)
        return average_marks > 50
    
student1 = Student("Witold", [60, 70, 80])
student2 = Student("Natalia", [40, 45, 55])

print(f"{student1.name} passed: {student1.is_passed()}")
print(f"{student2.name} passed: {student2.is_passed()}")