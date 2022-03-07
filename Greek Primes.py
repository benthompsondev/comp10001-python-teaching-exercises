
def prime_eratosthenes(integer):
    num_list = []
    for num in range(2, integer +1):
        num_list.append(num)   
    for num in num_list:
        if (num_list[0])!= num and num % (num_list[0])== 0:
            num_list.remove(num)
    for num in num_list:
        if (num_list[1])!= num and num % (num_list[1])== 0:
            num_list.remove(num)
    for num in num_list:
        if (num_list[2])!= num and num % (num_list[2])== 0:
            num_list.remove(num)
    for num in num_list:
        if (num_list[3])!= num and num % (num_list[3])== 0:
            num_list.remove(num)
    for num in num_list:
        if (num_list[4])!= num and num % (num_list[4])== 0:
            num_list.remove(num)
    for num in num_list:
        if (num_list[5])!= num and num % (num_list[5])== 0:
            num_list.remove(num)

    for num in num_list:
        if (num_list[6])!= num and num % (num_list[6])== 0:
            num_list.remove(num)
    for num in num_list:
        if (num_list[7])!= num and num % (num_list[7])== 0:
            num_list.remove(num)
    for num in num_list:
        if (num_list[8])!= num and num % (num_list[8])== 0:
            num_list.remove(num)
    for num in num_list:
        if (num_list[9])!= num and num % (num_list[9])== 0:
            num_list.remove(num)

    for num in num_list:
        if (num_list[10])!= num and num % (num_list[10])== 0:
            num_list.remove(num)

        
                    
    print (num_list)

    
#Tried many different methods including del[1::2], del[2::3] so on so forth
    # Im super confused / stuck on this assignment

integer = int(input("Enter a number greater than or equal to 100: "))
prime_eratosthenes(integer)


