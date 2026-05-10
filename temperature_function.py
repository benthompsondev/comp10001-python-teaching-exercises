def convert_to_farenheit(celcius):
    return celcius * 9/5 + 32


celcius = int(input("Enter the temp in Celcius you want to convert: "))

#remember you need to convert the input to an integer with int()

print (celcius,"is equal to" ,convert_to_farenheit(celcius), "in farenheit")

print (convert_to_farenheit(celcius))
