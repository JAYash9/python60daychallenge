def strength(password):
    if len(password)>8:
        if any(char.isdigit() for char in password):
            if any(char.isupper()for char in password):
                return True
        
    else :
        print("Weak Password")
if strength("password123"):
    print("Strong Password")