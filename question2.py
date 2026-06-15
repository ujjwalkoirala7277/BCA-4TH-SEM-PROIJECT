# Create a program that takes a list of student names and stores them in a file. Then, read
# the file and display the contents.
def get_students():
    students = []

    n = int(input("Enter number of students: "))

    for i in range(n):
        students.append(input(f"Enter name of student {i+1}: "))

    with open("file.txt", "w") as f:
        for name in students:
            f.write(name + "\n")

    with open("file.txt", "r") as f:
        print("\nStudents name in file are:")
        print(f.read())


get_students()