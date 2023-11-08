#A python program to illustrate Caesar Cipher Technique
def encrypt(text,s):
	# traverse text
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char != " ":
            if char.isupper():
                result += chr((ord(char) + s - 65) % 26 + 65)
            else:
                result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result += " "
    return result


#check the above function
text = input("Enter a message to encrypt: ")
s = int(input("Enter the shift value: "))
print ("Text : " + text)
print ("Shift : " + str(s))
print ("Cipher: " + encrypt(text,s))
