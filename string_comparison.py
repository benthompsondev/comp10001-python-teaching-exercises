#filename: string comparison.py
# Ben Thompson, COMP 10001 Programming Fundamentals

school = "Mohawk College"
data = input("Enter a string to compare with: ")
if data == school:
    print("same " + data + " equals " + school)

if data.lower() == school.lower():
    print("case insensitive " + data, " and " + school)

if data in school:
    print("found " + data + " in " + school)


