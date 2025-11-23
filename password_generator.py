import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
length = int(input("how many characters do you want in your password? "))

print("your password is ready:", generate_password(length))
