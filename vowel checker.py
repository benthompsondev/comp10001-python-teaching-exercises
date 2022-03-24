# Python Program to Count Vowels in a String using loops

sentence = input("Please enter a sentence: ")

vowels = 0
sentence.lower()

#converts the sentence to lower case so we only check for lower case letters

for i in sentence:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
        vowels = vowels + 1
 
print("The Total Number of vowels in your sentence is ", vowels)
