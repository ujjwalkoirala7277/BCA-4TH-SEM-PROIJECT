# Develop a simple OOP-based Python class Student with attributes like name, roll
# number, and marks. Implement methods to input and display details.
class Student:
    def __init__(self):
        self.name = ""
        self.roll = 0
        self.marks = 0

    def input_details(self):
        self.name = input("Enter Name: ")
        self.roll = int(input("Enter Roll Number: "))
        self.marks = float(input("Enter Marks: "))

    def display_details(self):
        print("\nStudent Details")
        print("Name:", self.name)
        print("Roll Number:", self.roll)
        print("Marks:", self.marks)



s1 = Student()


s1.input_details()
s1.display_details()