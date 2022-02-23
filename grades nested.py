
# Grading Scheme with nested statements:  
# Letter Grade Numerical Grade  
# A 90% or better  
# B 80%-89%  
# C 70%-79%  
# D 60%-69%  
# F < 60%  
# assign a percentage to num_grade num_grade = 99  

num_grade = float(input("enter your grade: "))
 
if num_grade >= 90:  
    let_grade = "A"  
else:  
    if num_grade >= 80:  
        let_grade = "B"  
    else:  
        if num_grade >= 70:  
            let_grade = "C"  
        else:  
            if num_grade >= 60:  
                let_grade = "D"  
            else:  
                let_grade = "F"  

print(let_grade)

 
