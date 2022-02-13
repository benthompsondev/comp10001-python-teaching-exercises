soundsOuter = []

#created an empty outer list of the program to work


while True:
    soundsInner = []
    #created an inner list to make a list of lists for the program
    name = str(input("Enter an animal name (or done to quit): "))
    #Assume the user enters an animal name
    if name == "done":
               break
    # if user enters the word done stop the program and print the lyrics below
    else:
        soundsInner.append(name)
        sound = str(input("Enter an animal sound: "))
        soundsInner.append(sound)
        soundsOuter.append(soundsInner)
    #else continue asking the user for animal names and sounds and put them in the inner list
        
print ("")

#print an empty line so the lyrics to the song are separate from the user input requests to look better

for animal in soundsOuter:
    print ("Old MacDonald had a farm, E-I E-I O!")
    print ("And on that farm there was a",animal[0]+",","E-I E-I O!")
    print ("With a", animal[1]+",", animal[1], "here, and a", animal[1]+",", animal[1]+",", "there,")
    print ("Here a", animal[1]+",","there a", animal[1]+",","everywhere a", animal[1]+",",animal[1]+".",)
    print ("Old MacDonald had a farm, E-I E-I O!")
    print ("")
    # print an empty line so the verses are separated and looks better 
