def kmtomiles(km): 
    return(km / 1.6)  

       
kilom = float(input("enter an amount in kilometers: "))
#Assume user enters a number
               
miles = kmtomiles(kilom) 


print(kilom, "km converted to miles is:" ,miles,) 
