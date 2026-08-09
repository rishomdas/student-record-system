print("       -:STUDENT RECORD:-")

name = input("Enter name: ")
age = input("Enter age: ")
dob = input("Enter date of birth: ")
date = input("Enter today's date: ")

file = open("student.txt", mode="a")

file.write("Name: ")
file.write(name)
file.write("\n")

file.write("Age: ")
file.write(age)
file.write("\n")

file.write("Date of Birth: ")
file.write(dob)
file.write("\n")

file.close()

file = open("log.txt", mode="a")

file.write("Student record added.\n")

file.write("Name: ")
file.write(name)
file.write("\n")

file.write("Date: ")
file.write(date)
file.write("\n")

file.close()

print()

print("Student record saved successfully.")

print("Log updated.")
