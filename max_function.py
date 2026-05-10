#function that mimics the max function with lists

list_numbers = []

def myMax():
    while True:
        number = (input("Enter a integer or done to quit: "))
        number.lower()
        if number == "done":
            break
        else:
            if number.isdigit():
                newNumber = int(number)
                list_numbers.append(newNumber)
            else:
                print("You did not enter an integer please try again")
           
    list_numbers.sort()
    return list_numbers[-1] 


print("Your max number is:" ,myMax(), "and here is your final list", list_numbers)      
