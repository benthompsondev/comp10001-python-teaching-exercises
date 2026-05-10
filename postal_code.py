

s = input("Enter a Postal code:")

def postal_code(Postal):
    if s[0].isalpha()and s[1].isdecimal()and s[2].isalpha() and s[3].isspace():
        if s[4].isdecimal() and s[5].isalpha() and s[6].isdecimal():
            return True
    else:
        return False

print("The Postal code you entered is", postal_code(s))
