
def prime_eratosthenes(integer):
    num_list = []
    x = 0
    for num in range(2, integer +1):
        num_list.append(num)   
    for num in num_list:
        for num in num_list:
            if (num_list[x])!= num and num % (num_list[x])== 0:
                num_list.remove(num)
        x = x + 1 
        
                    
    print (num_list)

    


integer = int(input("Enter a number greater than or equal to 100: "))
prime_eratosthenes(integer)


