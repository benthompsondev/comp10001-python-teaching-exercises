wordList = []
#makes an empty list

for i in range (5):
    w = input("Enter a word: ")
    wordList.append(w)

#asks the user for 5 strings and adds them to a list

wordList.sort()

#sorts the list in aphabetical order
print ()

for i in wordList:
    print(i)

#prints all items of the list
