s = input("Enter a Phone Number:")

def phone_number(Phone):
    if s[0]== "(" and s[1-4].isdigit()and s[4]== ")" and s[5-8].isdigit():
        if s[8]=="-" and s[9-13].isdigit():
            return True
    else:
        return False

print("The Phone Number you entered is", phone_number(s))
