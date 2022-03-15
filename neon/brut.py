from random import choice

correctPassword = "62192112"
wrongPasswords = set()

length = len(correctPassword)
chars = "6219"
run = True


while run:
    password = ''
    for i in range(length):
        password += choice(chars)

    if password not in wrongPasswords:
        if password != correctPassword:
            wrongPasswords.add(password)
            print(password)
        else:
            pass
            # run = False


print(password + " is correct")