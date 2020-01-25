text = input("Enter your message: ")
cipher = ''
shift = int(input("Enter shift 1-25: "))
for char in text:
    if  char.isalpha():
        char = char.upper()
        code = ord(char) + shift
    if code > ord('Z'):
        code = ord('A') + shift
    if code==" ":
        cipher += " "
    else:
        cipher += chr(code)

print(cipher)
