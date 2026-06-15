#  Implement a program to store student records (name, roll, marks,contact number) using a
# dictionary.
# a. Provide menu options to add, search, and display students
def stu_operations():
    students = {}
    while True:
        print("\n")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Display All Students")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            roll = input("Enter Roll Number: ")

            if roll in students:
                print("Student with this roll number already exists!")
            else:
                name = input("Enter Name: ")
                marks = int(input("Enter Marks: "))
                contact = input("Enter Contact Number: ")

                students[roll] = {
                    "Name": name,
                    "Marks": marks,
                    "Contact": contact
                }

                print("Student record added successfully!")

        elif choice == "2":
            roll = input("Enter Roll Number to search: ")

            if roll in students:
                print("\nStudent Found:")
                print(f"Roll No: {roll}")
                print(f"Name: {students[roll]['Name']}")
                print(f"Marks: {students[roll]['Marks']}")
                print(f"Contact: {students[roll]['Contact']}")
            else:
                print("Student not found!")

        elif choice == "3":
            if not students:
                print("No student records available.")
            else:

                for roll, details in students.items():
                    print(f"\nRoll No: {roll}")
                    print(f"Name: {details['Name']}")
                    print(f"Marks: {details['Marks']}")
                    print(f"Contact: {details['Contact']}")

        elif choice == "4":
            print("Exited")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ =="__main__":
    stu_operations()