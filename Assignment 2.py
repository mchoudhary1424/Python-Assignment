# Program to calculate total marks and percentage

name = input("Enter Student Name: ")
student_class = input("Enter Class: ")

sub1 = float(input("Enter marks of Subject 1: "))
sub2 = float(input("Enter marks of Subject 2: "))
sub3 = float(input("Enter marks of Subject 3: "))
sub4 = float(input("Enter marks of Subject 4: "))
sub5 = float(input("Enter marks of Subject 5: "))

total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total / 500) * 100

print("\n----- RESULT -----")
print("Name       :", name)
print("Class      :", student_class)
print("Total Marks:", total)
print("Percentage :", percentage, "%")



Output --

Enter Student Name: Rahul
Enter Class: 10
Enter marks of Subject 1: 80
Enter marks of Subject 2: 75
Enter marks of Subject 3: 90
Enter marks of Subject 4: 85
Enter marks of Subject 5: 70

----- RESULT -----
Name       : Rahul
Class      : 10
Total Marks: 400
Percentage : 80.0 %
