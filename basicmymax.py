#function that mimics the max function with lists

list_numbers = []

def myMax():
    for x in range(5):
        number = float(input("Enter a number: "))
        list_numbers.append(number)
        
    list_numbers.sort()
    return list_numbers[-1] 


print("Your max number is:" ,myMax(), "and here is your final list", list_numbers)      
