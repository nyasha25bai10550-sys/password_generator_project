import random
import string

# --- Function jo password banata hai ---
def generate_password(length):
    # Saare characters ek jagah: ABC...abc..., 0-9, @#$% etc.
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Random characters ko jod kar password banta hai
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# --- User se length poochna ---
length = int(input("Kitne characters ka password chahiye? "))

# --- Final output ---
print("Yeh lo tumhara secure password:", generate_password(length))