def calcAverage (temps): 
    mySum = 0 
    for i in temps: 
        mySum = mySum + i 
    myAvg = mySum / len(temps) 
    return myAvg 

tempList = [] 

for x in range(5): 

    temp = float(input("Enter a temperature: ")) 

    tempList.append(temp) 

  

# calculates the average of the temperatures in the list the user made 

average = calcAverage(tempList) 

  

#print the result 

print("the average temperature is ", average) 

 
