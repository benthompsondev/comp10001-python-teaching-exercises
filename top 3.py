def top_three_avg(grade1, grade2, grade3, grade4):
 total = grade1 + grade2 + grade3 + grade4
 top_three = total - min(grade1, grade2, grade3, grade4)
 return top_three / 3


#assume the user enters a number

grade1= int(input("Enter a grade: "))
grade2= int(input("Enter another grade: "))
grade3= int(input("Enter another grade: "))
grade4= int(input("Enter another grade: "))


print ("the average of the best 3 grades is: ", top_three_avg(grade1, grade2, grade3, grade4))
