import random

def characters():
    #Initializing the values
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
                'X', 'Y', 'Z']

    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
                'x', 'y', 'z']

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', ';', ':', "'", '"', '<', '>', ',', '.', '?', '/']

    name = username()
    length = ask() #Asking the length of the password
    result = event(length, uppercase, lowercase, numbers, special_characters) #Main event to generate password
    file(result, name)

def ask():
    length = int(input("Enter the length of password:"))
    return length

def username():
    print("..Password Generator..\n")
    user_name = input("Enter Username:")
    return user_name


def event(l, u, lwr, num, spec):
    password = ''
    for y in range(int(l/3)):
        #Initializing random value from above values
        upper_case = random.choice(u)
        lower_case = random.choice(lwr)
        number = random.choice(num)
        #special_character = random.choice(spec) ##If you want special character in password
        password = upper_case + lower_case  + str(number)  + password #Concatenating the values

    print("Password Generated:")
    print(f"Password:{password}")
    return password


def file(result, user_name):
    file_path = ''

    with open(file_path, 'a') as file_object:
        file_object.write(f'{user_name} : {result}\n')

characters()
