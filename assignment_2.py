import random

amount = random.randint(0,20) + round( random.randint(0,100)/100, 2 )

print (amount)

payment = int(input("enter what you are paying: "))

change = round(payment - amount, 2)

print (change)

if change > 0:
    d = 0
    q = 0
    i = 0
    n = 0
    d = change // 1
    change = change - d

    q = change // .25
    change = change - q*.25
    i = change // .10
    change = change - i*.10
    n = change // .05
    change = change - n*.05
    n = n + round(change*2,1)*10
    print ("you got" ,d, "dollars",q, "quarters",i,"dimes",n,"nickles back in change")
    
    
        
        
        
    

