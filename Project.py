import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '@', '$', '%', '&', '*', '+', '-']

print("Passoword Generator!\n")

num_letters = int(input("Quantas letras você quer na sua senha? \n"))
num_symbols = int(input("Quantos simbolos você quer na sua senha? \n"))
num_numbers = int(input("Quantos números você quer na sua senha? \n"))

#primeira maneira, não muito segura
password = ""

for char in range(1, num_letters + 1):
    password += random.choice(letters)

for char in range(1, num_symbols + 1):
    password += random.choice(symbols)

for char in range(1, num_numbers + 1):
    password += random.choice(numbers)

print(password)

#segunda maneira, mais segura deixando os caracteres em ordem aleatoria
password_list = []

for char in range(1, num_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, num_symbols + 1):
    password_list.append(random.choice(symbols))

for char in range(1, num_numbers + 1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print((f"Sua senha é: {password}"))