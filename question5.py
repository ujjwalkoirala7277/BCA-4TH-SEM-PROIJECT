# Write Python code to read from a CSV file of student marks and calculate average marks
import csv

total_marks = 0
count = 0

with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
        total_marks += float(row["Marks"])
        count += 1

average = total_marks / count

print("Average Marks:", average)