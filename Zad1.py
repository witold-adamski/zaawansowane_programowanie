class Student:
    def __init__(self, name: str, marks: int):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        return True if self.marks > 50 else False


student1 = Student('Adam', 99)
student2 = Student('Anna', 48)

print(student1.is_passed())
print(student2.is_passed())
