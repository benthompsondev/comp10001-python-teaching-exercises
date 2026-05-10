#function that mimics the sum function with lists

list_numbers = []

def mySum():
    sumtotal = 0
    for x in range(5):
        number = float(input("Enter a number: "))
        sumtotal = sumtotal + number
        list_numbers.append(number)    

    list_numbers.sort()
    return sumtotal



print("Your sum is:" ,mySum(), "and here is your final list", list_numbers)      
